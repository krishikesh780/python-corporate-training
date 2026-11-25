@echo off
cd /d "%~dp0.."
if not exist .venv (
  echo Creating .venv ...
  python -m venv .venv
)
call .venv\Scripts\activate.bat
python -m pip install --upgrade pip
pip install -r requirements.txt
echo.
echo Activated. To use later: .venv\Scripts\activate.bat