import speech_recognition as sr
import pyttsx3
import pywhatkit as kit
import datetime
import webbrowser
import os

# Initialize the recognizer
recognizer = sr.Recognizer()

# Initialize the Text-to-Speech engine
engine = pyttsx3.init()

# Set properties for voice (optional)
engine.setProperty('rate', 150)  # Speed of speech
engine.setProperty('volume', 1)  # Volume (0.0 to 1.0)


# Function to speak to the user
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen to the user's voice
def listen():
    with sr.Microphone() as source:
        print("Listening for your command...")
        recognizer.adjust_for_ambient_noise(source)  # Adjusts for ambient noise
        audio = recognizer.listen(source)
    return audio


# Function to recognize speech
def recognize_speech(audio):
    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio)
        print(f"You said: {command}\n")
        return command.lower()
    except sr.UnknownValueError:
        print("Sorry, I couldn't understand that.")
        return None
    except sr.RequestError:
        print("Sorry, the service is down.")
        return None


# Function to execute the assistant's tasks
def execute_command(command):
    if "hello" in command:
        speak("Hello! How can I assist you today?")

    elif "time" in command:
        now = datetime.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}")

    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube")
        kit.playonyt(song)

    elif "search" in command:
        query = command.replace("search", "").strip()
        speak(f"Searching for {query} on Google")
        kit.search(query)

    elif "open" in command:
        website = command.replace("open", "").strip()
        speak(f"Opening {website}")
        webbrowser.open(f"https://{website}.com")

    elif "bye" in command:
        speak("Goodbye, have a nice day!")
        exit()


# Main loop for voice assistant
def main():
    speak("I am your virtual assistant. How can I help you?")
    while True:
        audio = listen()
        command = recognize_speech(audio)
        if command:
            execute_command(command)


if __name__ == "__main__":
    main()