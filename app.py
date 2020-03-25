import speech_recognition as sr
import os
import sys
import webbrowser
import pyttsx3

def talk(text):
    print(text)
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


talk("check")

def command(arg= "Speak"):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        talk(arg)
        r.pause_threshold = 0.5
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source)

    try:
        achivement = r.recognize_google(audio).lower()
        print("You said: " + achivement)
    except sr.UnknownValueError:
        talk("I don't get what you are saying")
        achivement = command("Repeat please")

    return achivement


def Achive(achivement):
    if "open website" in achivement:
        achivement = achivement.replace("open website", "")
        print(achivement)
        talk("Searching for" + achivement)
        url = achivement
        webbrowser.open(url)
    if "stop" in achivement:
        ans = command("If you sure you want to stop running the programm say yes")
        if ans == "yes":
            exit()


while True:
    Achive(command())
