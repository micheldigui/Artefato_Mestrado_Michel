import pandas as pd
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression, Ridge, Lasso
from sklearn.neighbors import KNeighborsRegressor
from sklearn.svm import SVR
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor, ExtraTreesRegressor, GradientBoostingRegressor, VotingRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from lightgbm import LGBMRegressor
from xgboost import XGBRegressor
from catboost import CatBoostRegressor

df = pd.read_parquet('dados/gold/gold_dataset_ml_limpo.parquet')
df['data_dt'] = pd.to_datetime(df['data_iso'])
df = df.sort_values('data_dt').reset_index(drop=True)

# Features puras (SEM NENHUMA FEATURE CALIBRADA ARTIFICIALMENTE)
f_memoria = [
    'consumo_mesmo_dia_sem_passada', 'consumo_mesmo_dia_sem_retrasada',
    'media_movel_5d', 'media_movel_10d', 'lag_1_dia_letivo', 'lag_5_dias_letivos'
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
# Reservas brutas (seja de alunos 2023-2025 ou nutricionista 2026, sem nenhum ajuste futuro)
f_reserva = ['reservas']

features_c1 = f_memoria + f_calendario + f_cardapio
features_c2 = features_c1 + f_clima
features_c3 = features_c2 + f_reserva

print("Features C1:", len(features_c1))
print("Features C2:", len(features_c2))
print("Features C3:", len(features_c3))

# Vamos testar os modelos sob Walk-Forward em 2026 (Semana t+1 e t+2) e verificar o comportamento das árvores
modelos = {
    "Regressao_Linear": Pipeline([("scaler", StandardScaler()), ("model", LinearRegression())]),
    "Ridge": Pipeline([("scaler", StandardScaler()), ("model", Ridge(alpha=1.0, random_state=42))]),
    "Lasso": Pipeline([("scaler", StandardScaler()), ("model", Lasso(alpha=0.1, random_state=42))]),
    "KNN": Pipeline([("scaler", StandardScaler()), ("model", KNeighborsRegressor(n_neighbors=5))]),
    "SVR": Pipeline([("scaler", StandardScaler()), ("model", SVR(C=50.0, epsilon=5.0))]),
    "Decision_Tree": DecisionTreeRegressor(max_depth=6, min_samples_split=5, random_state=42),
    "Random_Forest_Def": RandomForestRegressor(n_estimators=150, max_depth=10, min_samples_split=4, random_state=42, n_jobs=-1),
    "Extra_Trees": ExtraTreesRegressor(n_estimators=150, max_depth=10, min_samples_split=4, random_state=42, n_jobs=-1),
    "Gradient_Boosting": GradientBoostingRegressor(n_estimators=100, learning_rate=0.05, max_depth=4, random_state=42),
    "LightGBM": LGBMRegressor(n_estimators=100, learning_rate=0.05, max_depth=6, num_leaves=31, random_state=42, verbose=-1),
    "XGBoost": XGBRegressor(n_estimators=100, learning_rate=0.05, max_depth=5, random_state=42, verbosity=0),
    "CatBoost": CatBoostRegressor(iterations=100, learning_rate=0.05, depth=5, random_seed=42, verbose=0),
    "MLP_NeuralNet": Pipeline([("scaler", StandardScaler()), ("model", MLPRegressor(hidden_layer_sizes=(64, 32), max_iter=250, random_state=42))])
}

# Realizar o Walk-Forward em 2026 para Cenário 1, 2 e 3
df_2026 = df[(df['ano'] == 2026) & (df['consumo'].notna())]
sextas_2026 = sorted(df_2026[df_2026['dia_da_semana_num'] == 4]['data_dt'].unique())

print(f"Total de cortes semanais em 2026: {len(sextas_2026)}")

for c_nome, feats in [("C1_Cardapio", features_c1), ("C2_Clima", features_c2), ("C3_Com_Reserva", features_c3)]:
    print(f"\n==================== {c_nome} ====================")
    res_t1 = []
    for m_nome, model in modelos.items():
        y_true_all = []
        y_pred_all = []
        for sexta in sextas_2026:
            df_tr = df[(df['data_dt'] <= sexta) & (df['consumo'].notna())].dropna(subset=feats + ['consumo'])
            if len(df_tr) < 50:
                continue
            X_tr, y_tr = df_tr[feats], df_tr['consumo']
            try:
                model.fit(X_tr, y_tr)
            except Exception as e:
                continue
            df_te = df[(df['data_dt'] > sexta) & (df['data_dt'] <= sexta + pd.Timedelta(days=7)) & (df['consumo'].notna())].dropna(subset=feats)
            if len(df_te) > 0:
                preds = model.predict(df_te[feats])
                y_true_all.extend(df_te['consumo'].values)
                y_pred_all.extend(preds)
        if len(y_true_all) > 20:
            y_t = np.array(y_true_all)
            y_p = np.maximum(0, np.array(y_pred_all))
            mae = mean_absolute_error(y_t, y_p)
            rmse = np.sqrt(mean_squared_error(y_t, y_p))
            r2 = r2_score(y_t, y_p)
            wape = np.sum(np.abs(y_t - y_p)) / np.sum(y_t) * 100
            sobra = np.sum(np.maximum(0, y_p - y_t))
            falta = np.sum(np.maximum(0, y_t - y_p))
            res_t1.append((m_nome, mae, rmse, r2, wape, sobra, falta))
    
    res_df = pd.DataFrame(res_t1, columns=['Modelo', 'MAE', 'RMSE', 'R2', 'WAPE', 'Sobra', 'Falta']).sort_values('MAE')
    print(res_df.to_string(index=False))
