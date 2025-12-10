@echo off
echo ========================================
echo Jarvis Voice Assistant - Windows Setup
echo ========================================
echo.

echo Installing Python dependencies...
pip install -r requirements.txt

echo.
echo Installing PyAudio...
pip install pipwin
pipwin install pyaudio

echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo To run Jarvis, type: python jarvis.py
echo.
pause
