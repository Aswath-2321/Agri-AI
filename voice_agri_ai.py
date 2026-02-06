import speech_recognition as sr
import pyttsx3
import time

# ---------- LOAD UNSTRUCTURED DATA ----------
def load_unstructured_data(file_path):
    """Load agriculture statements from file"""
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = [line.strip() for line in f if line.strip()]
    return lines

agri_data = load_unstructured_data("agri_data_unstructured.txt")

# ---------- TTS & STT ----------
engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

recognizer = sr.Recognizer()

def speak(text):
    """Speak text aloud"""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listen to user via microphone"""
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        print("Listening... Speak your question about agriculture:")
        audio = recognizer.listen(source)
    try:
        query = recognizer.recognize_google(audio)
        print("You said:", query)
        return query
    except sr.UnknownValueError:
        speak("Sorry, I could not understand your voice. Please try again.")
        return None
    except sr.RequestError as e:
        speak(f"Error: {e}")
        return None

# ---------- OFFLINE Q&A SEARCH ----------
def get_agri_answer_offline(user_question):
    """Search unstructured data for keywords and return matching answer"""
    user_question = user_question.lower()
    for line in agri_data:
        # Match if any word from user question is in a line
        if any(word in line.lower() for word in user_question.split()):
            return line
    return "Sorry, I don't have information on that. Please ask another question."

# ---------- MAIN LOOP ----------
speak("Hello! I am your offline Agriculture AI assistant. You can ask me any question about farming.")
time.sleep(1)

while True:
    
    query = listen()
    if query:
        if query.lower() in ["exit", "quit", "stop"]:
            speak("Goodbye! Happy farming.")
            break
        answer = get_agri_answer_offline(query)
        print("AI says:", answer)
        speak(answer)
    time.sleep(1)

