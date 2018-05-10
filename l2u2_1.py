# -*- coding: utf-8 -*-
"""
Created on Wed May 09 22:53:49 2018

@author: Annie
"""

'''
set up detection of "how have you been" kind of phrasing
'''
# answer 1 keyword dictionaries
goodDict = ["good", "gut", "gud"]
badDict = ["bad", "dad", "dab", "bud", "bed"]
sosoDict = ["so", "soe", "sew"]

import speech_recognition as sr
import pyttsx3 as tts
import time
import sys

sympa = False;

if sys.argv[1] == "-s":
    sympa = True 

# set up text to speech
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# functions

def interact1():
    listen1 = answer1()
    engine.say("I see.")
    if sympa == True:
        sympaRespond1(listen1)
    engine.say("I feel pretty good. I get to talk to you today.")
    print(listen1)

# answer 1 - gets string of spoken phrase
def answer1():
    verify = False
    listen1 = ""
    while verify == False:
        # obtain audio from microphone
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Say something!")
            audio = r.listen(source)
        try:
            listen1 = r.recognize_sphinx(audio)
        except sr.UnknownValueError:
            engine.say("I'm sorry, could you say that again? Good, bad, or so so?")
            engine.runAndWait()
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))
        if listen1 != "":
            print(listen1)
            ver = verify1(listen1)
            if ver != None:
                return ver
            else:
                engine.say("Could you repeat that please? My sensors didn't quite pick that up.")
                engine.runAndWait()
        
        print(verify)
        print(listen1)

# checks if the string detected in answer1 has the correct keywords
def verify1(listen1):
    for gphrase in goodDict:
        if gphrase in listen1:
            return "good"
    for bphrase in badDict:
        if bphrase in listen1:
            return "bad"
    for sphrase in sosoDict:
        if sphrase in listen1:
            return "soso"
    return None

def sympaRespond1(listen1):
    if listen1 == "good":
        engine.say("I'm glad you feel that way.")
    elif listen1 == "bad":
        engine.say("I'm sorry you feel that way.")
    else:
        engine.say("Ah, it's one of those days. I hope your day gets better.")
        
        

# initiate small talk about time
localtime = time.localtime(time.time())
hour = localtime[3]
if hour < 12:
    engine.say("Good morning.")
elif hour > 18:
    engine.say("Good evening.")
else:
    engine.say("Good afternoon.")
    
engine.say("It's nice to see you. I've been turned off")
if hour < 12 and hour > 6:
    engine.say("all morning")
elif hour < 12 and hour < 7:
    engine.say("all evening")
elif hour > 18:
    engine.say("all day")
else:
    engine.say("a while")
engine.say("It gets quite lonely.")


engine.say("Allow me to introduce myself. My name is L2U2.")
engine.runAndWait()
engine.say("Thank you for taking the time to meet with me today.")

# sympathetic phrase 1
if sympa == True:
    engine.say("I know you are probably busy this time of year.")
    engine.runAndWait()

# question 1
engine.say("How have you been? Good? Bad? So so")
engine.runAndWait()

# verify recognition of correct keywords
listen1 = answer1()
engine.say("I see.")

# first sympathetic phrase - follow up to first question
if sympa == True:
    sympaRespond1(listen1)
engine.say("I feel pretty good. I get to talk to you today.")
engine.runAndWait()
print(listen1)
'''

# question 2
engine.say("Alright, please tell me about yourself. I would like to get to know you better.")
engine.runAndWait()
'''


