# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:27:24 2018

@author: Annie
"""

import tkinter as tkr
import pyttsx3 as tts
import time
import sys
from random import randint

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

''' functions for introduction and q1 '''

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

# sympathetic phrasing 1
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

# exchange 1 end
def conclusion1(event):
    if sympa == False:
        engine.say("I see.")
    engine.say("I feel pretty good myself. I get to talk to you today.")
    engine.runAndWait()
  
# exchange 1 GUI
def exchange1():
    
    ex1 = tkr.Label(bottomFrame, text="Exchange 1", bg="blue", fg="white", font=("", 16))
    
    smalltalkintro =tkr.Button(bottomFrame, text="Small Talk + Intro", font=("", 14))
    smalltalkintro.bind("<Button-1>", smallTalkAndIntro)
    
    howareyou = tkr.Button(bottomFrame, text="How are you? (HRU)", font=("", 14))
    howareyou.bind("<Button-1>", howAreYou)
    
    if sympa == True:
        howlabel = tkr.Label(bottomFrame, text="S1: Response to HRU [good/bad/else]", bg="gray", fg="white", font=("", 14))
        howentry = tkr.Entry(bottomFrame)
        howentry.bind("<Return>", howResponse)
    
    conclu1 = tkr.Button(bottomFrame, text="End 1", font=("", 14))
    conclu1.bind("<Button-1>", conclusion1)
    
    # put buttons on grid
    ex1.grid(row=1)
    smalltalkintro.grid(row=2)
    howareyou.grid(row=3)
    if sympa == True:
        howlabel.grid(row=4)
        howentry.grid(row=5)
    conclu1.grid(row=6)

''' functions for q2 '''

# question 2
def tellMeAbout(event):
    engine.say("Please tell me about yourself. I want to get to know you better.")
    engine.runAndWait()

def exchange2():
    
    ex2 = tkr.Label(bottomFrame, text="Exchange 2", bg="blue", fg="white", font=("", 16))
    
    tellme = tkr.Button(bottomFrame, text="Tell Me About", font=("", 14))
    tellme.bind("<Button-1>", tellMeAbout)
    
    ex2.grid(row=1, column=1)
    tellme.grid(row=2, column=1)

''' functions for q3 '''
# evaluate stress with verba likert scale
def evalStress(event):
    engine.say("I hear this may be a stressful time for you.")
    engine.say("On a scale of 1-5, where 1 is not stressed and 5 is very stressed.")
    engine.say("How stressed would you say you are?")
    engine.runAndWait()
    
# response to verbal likert scale
def respEvalStress(howentry):
    sympa2 = howentry.widget.get()

    if sympa2 == "1":
        engine.say("That's great to hear. I'm glad you aren't that stressed.")
    elif sympa2 == "2":
        engine.say("That's good. I'm glad you don't have that much stress right now.")
    elif sympa2 == "3":
        engine.say("One might say that's a healthy balance between stressed and not stressed, haha.")
    elif sympa2 == "4":
        engine.say("That's pretty stressed. I'm sorry you feel that way.")
    else:
        engine.say("Oh dear, that is a lot of stress. I hope you are okay.")
    
    engine.runAndWait()
    
def thankShare(event):
    engine.say("Thank you for sharing that information.")
    engine.runAndWait()
    
def whyStress(howentry):
    stressLvl = howentry.widget.get()
    
    engine.say("If you don't mind...")
    if stressLvl == "1" or stressLvl == "2":
        engine.say("Could you tell me about a time when you were very stressed and why that was the case?")
    else:
        engine.say("Could you tell me why you are so stressed?")
    
    engine.runAndWait()

def reduceStress(howentry):
    stressLvl = howentry.widget.get()
    engine.say("Hhhhmmmmm... on a scale of 1-5, where 1 is not well at all and 5 is great,")
    
    if stressLvl == "1" or stressLvl == "2" or stressLvl == "3":
        engine.say("How did you handle that stress?")
    else:
        engine.say("How are you currently handling that stress?")
    
    engine.runAndWait()
    
def thankLetMe(event):
    engine.say("Thank you for letting me know about that.")
    if sympa == True:
        engine.say("I know it can be hard to talk to a stranger about these things.")
    engine.runAndWait()
    
def binaryReduceStress(howentry):
    stressLvl = howentry.widget.get()
    
    if stressLvl == "3" or stressLvl == "4" or stressLvl == "5":
        engine.say("Are you doing anything right now to reduce that stress?")
    
    engine.runAndWait()
    
def resolveStress(howentry):
    currentlyResolving = howentry.widget.get()
    
    if currentlyResolving == "y" or currentlyResolving == "Y":
        engine.say("What are you doing right now to reduce your stress?")
    elif currentlyResolving == "n" or currentlyResolving == "N":
        engine.say("What could you do right now to reduce your stress?")
    
    engine.runAndWait()

def appreciateTell(event):
    engine.say("I appreciate you telling me that. It was very interesting to hear.")
    engine.runAndWait()
    
def exchange3():
    
    ex3 = tkr.Label(bottomFrame, text="Exchange 3", bg="blue", fg="white", font=("", 16))
    
    evalstress = tkr.Button(bottomFrame, text="Evaluate Stress", bg="green", fg="white", font=("", 14))
    evalstress.bind("<Button-1>", evalStress)
    
    if sympa == True:
        respevalstress = tkr.Label(bottomFrame, text="S2: Response to Stress Lvl [1-5]", bg="gray", fg="white", font=("", 14))
        respevalentry = tkr.Entry(bottomFrame)
        respevalentry.bind("<Return>", respEvalStress)
    
    thankshare = tkr.Button(bottomFrame, text="Thank for Share", font=("", 14))
    thankshare.bind("<Button-1>", thankShare)
    
    whylabel = tkr.Label(bottomFrame, text="Why Stressed [1-5]", bg="green", fg="white", font=("", 14))
    whyentry = tkr.Entry(bottomFrame)
    whyentry.bind("<Return>", whyStress)
    
    howhandlestressscale = tkr.Button(bottomFrame, text="How Well Handle Stress", font=("", 14))
    howhandlestressscale.bind("<Button-1>", reduceStress)
    
    if sympa == True:
        thankletme = tkr.Button(bottomFrame, text="S3: Thank you for LMK", bg="gray", fg="white", font=("", 14))
    else:
        thankletme = tkr.Button(bottomFrame, text="Thank you for LMK", font=("", 14))
        
    currentstresslabel = tkr.Label(bottomFrame, text="Currently Decr. Stress? [y/n]", font=("", 14))
    currentstressentry = tkr.Entry(bottomFrame)
    currentstressentry.bind("<Return>", binaryReduceStress)
    
    resolvestresslabel = tkr.Label(bottomFrame, text="Resolving Stress? [y/n]", font=("", 14))
    resolvestressentry = tkr.Entry(bottomFrame)
    resolvestressentry.bind("<Return>", binaryReduceStress)
    
    appreciate = tkr.Button(bottomFrame, text="Appreciate Tell", font=("", 14))
    appreciate.bind("<Button-1>", appreciateTell)
    
    fin = tkr.Button(bottomFrame, text="Closing", font=("", 14))
    fin.bind("<Button-1>", final)
    
    ex3.grid(row=1, column=2)
    evalstress.grid(row=2, column=2)
    if sympa == True:
        respevalstress.grid(row=3, column=2)
        respevalentry.grid(row=4, column=2)
    thankshare.grid(row=5, column=2)
    whylabel.grid(row=6, column=2)
    whyentry.grid(row=7, column=2)
    howhandlestressscale.grid(row=8, column=2)
    thankletme.grid(row=9, column=2)
    currentstresslabel.grid(row=10, column=2)
    currentstressentry.grid(row=11, column=2)
    resolvestresslabel.grid(row=12, column=2)
    resolvestressentry.grid(row=13, column=2)
    appreciate.grid(row=14, column=2)
    fin.grid(row=15, column=2)
    
def final(howentry):
    engine.say("I said this before, but thank you for taking the time to talk to me today.")
    stressLvl = howentry.widget.get()
    
    if stressLvl == "3" or stressLvl == "4" or stressLvl == "5":
        engine.say("I hope you're a little less stressed now.")
    
    localtime = time.localtime(time.time())
    hour = localtime[3]
    if hour < 12:
        engine.say("Have a good morning.")
    elif hour > 18:
        engine.say("Have a good evening.")
    else:
        engine.say("Have a good afternoon.")
        
    engine.say("Goodbye.")
    
    engine.runAndWait()

def thankYou(event):
    engine.say("Thank you.")
    engine.runAndWait()
    
def abort(event):
    engine.say("I'm sorry, I'm not sure how to answer that.")
    engine.runAndWait()

def welcome(event):
    engine.say("You are welcome.")
    engine.runAndWait()

def followUp(event):
    numRand = randint(0,3)
    if numRand == 0:
        engine.say("Could you expand on that?")
    elif numRand == 1:
        engine.say("I'd like to hear more about that?")
    elif numRand == 2:
        engine.say("Please tell me more about that.")
    elif numRand == 3:
        engine.say("And then?")
    engine.runAndWait()
    
def wildCardButtons():
    wild = tkr.Label(bottomFrame, text="Wild Cards", bg="magenta", fg="white", font=("", 16))
    thankyou = tkr.Button(bottomFrame, text="Generic Thank You", font=("", 14))
    idk = tkr.Button(bottomFrame, text="Don't know answer", font=("", 14))
    yourewelcome = tkr.Button(bottomFrame, text="Generic You're Welcome", font=("", 14))
    follow = tkr.Button(bottomFrame, text="Follow Up Quips", font=("", 14))
    
    thankyou.bind("<Button-1>", thankYou)
    idk.bind("<Button-1>", abort)
    yourewelcome.bind("<Button-1>", welcome)
    follow.bind("<Button-1>", followUp)
    
    wild.grid(row=1, column=3)
    thankyou.grid(row=2, column=3)
    idk.grid(row=3, column=3)
    yourewelcome.grid(row=4, column=3)
    follow.grid(row=5, column=3)
    
    
# emergency buttons, i don't know, generic thank you, i'd like to hear more, you're welcome

    
''' GUI set up '''
topFrame = tkr.Frame(root)
topFrame.pack()
bottomFrame = tkr.Frame(root)
bottomFrame.pack(side="bottom")

# set up main heading label
titlelabel = tkr.Label(topFrame, text="L2U2 Wizard of Oz Command Controls", bg="black", fg="white", font=("", 20))
titlelabel.grid(row=0)

exchange1()
exchange2()
exchange3()
wildCardButtons()

''' don't forget tell me more questions '''

root.mainloop()