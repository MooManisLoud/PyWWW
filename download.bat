@echo off

python --version >nul 2>&1
if errorlevel 1 (
    echo In order for PyWWW to run its needs python whats used to be coded.
    echo.
     set /p download=Do you want to download Python now? (y/n)
    if /i "%download%"=="y" (
        echo Downloading Python...
        start "" https://www.python.org/downloads/
        echo Please install Python and try again.
        pause
        exit /b 1
)

pip install -r requirements.txt

pause
