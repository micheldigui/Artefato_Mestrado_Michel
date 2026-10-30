@echo off
title Artefato de Previsao de Refeicoes - Mestrado PPG-GTSP
echo ======================================================================
echo    ARTEFATO DE APOIO A DECISAO: PREVISAO DE REFEICOES ESCOLARES
echo    Mestrado Profissional em Gestao e Tecnologia em Sistemas Produtivos
echo ======================================================================
echo.
echo Iniciando o servidor web local em http://localhost:8501 ...
echo O navegador abrira automaticamente. Para encerrar, feche esta janela.
echo.
python -m streamlit run src/app/main.py
pause
