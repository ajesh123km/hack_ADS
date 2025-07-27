import pyttsx3
import os

def speak_text(text, filename="tts_output.mp3"):
    engine = pyttsx3.init()
    engine.save_to_file(text, filename)
    engine.runAndWait()
    return filename
