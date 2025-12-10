import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import sys
import subprocess
import requests
import json

class Jarvis:
    def __init__(self):
        # Initialize speech recognition
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        
        # Initialize text-to-speech
        self.engine = pyttsx3.init()
        self.engine.setProperty('rate', 180)
        self.engine.setProperty('volume', 0.9)
        
        # Set voice (try to use a male voice)
        voices = self.engine.getProperty('voices')
        for voice in voices:
            if 'male' in voice.name.lower() and 'female' not in voice.name.lower():
                self.engine.setProperty('voice', voice.id)
                break
        
        print("Jarvis initialized successfully!")
        self.speak("Hello sir, Jarvis is online and ready to assist you.")
    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Jarvis: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
    
    def listen(self):
        """Listen to user's voice command"""
        with self.microphone as source:
            print("\nListening...")
            self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
            try:
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                print("Processing...")
                command = self.recognizer.recognize_google(audio).lower()
                print(f"You said: {command}")
                return command
            except sr.WaitTimeoutError:
                return ""
            except sr.UnknownValueError:
                self.speak("Sorry sir, I didn't catch that. Could you please repeat?")
                return ""
            except sr.RequestError:
                self.speak("Sorry sir, speech recognition service is unavailable.")
                return ""
    
    def get_time(self):
        """Get current time"""
        now = datetime.datetime.now()
        time_str = now.strftime("%I:%M %p")
        self.speak(f"The time is {time_str}")
    
    def get_date(self):
        """Get current date"""
        now = datetime.datetime.now()
        date_str = now.strftime("%B %d, %Y")
        day = now.strftime("%A")
        self.speak(f"Today is {day}, {date_str}")
    
    def open_website(self, url):
        """Open a website"""
        webbrowser.open(url)
        self.speak(f"Opening {url}")
    
    def search_web(self, query):
        """Search on Google"""
        url = f"https://www.google.com/search?q={query}"
        webbrowser.open(url)
        self.speak(f"Here are the search results for {query}")
    
    def open_application(self, app_name):
        """Open system applications"""
        try:
            if sys.platform == "win32":
                # Windows applications
                apps = {
                    'notepad': 'notepad.exe',
                    'calculator': 'calc.exe',
                    'paint': 'mspaint.exe',
                    'chrome': 'chrome.exe',
                    'edge': 'msedge.exe',
                    'explorer': 'explorer.exe'
                }
                if app_name in apps:
                    os.startfile(apps[app_name])
                    self.speak(f"Opening {app_name}")
                else:
                    self.speak(f"Sorry sir, I don't know how to open {app_name}")
            elif sys.platform == "darwin":
                # macOS applications
                apps = {
                    'safari': 'Safari',
                    'chrome': 'Google Chrome',
                    'notes': 'Notes',
                    'calculator': 'Calculator',
                    'finder': 'Finder'
                }
                if app_name in apps:
                    subprocess.call(['open', '-a', apps[app_name]])
                    self.speak(f"Opening {app_name}")
                else:
                    self.speak(f"Sorry sir, I don't know how to open {app_name}")
            else:
                # Linux applications
                self.speak(f"Opening {app_name}")
                subprocess.Popen([app_name])
        except Exception as e:
            self.speak(f"Sorry sir, I couldn't open {app_name}")
            print(f"Error: {e}")
    
    def system_info(self):
        """Get system information"""
        platform = sys.platform
        if platform == "win32":
            os_name = "Windows"
        elif platform == "darwin":
            os_name = "macOS"
        else:
            os_name = "Linux"
        self.speak(f"You are running {os_name}")
    
    def process_command(self, command):
        """Process voice commands"""
        if not command:
            return True
        
        # Greetings
        if any(word in command for word in ['hello', 'hi', 'hey']):
            self.speak("Hello sir, how may I assist you?")
        
        # Time
        elif 'time' in command:
            self.get_time()
        
        # Date
        elif 'date' in command or 'today' in command:
            self.get_date()
        
        # Open websites
        elif 'open youtube' in command:
            self.open_website('https://www.youtube.com')
        elif 'open google' in command:
            self.open_website('https://www.google.com')
        elif 'open github' in command:
            self.open_website('https://www.github.com')
        elif 'open' in command and 'website' in command:
            self.speak("Which website would you like to open?")
            site = self.listen()
            if site:
                self.open_website(f'https://www.{site}.com')
        
        # Search
        elif 'search' in command or 'google' in command:
            query = command.replace('search', '').replace('google', '').strip()
            if query:
                self.search_web(query)
            else:
                self.speak("What would you like me to search for?")
                query = self.listen()
                if query:
                    self.search_web(query)
        
        # Open applications
        elif 'open' in command:
            app = command.replace('open', '').strip()
            self.open_application(app)
        
        # System info
        elif 'system' in command or 'operating system' in command:
            self.system_info()
        
        # Introduction
        elif 'who are you' in command or 'what are you' in command:
            self.speak("I am Jarvis, your personal AI voice assistant. I can help you with various tasks like opening applications, searching the web, telling time, and much more.")
        
        # Exit commands
        elif any(word in command for word in ['exit', 'quit', 'goodbye', 'bye', 'stop']):
            self.speak("Goodbye sir. Have a great day!")
            return False
        
        # Help
        elif 'help' in command or 'what can you do' in command:
            self.speak("I can help you with: telling time and date, opening websites and applications, searching the web, providing system information, and much more. Just ask me!")
        
        else:
            self.speak("I'm not sure how to help with that yet, but I'm learning every day!")
        
        return True
    
    def run(self):
        """Main loop"""
        while True:
            try:
                command = self.listen()
                if not self.process_command(command):
                    break
            except KeyboardInterrupt:
                self.speak("Shutting down. Goodbye sir!")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue

if __name__ == "__main__":
    jarvis = Jarvis()
    jarvis.run()
