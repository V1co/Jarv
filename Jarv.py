__version__ = '1.0.0'
__author__ = 'Rafal Pawlowski'

import speech_recognition
import os
import time
import sys
import webbrowser
from datetime import datetime
import pyttsx3

# pyttsx3 initialization and settings

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-30)


def welcome_message():
    engine.say('Hello, I am Jarv, how may I help?')
    engine.runAndWait()


# Jarv recognizing voice

def read_from_microphone():
    recognise_speech = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        print("Say some command, I am listening")
        audio = recognise_speech.listen(source)
    try:
        text = recognise_speech.recognize_google(audio, language='en')
        print("You said: {}".format(text))
        return text
    except BaseException:
        text = "I am waiting for a command"
        return text


# Jarv's speech via pyttsx3

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# Jarv's responsive commands

def turn_off():
    speak('I am turning off, good bye')
    quit()


def open_notepad():
    speak('I am opening Notepad')
    os.system('start notepad')
    return


def open_browser():
    speak('I am opening browser')
    os.system('start https://www.google.com/')
    return


def open_instagram():
    speak('I am opening Instagram')
    os.system('start https://instagram.com')
    return


def open_spotify():
    speak('I am opening Spotify')
    os.system('start https://open.spotify.com')
    return


def open_calculator():
    speak('I am opening calculator')
    os.system('start calc')
    return


def open_paint():
    speak('I am opening Paint')
    os.system('start mspaint')
    return


def find_in_google():
    speak('What do you want me to find?')
    sentence = str(read_from_microphone())
    if sentence == 'I am waiting for a command':
        speak('I have not recognised command')
        return
    else:
        webbrowser.open_new_tab(
            'http://www.google.com/search?btnG=1&q=' + sentence)
        return


def find_in_youtube():
    speak('What do you want me to find?')
    sentence = str(read_from_microphone())
    if sentence == 'I am waiting for a command':
        speak('I have not recognised command')
        return
    else:
        webbrowser.open_new_tab(
            'http://www.youtube.com/search?btnG=1&q=' + sentence)
        return


def awake():
    speak('I am awake')
    return


def what_date_is_it():
    current = datetime.now()
    date_string = current.strftime("%d/%m/%Y")
    print(date_string)
    speak(date_string)
    return


def what_day_is_it():
    current = datetime.now()
    day_string = current.strftime("%A")
    print(day_string)
    speak(day_string)
    return


def what_month_is_it():
    current = datetime.now()
    month_string = current.strftime("%B")
    print(month_string)
    speak(month_string)
    return


def what_time_is_it():
    current = datetime.now()
    time_string = current.strftime("%I:%M" + " " + "%p")
    print(time_string)
    speak(time_string)
    return


def weather():
    speak('In which city?')
    city = str(read_from_microphone())
    if city == 'I am waiting for a command':
        speak('I have not recognised command')
        return
    else:
        webbrowser.open_new_tab(
            'http://www.google.com/search?btnG=1&q=' +
            city +
            '+weather')
        return


def thank_you():
    speak('You are welcome')
    return


def how_are_you():
    speak('I am fine, thank you')
    return


# Jarv's command regotnition and initialization of responsive commands.
# Jarv is using text to recognise commands.


def recognise_command():

# Opening commands

    open_notepad_commands = ['open' and 'notepad' or 'turn' and 'notepad']
    for str in open_notepad_commands:
        if str in text:
            open_notepad()

    open_browser_commands = ['open' and 'browser' or 'turn' and 'browser']
    for str in open_browser_commands:
        if str in text:
            open_browser()

    open_instagram_commands = [
    'open' and 'instagram' or
    'turn' and 'instagram']
    for str in open_instagram_commands:
        if str in text:
            open_instagram()

    open_spotify_commands = ['open' and 'spotify' or 'turn' and 'spotify']
    for str in open_spotify_commands:
        if str in text:
            open_spotify()   

    open_calculator_commands = [
    'open' and 'calculator' or
    'turn' and 'calculator']
    for str in open_calculator_commands:
        if str in text:
            open_calculator()     

    open_paint_commands = ['open' and 'paint' or 'turn' and 'paint']
    for str in open_paint_commands:
        if str in text:
            open_paint()

# Searching commands

    find_in_google_commands = [
    'find' and 'google' or 
    'look' and 'google' or 
    'search' and 'google']
    for str in find_in_google_commands:
        if str in text:
            find_in_google()

    find_in_youtube_commands = [
    'find' and 'youtube' or 
    'look' and 'youtube' or 
    'search' and 'youtube']
    for str in find_in_youtube_commands:
        if str in text:
            find_in_youtube()

# Additional commands

    awake_commands = ['you' and 'awake']
    for str in awake_commands:
        if str in text:
            awake()

    what_date_is_it_commands = [
    'check' and 'date' or 
    'what' and 'date' or
    'which' and 'date'
    ]
    for str in what_date_is_it_commands:
        if str in text:
            what_date_is_it()

    what_day_is_it_commands = [
    'check' and 'day' or 
    'what' and 'day' or
    'which' and 'day'
    ]
    for str in what_day_is_it_commands:
        if str in text:
            what_day_is_it()

    what_month_is_it_commands = [
    'check' and 'month' or 
    'what' and 'month' or
    'which' and 'month'
    ]
    for str in what_month_is_it_commands:
        if str in text:
            what_month_is_it()

    what_time_is_it_commands = [
    'check' and 'time' or 
    'what' and 'time' or
    'which' and 'time'
    ]
    for str in what_time_is_it_commands:
        if str in text:
            what_time_is_it()

    check_weather_commands = ['check' and 'weather' or 'what' and 'weather']
    for str in check_weather_commands:
        if str in text:
            weather()

    thank_you_commands = ['thank you']
    for str in thank_you_commands:
        if str in text:
            thank_you()

    how_are_you_commands = ['how are you']
    for str in how_are_you_commands:
        if str in text:
            how_are_you()

    turn_off_commands = ['turn off']
    for str in turn_off_commands:
        if str in text:
            turn_off()

# Start of the program

if __name__ == '__main__':
    print('Welcome in Jarv 1.0.0')
    welcome_message()
    while (True):
        text = read_from_microphone().lower()
        recognise_command()