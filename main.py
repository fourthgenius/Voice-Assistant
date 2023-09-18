import speech_recognition as sr
from time import ctime
import time
import webbrowser as wb
import playsound
import os
import random
from gtts import gTTS

r = sr.Recognizer()

def record_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            voice_data = r.recognize_google(audio)
            print(voice_data)
        except sr.UnknownValueError:
            print("Sorry I did not Understand that")
        except sr.RequestError:
            print("Sorry, cant reach servers right now")
        except:
            print("Try again")
        return voice_data


def respond(voice_data):
    if "what is your name" in voice_data:
        assistant_speak("My name is Bro")
    if "time" in voice_data:
        assistant_speak(ctime())
    if "search" in voice_data:
        assistant_speak("What do you want to search for?")
        google_search = record_audio()
        url = "https://google.com/search?q=" + google_search
        wb.get().open(url)
        assistant_speak("Here's what I found on Google for " + google_search)
    if "YouTube" in voice_data:
        assistant_speak("What do you want to search in Youtube?")
        yt_search = record_audio()
        url = "https://www.youtube.com/results?search_query=" + yt_search
        wb.get().open(url)
        assistant_speak("Here's what I found on YouTube.")
    if "find location" in voice_data:
        assistant_speak("What is the location?")
        location = record_audio()
        url = "https://www.google.com/maps/place/" + location + "/&amp;"
        wb.get().open(url)
        assistant_speak("Here's the Location")
    if "exit" in voice_data:
        print("Bye")
        exit()

def assistant_speak(audio_string):
    tts = gTTS(text= audio_string, lang="en")
    r = random.randint(1,10000000)
    audio_file = "audio-" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)
  
time.sleep(1)
assistant_speak("How can i help you?")
while 1:
    voice_data = record_audio()
    respond(voice_data)
