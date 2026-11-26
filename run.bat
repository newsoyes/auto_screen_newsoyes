@echo off
chcp 65001 >nul
title Auto Screen Capture - NEWSOYES
cd /d "%~dp0"
echo ==================================================
echo   📸 Auto Screen Capture ^& Split-Window Tool
echo   กำลังตรวจสอบและติดตั้งไลบรารีที่จำเป็น...
echo ==================================================
python -m pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [ERROR] กรุณาติดตั้ง Python 3.8+ ก่อนใช้งาน
    pause
    exit /b 1
)
echo กำลังเปิดโปรแกรม...
python auto_screen_newsoyes.py
pause
