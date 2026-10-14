"""
Módulo de Modelagem Preditiva Multi-Estágio com Walk-Forward Validation
Projeto: Artefato de Previsão de Demanda de Refeições - IFSP Campus Itaquaquecetuba
Mestrado Profissional

Simula a tomada de decisão operacional às sextas-feiras:
- Semana t+1 (Lead time de 1 semana, com estimativa da nutricionista disponível)
- Semana t+2 (Lead time de 2 semanas, SEM estimativas humanas - puramente autônomo)
- Re-forecast / Ajuste: Ganho de acurácia obtido na transição de t+2 para t+1 ao receber a estimativa.
- Compara 11 famílias de algoritmos e Ensembles sob 3 cenários de dados (Ablation Study).
"""

import os
import warnings
import pandas as pd
import numpy as np

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, VotingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

warnings.filterwarnings("ignore")

GOLD_ML_PATH = "dados/gold/gold_dataset_ml_limpo.parquet"
OUTPUT_DIR = "dados/gold"

def calcular_wape(y_true, y_pred):
    """Weighted Absolute Percentage Error: soma(|y - y_hat|) / soma(y)"""
    soma_y = np.sum(y_true)
    if soma_y == 0:
        return 0.0
    return np.sum(np.abs(y_true - y_pred)) / soma_y * 100.0

def calcular_sobra_falta(y_true, y_pred):
    """Calcula total de refeições com sobra (pred > real) e falta (real > pred)."""
    sobra = np.sum(np.maximum(0, y_pred - y_true))
    falta = np.sum(np.maximum(0, y_true - y_pred))
    return sobra, falta

def obter_modelos():
    """Retorna o dicionário de modelos configurados com pipelines apropriados."""
    return {
        "Regressao_Linear": Pipeline([("scaler", StandardScaler()), ("model", LinearRegression())]),
        "Ridge": Pipeline([("scaler", StandardScaler()), ("model", Ridge(alpha=10.0, random_state=42))]),
        "Lasso": Pipeline([("scaler", StandardScaler()), ("model", Lasso(alpha=0.5, random_state=42))]),
        "KNN": Pipeline([("scaler", StandardScaler()), ("model", KNeighborsRegressor(n_neighbors=5))]),
        "SVR": Pipeline([("scaler", StandardScaler()), ("model", SVR(C=50.0, epsilon=5.0))]),
        "Decision_Tree": DecisionTreeRegressor(max_depth=5, random_state=42),
        "Random_Forest": RandomForestRegressor(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1),
        "Extra_Trees": ExtraTreesRegressor(n_estimators=100, max_depth=8, random_state=42, n_jobs=-1),
        "LightGBM": LGBMRegressor(n_estimators=100, learning_rate=0.05, max_depth=5, random_state=42, verbose=-1),
        "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.05, max_depth=4, random_state=42, verbosity=0),
        "CatBoost": CatBoostRegressor(iterations=100, learning_rate=0.05, depth=4, random_seed=42, verbose=0),
        "MLP_NeuralNet": Pipeline([("scaler", StandardScaler()), ("model", MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=200, random_state=42))])
    }

def definir_features_por_cenario():
    """Define as features selecionadas para cada cenário experimental."""
    f_memoria = [
        'consumo_mesmo_dia_sem_passada', 'consumo_mesmo_dia_sem_retrasada',
        'media_movel_5d', 'media_movel_10d', 'lag_5_dias_letivos', 'lag_10_dias_letivos'
    ]
    f_calendario = [
        'dia_da_semana_num', 'dia_do_mes', 'mes', 'semana_do_ano',
        'is_segunda', 'is_terca', 'is_quarta', 'is_quinta', 'is_sexta'
    ]
    f_cardapio = [
        'proteina_frango', 'proteina_bovina', 'proteina_suina', 'proteina_peixe', 'proteina_feijoada',
        'score_atratividade_proteina', 'score_atratividade_preparo'
    ]
    f_clima = [
        'precipitation_sum', 'precipitation_hours', 'temperature_2m_max', 'wind_speed_10m_max',
        'indice_adversidade_climatica', 'is_chuva_forte'
    ]
    f_reserva = [
        'reservas', 'estimativa_nutricionista_calibrada'
    ]
    
    cenario_1_puro = f_memoria + f_calendario + f_cardapio
    cenario_2_clima = cenario_1_puro + f_clima
    cenario_3_reserva = cenario_2_clima + f_reserva
    
    return {
        "Cenario_1_Base_Cardapio": cenario_1_puro,
        "Cenario_2_Com_Clima": cenario_2_clima,
        "Cenario_3_Com_Nutricionista": cenario_3_reserva
    }

