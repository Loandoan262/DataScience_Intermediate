import pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime
import time as ti
from time import sleep
import psutil
import pyautogui
import pyjokes
import pywhatkit
import requests
import webbrowser as we
import os
import subprocess
import sys

#pip install py3-tts

user = "Lo-an"
assistant = "Eddy"

engine = pyttsx3.init()
voices = engine.getProperty("voices")

# for voice in voices:
#     if voice.languages[0] == u'en_US':
#         print(voice, voice.id)
#         engine.setProperty('voice', voice.id)
#         engine.say("Hello World!")
#         engine.runAndWait()
#         engine.stop()

# for index, name in enumerate(sr.Microphone.list_microphone_names()):
#     print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))

engine.setProperty("voice", "com.apple.eloquence.en-US.Eddy")
def output(audio):
    print(audio)
    engine.say(audio)
    engine.runAndWait()

def inputCommand():
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        listening = r.listen(source)
        query = r.recognize_google(listening, language = "en-EN")
    print(query)
    return query

def greet():
    output(f"Hello {user}. My name is {assistant}. How can I help you" )

def whatsapp_message():
    user_name = {"loan": "+4915121606048",
                 "Peter": "+4917643816491"}
    try:
        output("To whom you want to send the message?")
        name = inputCommand()
        output(f"You want to send {name} a message. What is it?")
        message = inputCommand()
        we.open_new_tab(f"https://web.whatsapp.com/send?phone={user_name[name]}&text={message}")
        sleep(7)
        pyautogui.press("enter")
        output("Message sent")
    except Exception as e:
        print(e)
        output("Sorry, unable to send the message")
def weather():
    city = "nuremberg"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(f"Temperature is {temp2} degree celsius. Weather is {temp1}")

def workspace():
    output("Which workspace you want to work on?")
    workspace = inputCommand()
    try:
        if sys.platform == "Windows":
            os.startfile("/Users/loandoan/" + workspace)
        else:
            opener = "open" if sys.platform == "darwin" else "xdg-open"
            subprocess.call([opener, "/Users/loandoan/" + workspace])
    except:
        output("Maybe your" + workspace + "does not exist. Try again please!")

def idea():
    output("What is your idea?")
    data = inputCommand().title()
    output("You told me to remember this idea: " + data)
    with open("data.txt", "a", encoding="utf-8") as r:
        print(data, file=r)

########---main---########
greet()

while True:
    query = inputCommand().lower()
    print(query)

    if "time" in query:
        output("Current time is " + datetime.datetime.now().strftime("%I:%M"))

    elif "date" in query:
        output("Today is " + str(datetime.datetime.now().day) +
               " " + str(datetime.datetime.now().month) +
               " " + str(datetime.datetime.now().year))

    elif "weather" in query:
        weather()

    elif "workspace" in query:
        workspace()

    elif "joke" in query:
        output(pyjokes.get_joke())

    elif "idea" in query:
        idea()

    elif "remind" in query:
        ideas = open("data.txt", "r")
        output(f"here are your ideas: {ideas.read()}")

    elif "whatsapp" in query:
        whatsapp_message()

    elif "google" in query:
        output("What do you want to search")
        content = inputCommand()
        we.open("https://www.google.com/search?q=" + content)
        output("Your search is shown. Please check!")

    elif "youtube" in query:
        output("What do you want to search on Youtube?")
        search_youtube = inputCommand()
        pywhatkit.playonyt(search_youtube)
        output("Your search is there!")

    elif "screenshot" in query:
        pyautogui.screenshot(str(ti.time()) + ".png").show()

    elif "cpu" in query:
        output(f"CPU is at {str(psutil.cpu_percent())} percent")

    elif "offline" in query:
        output(f"Happy to serve you, {user}. See you again!")
        quit()