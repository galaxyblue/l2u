# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:27:24 2018

@author: Annie
"""

import tkinter as tkr
import pyttsx3 as tts
import time
import sys

# set up text to speech
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

root = tkr.Tk()

sympa = False;

try:
    if sys.argv[1] == "-s":
        sympa = True 
except(SyntaxError, IndexError):
    pass

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
    
    if sympa == True:
        engine.say("I know you are probably busy this time of year.")
    
    engine.runAndWait()

# question 1
def howAreYou(event):
    engine.say("How have you been? Good? Bad? Between good and bad?")
    engine.runAndWait()

def howResponse(howentry):
    sympa1 = howentry.widget.get()

    engine.say("I see.") 

    if sympa1 == "good":
        engine.say("I'm glad you feel that way.")
    elif sympa1 == "bad":
        engine.say("I'm sorry you feel that way. I hope your day improves later.")
    else:
        engine.say("Ah, it's one of those days. I hope your day gets better.")
    
    engine.runAndWait()

def conclusion1(event):
    if sympa == False:
        engine.say("I see.")
    engine.say("I feel pretty good myself. I get to talk to you today.")
    engine.runAndWait()
    
    
''' creating GUI '''
topFrame = tkr.Frame(root)
topFrame.pack()
bottomFrame = tkr.Frame(root)
bottomFrame.pack(side="bottom")

titlelabel = tkr.Label(topFrame, text="L2U2 Wizard of Oz Command Controls", bg="black", fg="white", font=("", 20))

introlabel = tkr.Label(bottomFrame, text="Exchange 1", bg="black", fg="white", font=("", 16))

smalltalkintro =tkr.Button(bottomFrame, text="Small Talk + Intro", font=("", 14))
smalltalkintro.bind("<Button-1>", smallTalkAndIntro)

howareyou = tkr.Button(bottomFrame, text="How are you?", font=("", 14))
howareyou.bind("<Button-1>", howAreYou)

if sympa == True:
    howlabel = tkr.Label(bottomFrame, text="S1: Input good/bad/else", bg="gray", fg="white", font=("", 14))
    howentry = tkr.Entry(bottomFrame)
    howentry.bind("<Return>", howResponse)

howareyou = tkr.Button(bottomFrame, text="How are you?", font=("", 14))
howareyou.bind("<Button-1>", howAreYou)

conclu1 = tkr.Button(bottomFrame, text="End 1", font=("", 14))
conclu1.bind("<Button-1>", conclusion1)

# put buttons on grid
titlelabel.grid(row=0)
introlabel.grid(row=1)
smalltalkintro.grid(row=2)
howareyou.grid(row=3)
if sympa == True:
    howlabel.grid(row=4)
    howentry.grid(row=4, column=1)
conclu1.grid(row=5)

root.mainloop()