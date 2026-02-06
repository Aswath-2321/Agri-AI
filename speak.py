import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()

# Set voice properties (optional)
engine.setProperty('rate', 150)   # Speed (words per minute)
engine.setProperty('volume', 1.0) # Volume (0.0 to 1.0)

# Text you want to speak
text = "Hello! I am your AI assistant. I can listen and speak!"

# Speak
engine.say(text)
engine.runAndWait()
