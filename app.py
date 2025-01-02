import streamlit as st
import speech_recognition as sr
import pyttsx3
import threading

# Initialize Text-to-Speech Engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to user input and converts speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening... Please ask a question.")
        try:
            audio = recognizer.listen(source, timeout=10)
            user_input = recognizer.recognize_google(audio)
            return user_input.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that. Please try again."
        except sr.RequestError:
            return "Speech recognition service is unavailable. Please check your internet connection."

def process_question(question):
    """Processes the user's question and provides a voice response."""
    responses = {
        "what is the capital of india": "The capital of India is New Delhi.",
        "who is the prime minister of india": "The Prime Minister of India is Narendra Modi.",
        "what is the national animal of india": "The national animal of India is the Bengal Tiger."
    }
    response = responses.get(question, "Sorry, I do not have an answer to that question.")
    return response

# Streamlit UI
st.title("Voice-to-Voice Assistant for Blind Users")

st.write("Speak your question. Example: 'What is the capital of India?'")

if st.button("Start Voice Interaction"):
    def interact():
        # Listen to user input
        user_input = listen()
        st.write(f"You said: {user_input}")
        speak(f"You said: {user_input}")

        # Process question and give response
        response = process_question(user_input)
        st.write(f"Assistant: {response}")
        speak(response)

    # Run interaction in a separate thread to prevent blocking
    interaction_thread = threading.Thread(target=interact)
    interaction_thread.start()
