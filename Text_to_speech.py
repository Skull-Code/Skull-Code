# Github: SkullCode

# U NEED 'SPEECHRECOGNITION, GTTS, PLAYSOUND' INSTALLED
# Install Command: 'pip install speech_recognition'
# Install Command: 'pip install gtts'
# Install Command: 'pip install playsound'

# Any bugs contact SkullCode#1878



import speech_recognition as sr
from gtts import gTTS
import os
import playsound

def speak (text):
    tts = gTTS(text = text,lang="en") #Not u must enter the part of a mp3 data must named 'sound.mp3'
    if os.path.exists(r"C:\Music\sound.mp3"):
        os.remove(r"C:\Music\sound.mp3")
    filename = r"C:\Music\sound.mp3"
    tts.save(sound.mp3)
    playsound.playsound(sound.mp3)

# Here u can write what u want to say
speak("Some words")