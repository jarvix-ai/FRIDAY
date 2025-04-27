import speech_recognition as sr
import pyttsx3
import time
import datetime
import pyautogui
import subprocess

engine = pyttsx3.init()
voices = engine.getProperty('voices')

 # Change index to select different voice
engine.setProperty('rate', 160)  # Speed of speech
engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)
def speak(text):
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.6)

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening sir...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing sir...")
        command = recognizer.recognize_google(audio)
        command = command.lower()
        print("You said", command,"sir")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I didn't catch that sir.")
        return ""
    except sr.RequestError:
        speak("Sorry, the service is unavailable right now sir.")
        return ""
def greet_user():
    hour=datetime.datetime.now().hour
    if hour>=5 and hour<12:
        greet= ("Good Morning Sir!")
    elif hour>=12 and hour<17:
        greet= "Good Afternoon Sir!"
    elif hour>=17 and hour<21:
        greet= "Good Evening Sir!"
    else:
        greet= "Good Night Sir!"
    print(greet)
    speak(greet)
def control_brightness(command):
    if "increase brightness" in command:
        subprocess.run("xrandr --output eDp-1 --brightness 1.1", shell=True)
        speak("Increasing Brightness Sir...")
    elif "decrease brightness" in command:
        subprocess.run("xrandr --output eDP-1 --brightness 0.9", shell=True)
        speak("Decreasing Brightness Sir...")
def take_screenshot(command):
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    print("Screenshot taken sir.")
    speak("Screenshot taken sir.")
def control_volume(command):
    if "increase volume" in command:
        pyautogui.press("volumeup")
        speak("Increasing volume sir...")
    elif "decrease volume" in command:
        pyautogui.press("volumedown")
        speak("Decreasing volume sir...")
def run_assistant():
    greet_user()
    speak("Hello Sir, I'm FRIDAY. What do you want me to do sir...?")
    time.sleep(1)
    speak("I am at your service sir.")
    while True:
        command = listen()
        if "hello" in command.lower():
            speak("Hi sir!")
            time.sleep(2)
        elif "what is your name" in command.lower():
            print("My name is FRIDAY sir.")
            speak("My name is FRIDAY sir.")
        elif "open firefox" in command.lower():
            print("Opening Firefox sir...")
            speak("Opening Firefox sir...")
        elif "what is the time" in command.lower():
            print("The time is", time.strftime("%H %M %S"), "sir.")
            speak("The time is " + time.strftime("%H hour %M minutes %S seconds") + " sir.")
        elif "what is the date" in command.lower():
            print("Today's date is", time.strftime("%d-%m-%y"), "sir.")
            speak("Today's date is " + time.strftime("%d %m %y") + " sir.")
        elif "play music" in command.lower():
            print("Playing music sir...")
            speak("Playing music sir...")
        elif "increase volume" in command.lower() or "decrease volume" in command.lower():
            control_volume(command)
        elif "how are you" in command.lower():
            speak("I'm doing great sir, thanks for asking!")
        elif "increase brightness" in command.lower() or "decrease brightness" in command.lower():
            control_brightness(command)
        elif "take screenshot" in command.lower():
            take_screenshot(command)
        elif "exit" in command.lower():
            speak("Anytime at your service sir.")
            break
        else:
            speak("I'm not sure how to respond to that yet sir.")

run_assistant()
