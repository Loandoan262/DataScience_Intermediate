import pyttsx3
import speech_recognition as sr #pip install speechrecognition
import datetime
import psutil
import pyautogui
import pyjokes
import pywhatkit
import requests
import time as ti
from time import sleep
import webbrowser as we
import os
import subprocess
import sys
#pip install py3-tts

user = "Lo-an"
assistant = "Eddy"

engine = pyttsx3.init()
voices = engine.getProperty("voices")

# For Mail voice
engine.setProperty("voice", "com.apple.eloquence.en-US.Eddy")

# engine = pyttsx3.init()
# voices = engine.getProperty('voices')
# for voice in voices:
#     if voice.languages[0] == u'en_US':
#         print(voice, voice.id)
#         engine.setProperty('voice', voice.id)
#         engine.say("Hello World!")
#         engine.runAndWait()
#         engine.stop()
def output(audio):
    print(audio) # For printing out the output
    engine.say(audio)
    engine.runAndWait()

# For getting the device index you can execute this code So if you want to change the device you can do that.
for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print("Microphone with name \"{1}\" found for Microphone(device_index={0})".format(index, name))

def inputCommand():
    # query = input() # For getting input from CLI
    r = sr.Recognizer()
    query = ""
    with sr.Microphone(device_index=2) as source:
        print("Listening...")
        r.pause_threshold = .5
        try:
            query = r.recognize_google(r.listen(source), language="en-EN")
        except Exception as e:
            output("Say that again Please...")
    print(query)
    return query

def greet():
    hour = datetime.datetime.now().hour
    print(hour)
    if (hour >= 0) and (hour < 12):
        output(f"Good Morning {user}. My name is {assistant}")
    elif (hour >= 12) and (hour < 18):
        output(f"Good afternoon {user}. My name is {assistant}")
    elif (hour >= 18) and (hour < 24):
        output(f"Good Evening {user}. My name is {assistant}")
    output("How may I assist you?")

def weather():
    city = "nuremberg"
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=16f0afad2fd9e18b7aee9582e8ce650b&units=metric").json()
    temp1 = res["weather"][0]["description"]
    temp2 = res["main"]["temp"]
    output(
        f"Temperature is {format(temp2)} degree Celsius \nWeather is {format(temp1)}")
def sendWhatMsg():
    user_name = {
        "loan": '+4915121606048',
        "Patrick": "+4917643816491"
    }
    try:
        output("To whom you want to send the message?")
        name = inputCommand()
        output("You want to send" + name + ". What is the message")
        we.open_new_tab(f"https://web.whatsapp.com/send?phone={user_name[name]}&text={inputCommand()}")
        sleep(7)
        pyautogui.press('enter')
        output("Message sent")
    except Exception as e:
        print(e)
        output("Unable to send the Message")

def idea():
    output("What is your idea?")
    data = inputCommand().title()
    output("You told me to remember this idea: " + data)
    with open("data.txt", "a", encoding="utf-8") as r:
        print(data, file=r)


greet()
# Then with while true we can make it a infinite loop on command
while True:
    # Getting input from the user
    query = inputCommand().lower()
    print(query)
    # According to the query if query have respective word we will execute the respective command

    if ("time" in query):
        output("Current time is " +
               datetime.datetime.now().strftime("%I:%M"))

    elif ('date' in query):
        output("Current date is " + str(datetime.datetime.now().day)
               + " " + str(datetime.datetime.now().month)
               + " " + str(datetime.datetime.now().year))

    elif ('whatsapp' in query):
        print("Sending...")
        sendWhatMsg()


    elif ("search" in query):
        output("what you want to search?")
        we.open("https://www.google.com/search?q=" + inputCommand())
        output("Your search is shown. You need to read yourself. I'm tired!")

    elif ("youtube" in query):
        output("What you want to search on Youtube?")
        pywhatkit.playonyt(inputCommand())

    elif ('weather' in query):
        weather()

    elif ("space" in query):
        output("Which workspace you want to work on")
        try:
            if sys.platform == "Windows":
                os.startfile("/Users/loandoan/" + inputCommand())
            else:
                opener = "open" if sys.platform == "darwin" else "xdg-open"
                subprocess.call([opener, "/Users/loandoan/" + inputCommand()])
        except Exception as e:
            print(e)
            output("Unable to send the Message")

    elif ("joke" in query):
        output(pyjokes.get_joke())

    elif ("do you know" in query):
        ideas = open("data.txt", "r")
        output(f"You said me to remember these ideas:\n{ideas.read()}")

    elif ("idea" in query):
        idea()

    elif ("screenshot" in query):
        pyautogui.screenshot(str(ti.time()) + ".png").show()

    elif "cpu" in query:
        output(f"Cpu is at {str(psutil.cpu_percent())} percent")

    elif "offline" in query:
        hour = datetime.datetime.now().hour
        if (hour >= 21) and (hour < 6):
            output(f"Good Night {user}! Have a nice Sleep")
        else:
            output(f"Happy to serve you! Bye bye {user}. See you soon.")
        quit()