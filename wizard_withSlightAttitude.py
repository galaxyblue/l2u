# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:27:24 2018

@author: Annie
"""

import tkinter as tkr
import pyttsx3 as tts
import time
import sys

sympa = False

root = tkr.Tk()

# set smpathetic language mode from command line input
try:
    if sys.argv[1] == "-s":
        sympa = True 
except(SyntaxError, IndexError):
    pass

# set up text to speech
engine = tts.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

''' functions for introduction and q1 '''

# small talk about time and introduction
def smallTalkAndIntro(event):
    engine.say("Oh hello. I see you're going to talk to me.")
    
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
    engine.say("Especially because I can't access my microphone because, you know, I'm turned off.")
    engine.say("But anyways.")
    engine.say("Allow me to introduce myself, my name is L2U2.")
    engine.say("Thank you for taking the time to talk to me today.")
    
    if sympa == True:
        engine.say("I know you are probably busy this time of year with things, like exams, papers, life, the usual.")
    
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
        engine.say("I'm glad you feel that way. I love days that are going well.")
    elif sympa1 == "bad":
        engine.say("I'm sorry you feel that way. I hope your day improves later.")
        #engine.say("I could give you a cupcake, but it would be made of ones and zeros, which you unfortunately cannot eat.")
    else:
        engine.say("It's one of those days. I hope your day gets better.")
    
    engine.runAndWait()

# exchange 1 end
def conclusion1(event):
    if sympa == False:
        engine.say("I see.")
    engine.say("I feel pretty good myself. I get to talk to you today, which is more interesting what I normally do.")
    engine.say("Which is nothing, but I'm not complaining. Too much.")
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
    engine.say("Especially since you've decided to talk to me.")
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
    engine.say("Would you say you were stressed right now?")
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
    
    engine.say("Thank you for sharing with me about your stress.")
    engine.runAndWait()
    
def whyStress(howentry):
    currentStress = howentry.widget.get()

    if currentStress == "n" or currentStress == "N":
        engine.say("If you don't mind...")
        engine.say("Could you tell me about a time when you were very stressed and why that was the case?")
    elif currentStress == "y" or currentStress == "Y":
        engine.say("If you don't mind...")
        engine.say("Could you tell me why you are so stressed?")
    
    engine.runAndWait()
    
    
def thankLetMe(event):
    engine.say("Thank you for letting me know about that.")
    if sympa == True:
        engine.say("I know it can be hard to talk to a stranger about these things.")
    engine.runAndWait()
    
def binaryReduceStress(event):    
    engine.say("Are you doing anything right now to reduce that stress?")
    engine.runAndWait()
    
def resolveStress(howentry):
    currentlyResolving = howentry.widget.get()
    
    if currentlyResolving == "y" or currentlyResolving == "Y":
        engine.say("What are you doing right now to reduce your stress?")
    elif currentlyResolving == "n" or currentlyResolving == "N":
        engine.say("What do you think you could do right now to reduce your stress?")
    
    engine.runAndWait()

def appreciateTell(event):
    engine.say("I appreciate you telling me that. It was very interesting to hear.")
    engine.runAndWait()
    
def final(howentry):
    engine.say("I said this before, but thank you for taking the time to talk to me today.")
    stressLvl = howentry.widget.get()
    
    if stressLvl == "3" or stressLvl == "4" or stressLvl == "5":
        engine.say("I hope you're a little less stressed now.")
    elif stressLvl == "1" or stressLvl == "1":
        engine.say("I hope you continue to not be stressed.")
    
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

    
def exchange3():
    
    ex3 = tkr.Label(bottomFrame, text="Exchange 3", bg="blue", fg="white", font=("", 16))
    
    evalstress = tkr.Button(bottomFrame, text="Are You Stressed?", bg="green", fg="white", font=("", 14))
    evalstress.bind("<Button-1>", evalStress)
    
    if sympa == True:
        respevalstress = tkr.Label(bottomFrame, text="S2: Response to \"Are You Stressed?\" [1-5]", bg="gray", fg="white", font=("", 14))
        respevalentry = tkr.Entry(bottomFrame)
        respevalentry.bind("<Return>", respEvalStress)
    
    thankshare = tkr.Button(bottomFrame, text="Thank for Sharing About Stress", font=("", 14))
    thankshare.bind("<Button-1>", thankShare)
    
    whylabel = tkr.Label(bottomFrame, text="Why Are/Were You Stressed [currently stressed y/n]", bg="green", fg="white", font=("", 14))
    whyentry = tkr.Entry(bottomFrame)
    whyentry.bind("<Return>", whyStress)
    
    if sympa == True:
        thankletme = tkr.Button(bottomFrame, text="S3: Thank you for LMK", bg="gray", fg="white", font=("", 14))
    else:
        thankletme = tkr.Button(bottomFrame, text="Thank you for LMK", font=("", 14))
    
    thankletme.bind("<Button-1>", thankLetMe)
        
    currentstress = tkr.Button(bottomFrame, text="Doing anything RN to Reduce Stress?", font=("", 14))
    currentstress.bind("<Button-1>", binaryReduceStress)
    
    resolvestresslabel = tkr.Label(bottomFrame, text="What are/could you do? [doing something RN? y/n]", font=("", 14))
    resolvestressentry = tkr.Entry(bottomFrame)
    resolvestressentry.bind("<Return>", resolveStress)
    
    appreciate = tkr.Button(bottomFrame, text="Appreciate Tell", font=("", 14))
    appreciate.bind("<Button-1>", appreciateTell)
    
    finlabel = tkr.Label(bottomFrame, text="Closing [percevied stress level 1-5]", font=("", 14))
    finentry = tkr.Entry(bottomFrame)
    finentry.bind("<Return>", final)
    
    ex3.grid(row=1, column=2)
    evalstress.grid(row=2, column=2)
    if sympa == True:
        respevalstress.grid(row=3, column=2)
        respevalentry.grid(row=4, column=2)
    thankshare.grid(row=5, column=2)
    whylabel.grid(row=6, column=2)
    whyentry.grid(row=7, column=2)
    thankletme.grid(row=9, column=2)
    currentstress.grid(row=10, column=2)
    resolvestresslabel.grid(row=12, column=2)
    resolvestressentry.grid(row=13, column=2)
    appreciate.grid(row=14, column=2)
    finlabel.grid(row=15, column=2)
    finentry.grid(row=16, column=2)
    

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
    global count
    if count != 4:
        count = count + 1
    else:
        count = 0
    engine.runAndWait()
    if count == 0:
        engine.say("Please tell me more.")
    elif count == 1:
        engine.say("That sounds interesting. I'd like to hear more.")
    elif count == 2:
        engine.say("And then?")
    elif count == 3:
        engine.say("Could you expand on that?")
    elif count == 4:
        engine.say("Fascinating. Tell me more?")
        
    engine.runAndWait()

def randomDialogue(howentry):
    random = howentry.widget.get()
    engine.say(random)
    engine.runAndWait()

def letMeThink(event):
    global count1
    if count1 != 2:
        count1 = count1 + 1
    else:
        count1 = 0
    if count1 == 0:
        engine.say("Let me think about that for a moment.")
    elif count1 == 1:
        engine.say("Let me see... Hold on a second.")
    engine.runAndWait()
    
def wildCardButtons():
    wild = tkr.Label(bottomFrame, text="Wild Cards", bg="magenta", fg="white", font=("", 16))
    thankyou = tkr.Button(bottomFrame, text="Generic Thank You", font=("", 14))
    idk = tkr.Button(bottomFrame, text="Don't know answer", font=("", 14))
    yourewelcome = tkr.Button(bottomFrame, text="Generic You're Welcome", font=("", 14))
    follow = tkr.Button(bottomFrame, text="Follow Up Quips", font=("", 14))
    emerlabel = tkr.Label(bottomFrame, text="For Random Speech-to-Text", bg="red", fg="white", font=("", 14))
    emerentry = tkr.Entry(bottomFrame)
    think = tkr.Button(bottomFrame, text="Let Me Think", font=("", 14))
    
    thankyou.bind("<Button-1>", thankYou)
    idk.bind("<Button-1>", abort)
    yourewelcome.bind("<Button-1>", welcome)
    follow.bind("<Button-1>", followUp)
    emerentry.bind("<Return>", randomDialogue)
    think.bind("<Button-1>", letMeThink)
    
    wild.grid(row=1, column=3)
    thankyou.grid(row=2, column=3)
    idk.grid(row=3, column=3)
    yourewelcome.grid(row=4, column=3)
    follow.grid(row=5, column=3)
    think.grid(row=6, column=3)
    emerlabel.grid(row=7, column=3)
    emerentry.grid(row=8, column=3)


    
''' GUI set up '''

topFrame = tkr.Frame(root)
topFrame.pack()
bottomFrame = tkr.Frame(root)
bottomFrame.pack(side="bottom")

# set up main heading label
titlelabel = tkr.Label(topFrame, text="L2U2 Wizard of Oz Command Controls", bg="black", fg="white", font=("", 20))
titlelabel.grid(row=0)
count = 0
count1 = 0
exchange1()
exchange2()
exchange3()
wildCardButtons()

''' don't forget tell me more questions '''

root.mainloop()