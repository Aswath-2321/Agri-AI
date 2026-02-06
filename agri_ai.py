import openai
import pyttsx3

# Initialize TTS engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# OpenAI API key
openai.api_key = "YOUR_API_KEY_HERE"


def get_agri_response(question):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in agriculture. Answer all queries accurately."},
                {"role": "user", "content": question}
            ],
            max_tokens=300
        )
        answer = response['choices'][0]['message']['content']
        return answer
    except Exception as e:
        return f"Error: {e}"

# Main loop
while True:
    question = input("Ask any agriculture question (or type 'exit' to quit): ")
    if question.lower() == "exit":
        break

    answer = get_agri_response(question)
    print("\nAI says:", answer)

    # Speak the answer (with retry in case of long text)
    try:
        engine.say(answer)
        engine.runAndWait()
    except Exception as e:
        print("Error speaking:", e)
print("API Key Loaded:", openai.api_key)
