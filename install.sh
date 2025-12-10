#!/bin/bash

echo "========================================"
echo "Jarvis Voice Assistant - Setup"
echo "========================================"
echo ""

# Detect OS
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
    echo "Detected Linux system"
    echo "Installing system dependencies..."
    sudo apt-get update
    sudo apt-get install -y python3-pyaudio portaudio19-dev espeak
elif [[ "$OSTYPE" == "darwin"* ]]; then
    echo "Detected macOS system"
    echo "Installing system dependencies..."
    brew install portaudio
fi

echo ""
echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo ""
echo "========================================"
echo "Installation Complete!"
echo "========================================"
echo ""
echo "To run Jarvis, type: python3 jarvis.py"
echo ""
