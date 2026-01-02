@echo off
cd /d "%~dp0"
echo Starting Streamlit App...
".venv\Scripts\python.exe" -m streamlit run app.py
if errorlevel 1 pause
