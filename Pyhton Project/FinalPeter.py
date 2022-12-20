import pyttsx3  # pip install pyttsx3
import speech_recognition as sr  # pip install speechRecognition
import datetime
import wikipedia  # pip install wikipedia
import webbrowser
import os
import smtplib
import pyautogui as pag  # pip install pyautogui
import time
from pas import password

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("peter here. Sir how may I help you")


def takeCommand():
    # It takes microphone input from the user and returns string output
    speech = sr.Recognizer()  # it will help to recognize the voice
    with sr.Microphone() as source:  # it will use the microphoone as source
        print("Tell me what you want....")
        speech.pause_threshold = 1
        audio = speech.listen(source)

    try:
        print("Recognizing.....")
        query = speech.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print(" Say that again please.....")
        return "None"
    return query


def takeMessage():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()  # it will help to recognize the voice
    with sr.Microphone() as source:  # it will use the microphoone as source
        print("whats the message...")
        speak("whats the message")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def takeName():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()  # it will help to recognize the voice
    with sr.Microphone() as source:  # it will use the microphoone as source
        print("Tell me the name....")
        speak("Tell me the name")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"
    return query


def takeText():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()  # it will help to recognize the voice
    with sr.Microphone() as source:  # it will use the microphoone as source
        speak("You can start speaking")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def takeYN():
    # It takes microphone input from the user and returns string output
    r = sr.Recognizer()  # it will help to recognize the voice
    with sr.Microphone() as source:  # it will use the microphoone as source
        speak("say yes or no")
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('rishuyadav_ee20a14_56@dtu.ac.in', password())
    server.sendmail('sauravkumarmehar97@gmail.com', to, content)
    server.close()


if __name__ == "__main__":
    wishMe()
    thisdict = {
        "saurabh": "9821808096",
        "saurav": "9821808096",
        "rishu": "8447068664",
        "saroj": "9821808096"
    }
    while True:
        query = takeCommand().lower()
        # Logics for executing tasks based on query
        if 'who is' in query:
            speak('Wait few seconds')
            query = query.replace("who is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(1)
            speak("what else i can search for you")
            
        elif 'what is' in query:
            speak('Wait few seconds')
            query = query.replace("what is", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            time.sleep(1)
            speak("what else i can search for you")

        elif 'whatsapp' in query:  # send message to rishu verma on whatsapp
            message = takeMessage()
            while message == "None":
                message = takeMessage()

            name = takeName().lower()
            if thisdict.get(name) == None:
                while thisdict.get(name) == None:
                    name = takeName().lower()
            if thisdict.get(name) != None:
                webbrowser.open(f"https://wa.me/91{thisdict.get(name)}")

            time.sleep(7)
            pag.typewrite(message)
            pag.press("enter")

        elif 'speech to text' in query:
            f = open("myfile.txt", "x")
            txt = takeText()
            f = open("myfile.txt", "w")
            f.write(txt)
            f.close()

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\rishu\\Music\\Playlist'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        elif 'email' in query:
            try:
                speak("What should I say to Mr. saurav?")
                content = takeCommand()
                to = "rishuyadav5349@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent Syccessfully!")
            except Exception as e:
                print(e)
                speak("Sorry Sir, I am not able to send this email. You may try again.")

        elif 'quit' in query:
            speak("ok sir, have a nice day")
            break

        elif "shutdown" in query:
            speak("Are You sure you want to shutdown")
            print("Do you wish to shutdown your computer? (yes/no)")
            shutdown = input(takeYN().lower())
            print(shutdown)
            if 'yes' in shutdown:
                os.system("shutdown /s /t 1")
            elif 'no' in shutdown:
                speak("ok sir as you wish")

        else:
            speak("try again...")


