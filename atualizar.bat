@echo off
cls
echo =========================================
echo   ENVIANDO NOVO VIDEO PARA O DASHBOARD
echo =========================================
echo.

:: Adiciona os arquivos garantindo o nome correto
git add data/IndicadoresTV.mp4
git add dashboard.py
git add requirements.txt
git add .streamlit/config.toml

:: Cria a mensagem de atualização
set d=%date% %time%
git commit -m "Atualizacao do Dashboard: %d%"

:: Envia para o GitHub usando a branch correta (master)
git push origin master

echo.
echo =========================================
echo   SUCESSO! AGUARDE 1 MINUTO E A TV ATUALIZARA.
echo =========================================
pause