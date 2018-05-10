# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:27:24 2018

@author: Annie
"""

import tkinter as tkr
import pyttsx3 as tts
import time

# set up text to speech
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

root = tkr.Tk()

''' introduction and first dialogue '''

# small talk about time and introduction
def smallTalkAndIntro(event):
    
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
        engine.say("for a while")
    engine.say("It gets pretty quiet around here.")
    engine.say("Allow me to introduce myself, my name is L2U2.")
    engine.say("Thank you for taking the time to meet with me today.")
    engine.runAndWait()

# question 1
def howAreYou(event):
    engine.say("How have you been? Good? Bad? Between good and bad?")
    engine.runAndWait()

def howResponse(howentry):
    resp = howentry.widget.get()
    print(resp)
'''    
    if listen1 == "good":
        engine.say("I'm glad you feel that way.")
    elif listen1 == "bad":
        engine.say("I'm sorry you feel that way.")
    else:
        engine.say("Ah, it's one of those days. I hope your day gets better.")
        '''
    
    
''' creating GUI '''

introlabel = tkr.Label(root, text="Introduction", bg="black", fg="white", font=("", 20))

smalltalkintro =tkr.Button(root, text="Small Talk and Intro", font=("", 14))
smalltalkintro.bind("<Button-1>", smallTalkAndIntro)

howareyou = tkr.Button(root, text="How are you?", font=("", 14))
howareyou.bind("<Button-1>", howAreYou)

howlabel = tkr.Label(root, text="Good/Bad/Else", bg="gray", fg="white", font=("", 14))
howentry = tkr.Entry(root)
howentry.bind("<Return>", howResponse)

introlabel.grid(row=0)
smalltalkintro.grid(row=1)
howareyou.grid(row=2)
howlabel.grid(row=3)
howentry.grid(row=3, column=1)

root.mainloop()