def executar_walk_forward():
    print("[*] Carregando dados da Camada Gold para Walk-Forward Validation...")
    df = pd.read_parquet(GOLD_ML_PATH)
    df["data_dt"] = pd.to_datetime(df["data_iso"])
    df = df.sort_values("data_dt").reset_index(drop=True)
    
    cenarios = definir_features_por_cenario()
    
    # Identificar todas as sextas-feiras de 2026 onde temos dados suficientes
    df_2026 = df[(df["ano"] == 2026) & (df["consumo"].notna())].copy()
    sextas_feiras = df_2026[df_2026["dia_da_semana_num"] == 4]["data_dt"].unique()
    sextas_feiras = sorted(sextas_feiras)
    
    print(f"[+] Total de semanas de corte identificadas em 2026: {len(sextas_feiras)}")
    
    # Coletor de métricas
    resultados = []
    
    # Modelos candidatos
    modelos_dict = obter_modelos()
    
    for cenario_nome, feature_cols in cenarios.items():
        print(f"\n[*] Executando Experimento: {cenario_nome} (Total de features: {len(feature_cols)})...")
        
        # Avaliar cada modelo
        for mod_nome, model in modelos_dict.items():
            
            y_true_t1_todas = []
            y_pred_t1_todas = []
            
            y_true_t2_todas = []
            y_pred_t2_todas = []
            
            for sexta in sextas_feiras:
                # 1. Treino: tudo até a sexta-feira de corte T
                df_treino = df[(df["data_dt"] <= sexta) & (df["consumo"].notna())].dropna(subset=feature_cols + ["consumo"])
                if len(df_treino) < 50:
                    continue
                    
                X_tr = df_treino[feature_cols]
                y_tr = df_treino["consumo"]
                
                # Ajustar modelo
                try:
                    model.fit(X_tr, y_tr)
                except Exception as e:
                    continue
                    
                # 2. Teste Semana t+1 (próximos 5 dias úteis)
                df_t1 = df[(df["data_dt"] > sexta) & (df["data_dt"] <= sexta + pd.Timedelta(days=7)) & (df["consumo"].notna())]
                df_t1 = df_t1.dropna(subset=feature_cols)
                if len(df_t1) > 0:
                    y_pred_t1 = model.predict(df_t1[feature_cols])
                    y_true_t1_todas.extend(df_t1["consumo"].values)
                    y_pred_t1_todas.extend(y_pred_t1)
                    
                # 3. Teste Semana t+2 (dias úteis de 8 a 14 dias após T) - Não se aplica a Cenário com Reserva
                if "Nutricionista" not in cenario_nome:
                    df_t2 = df[(df["data_dt"] > sexta + pd.Timedelta(days=7)) & (df["data_dt"] <= sexta + pd.Timedelta(days=14)) & (df["consumo"].notna())]
                    df_t2 = df_t2.dropna(subset=feature_cols)
                    if len(df_t2) > 0:
                        y_pred_t2 = model.predict(df_t2[feature_cols])
                        y_true_t2_todas.extend(df_t2["consumo"].values)
                        y_pred_t2_todas.extend(y_pred_t2)
                        
            # Consolidar métricas para t+1
            if len(y_true_t1_todas) >= 20:
                y_tr_t1 = np.array(y_true_t1_todas)
                y_pr_t1 = np.maximum(0, np.array(y_pred_t1_todas))
                
                mae_t1 = mean_absolute_error(y_tr_t1, y_pr_t1)
                rmse_t1 = np.sqrt(mean_squared_error(y_tr_t1, y_pr_t1))
                r2_t1 = r2_score(y_tr_t1, y_pr_t1)
                wape_t1 = calcular_wape(y_tr_t1, y_pr_t1)
                sobra_t1, falta_t1 = calcular_sobra_falta(y_tr_t1, y_pr_t1)
                
                resultados.append({
                    "cenario": cenario_nome,
                    "horizonte": "Semana_t1 (Curto Prazo)",
                    "algoritmo": mod_nome,
                    "mae": round(mae_t1, 2),
                    "rmse": round(rmse_t1, 2),
                    "r2": round(r2_t1, 3),
                    "wape_pct": round(wape_t1, 2),
                    "total_sobra_ref": int(sobra_t1),
                    "total_falta_ref": int(falta_t1)
                })
                
            # Consolidar métricas para t+2 (se aplicável)
            if len(y_true_t2_todas) >= 20:
                y_tr_t2 = np.array(y_true_t2_todas)
                y_pr_t2 = np.maximum(0, np.array(y_pred_t2_todas))
                
                mae_t2 = mean_absolute_error(y_tr_t2, y_pr_t2)
                rmse_t2 = np.sqrt(mean_squared_error(y_tr_t2, y_pr_t2))
                r2_t2 = r2_score(y_tr_t2, y_pr_t2)
                wape_t2 = calcular_wape(y_tr_t2, y_pr_t2)
                sobra_t2, falta_t2 = calcular_sobra_falta(y_tr_t2, y_pr_t2)
                
                resultados.append({
                    "cenario": cenario_nome,
                    "horizonte": "Semana_t2 (Longo Prazo)",
                    "algoritmo": mod_nome,
                    "mae": round(mae_t2, 2),
                    "rmse": round(rmse_t2, 2),
                    "r2": round(r2_t2, 3),
                    "wape_pct": round(wape_t2, 2),
                    "total_sobra_ref": int(sobra_t2),
                    "total_falta_ref": int(falta_t2)
                })

    # Benchmark: Estimativa pura da nutricionista (semana t+1)
    df_2026_val = df_2026[df_2026["reservas"].notna() & df_2026["consumo"].notna()]
    y_real_nutri = df_2026_val["consumo"].values
    y_pred_nutri = df_2026_val["reservas"].values
    mae_nutri = mean_absolute_error(y_real_nutri, y_pred_nutri)
    rmse_nutri = np.sqrt(mean_squared_error(y_real_nutri, y_pred_nutri))
    r2_nutri = r2_score(y_real_nutri, y_pred_nutri)
    wape_nutri = calcular_wape(y_real_nutri, y_pred_nutri)
    sobra_nutri, falta_nutri = calcular_sobra_falta(y_real_nutri, y_pred_nutri)
    
    resultados.append({
        "cenario": "Benchmark_Humano",
        "horizonte": "Semana_t1 (Curto Prazo)",
        "algoritmo": "Estimativa_Nutricionista_Pura",
        "mae": round(mae_nutri, 2),
        "rmse": round(rmse_nutri, 2),
        "r2": round(r2_nutri, 3),
        "wape_pct": round(wape_nutri, 2),
        "total_sobra_ref": int(sobra_nutri),
        "total_falta_ref": int(falta_nutri)
    })
    
    df_res = pd.DataFrame(resultados)
    
    # Salvar resultados
    p_parquet = f"{OUTPUT_DIR}/metricas_modelos_cenarios.parquet"
    p_csv = f"{OUTPUT_DIR}/metricas_modelos_cenarios.csv"
    df_res.to_parquet(p_parquet, index=False)
    df_res.to_csv(p_csv, sep=";", index=False, encoding="utf-8-sig")
    
    print("\n[OK] Experimento Walk-Forward concluído!")
    print(f"    Tabela de métricas salva em: {p_parquet} e {p_csv}")
    
    return df_res

if __name__ == "__main__":
    df_res = executar_walk_forward()
    print("\nTop 5 Melhores Modelos para Semana t+1 (Menor MAE):")
    top_t1 = df_res[df_res["horizonte"] == "Semana_t1 (Curto Prazo)"].sort_values("mae").head(8)
    print(top_t1[["cenario", "algoritmo", "mae", "rmse", "r2", "wape_pct", "total_sobra_ref", "total_falta_ref"]].to_string())
    
    print("\nTop 5 Melhores Modelos para Semana t+2 (Previsão Pura 2 semanas antes):")
    top_t2 = df_res[df_res["horizonte"] == "Semana_t2 (Longo Prazo)"].sort_values("mae").head(8)
    print(top_t2[["cenario", "algoritmo", "mae", "rmse", "r2", "wape_pct", "total_sobra_ref", "total_falta_ref"]].to_string())
