# 🤖 Jarvis Voice Assistant

Your personal AI-powered voice assistant inspired by Iron Man's Jarvis! Control your computer, search the web, and get information using just your voice.

## ✨ Features

- 🎤 **Voice Recognition**: Understands natural language commands
- 🔊 **Text-to-Speech**: Responds with natural voice
- 🌐 **Web Control**: Open websites and search Google
- 💻 **Application Control**: Launch system applications
- ⏰ **Time & Date**: Get current time and date
- 🖥️ **System Info**: Check system information
- 🔄 **Continuous Listening**: Always ready for your commands

## 🎯 Voice Commands

### Greetings
- "Hello Jarvis"
- "Hi Jarvis"

### Time & Date
- "What time is it?"
- "Tell me the time"
- "What's the date today?"

### Web Browsing
- "Open YouTube"
- "Open Google"
- "Open GitHub"
- "Search for [query]"
- "Google [query]"

### Applications
- "Open notepad"
- "Open calculator"
- "Open chrome"
- "Open [application name]"

### System
- "What's my operating system?"
- "System information"

### Help & Info
- "What can you do?"
- "Help"
- "Who are you?"

### Exit
- "Exit"
- "Goodbye"
- "Stop"

## 🚀 Installation

### Prerequisites

- Python 3.7 or higher
- Microphone
- Internet connection (for speech recognition)

### Windows Installation

1. **Clone the repository**
```bash
git clone https://github.com/rahul700raj/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. **Install Python dependencies**
```bash
pip install -r requirements.txt
```

3. **Install PyAudio** (Required for microphone access)
```bash
pip install pipwin
pipwin install pyaudio
```

4. **Run Jarvis**
```bash
python jarvis.py
```

### macOS Installation

1. **Clone the repository**
```bash
git clone https://github.com/rahul700raj/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. **Install dependencies**
```bash
pip3 install -r requirements.txt
brew install portaudio
pip3 install pyaudio
```

3. **Run Jarvis**
```bash
python3 jarvis.py
```

### Linux Installation

1. **Clone the repository**
```bash
git clone https://github.com/rahul700raj/jarvis-voice-assistant.git
cd jarvis-voice-assistant
```

2. **Install system dependencies**
```bash
sudo apt-get update
sudo apt-get install python3-pyaudio portaudio19-dev
sudo apt-get install espeak
```

3. **Install Python dependencies**
```bash
pip3 install -r requirements.txt
```

4. **Run Jarvis**
```bash
python3 jarvis.py
```

## 🔧 Auto-Start on System Boot

### Windows

1. Press `Win + R`, type `shell:startup`, press Enter
2. Create a shortcut to `jarvis.py` in the Startup folder
3. Or create a batch file:

```batch
@echo off
cd C:\path\to\jarvis-voice-assistant
python jarvis.py
```

### macOS

1. Create a `.plist` file in `~/Library/LaunchAgents/`
2. Add auto-start configuration
3. Or use Automator to create a startup application

### Linux

1. Create a systemd service:
```bash
sudo nano /etc/systemd/system/jarvis.service
```

2. Add configuration:
```ini
[Unit]
Description=Jarvis Voice Assistant
After=network.target

[Service]
ExecStart=/usr/bin/python3 /path/to/jarvis-voice-assistant/jarvis.py
Restart=always
User=yourusername

[Install]
WantedBy=multi-user.target
```

3. Enable and start:
```bash
sudo systemctl enable jarvis.service
sudo systemctl start jarvis.service
```

## 🎨 Customization

### Change Voice Settings

Edit `jarvis.py` and modify:
```python
self.engine.setProperty('rate', 180)  # Speed of speech
self.engine.setProperty('volume', 0.9)  # Volume (0.0 to 1.0)
```

### Add Custom Commands

Add new commands in the `process_command()` method:
```python
elif 'your command' in command:
    # Your custom action
    self.speak("Response")
```

## 🐛 Troubleshooting

### Microphone Not Working
- Check microphone permissions in system settings
- Ensure microphone is set as default input device
- Test microphone with other applications

### PyAudio Installation Issues
- **Windows**: Use `pipwin install pyaudio`
- **macOS**: Install portaudio first: `brew install portaudio`
- **Linux**: Install system packages: `sudo apt-get install python3-pyaudio`

### Speech Recognition Errors
- Check internet connection (Google Speech API requires internet)
- Speak clearly and at moderate pace
- Reduce background noise

## 📝 License

MIT License - Feel free to modify and distribute!

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 👨‍💻 Author

**Rahul Mishra**
- GitHub: [@rahul700raj](https://github.com/rahul700raj)
- Email: rm2778643@gmail.com

## 🙏 Acknowledgments

- Inspired by Iron Man's Jarvis
- Built with Python and open-source libraries
- Powered by Google Speech Recognition

---

**Made with ❤️ by Rahul Mishra**
