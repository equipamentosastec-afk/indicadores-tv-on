@echo off
cls
echo =========================================
echo   ENVIANDO NOVO VIDEO PARA O DASHBOARD
echo =========================================
echo.

:: Adiciona apenas o arquivo de vídeo (para ser mais rápido)
git add data/video.mp4
git add dashboard.py
git add requirements.txt

:: Cria a mensagem de atualização com data e hora
set d=%date% %time%
git commit -m "Atualizacao do Dashboard: %d%"

:: Envia para o GitHub
git push origin main

echo.
echo =========================================
echo   SUCESSO! AGUARDE 1 MINUTO E A TV ATUALIZARA.
echo =========================================
pause