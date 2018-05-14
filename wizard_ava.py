# -*- coding: utf-8 -*-
"""
Created on Thu May 10 15:27:24 2018

@author: Annie
"""

''' STILL NEED TO HAVE UPDATED COMMENTS/MORE COMMENDS '''
''' STILL NEEDS SOME CLEANING UP '''

import tkinter as tkr
import pyttsx3 as tts
import time
import sys
from playsound import playsound

sympa = False

root = tkr.Tk()

# set smpathetic language mode from command line input
try:
    if sys.argv[1] == "-s":
        sympa = True 
except(SyntaxError, IndexError):
    pass

directory = 'C:/Users/Annie/Documents/hri/finalProject/Text_to_Speech_files_F/'
extension = '.mp3'

''' functions for introduction and q1 '''

# small talk about time and introduction
def smallTalkAndIntro(event):
    playsound(directory + 'hello_F' + extension)
    
    localtime = time.localtime(time.time())
    hour = localtime[3]
    if hour < 12:
        playsound(directory + 'GoodMorning_F' + extension)
    elif hour > 18:
        playsound(directory + 'GoodAfternoon_F' + extension)
    else:
        playsound(directory + 'GoodEvening_F' + extension)
    
    if hour < 12 and hour > 6:
        playsound(directory + 'Nicetotalkfirstime_morning_F' + extension)
    elif hour < 12 and hour < 7:
        playsound(directory + 'Nicetotalk_allevening_F' + extension)
    elif hour > 18:
        playsound(directory + 'Nicetotalk_allday_F' + extension)
    else:
        playsound(directory + 'Nicetotalk_forawhile_F' + extension)
    
    playsound(directory + 'Quietaroundhere_F' + extension)
    
    if sympa == True:
        engine.say("I know you are probably busy this time of year with things, like exams, papers, life, the usual.")
    
# question 1
def howAreYou(event):
    playsound(directory +'Howhaveyoubeen_F' + extension)

# sympathetic phrasing 1
def howResponse(howentry):
    sympa1 = howentry.widget.get()

    playsound(directory + 'I_see_F' + extension)

    if sympa1 == "good":
        playsound(directory + 'Gladfeel_F' + extension)
    elif sympa1 == "bad":
        playsound(directory + 'Sorryfeel_F' + extension)
    elif sympa1 == "else":
        playsound(directory + 'Oneofthosedays_F' + extension)

# exchange 1 end
def conclusion1(event):
    if sympa == False:
        playsound(directory + 'I_see_F' + extension)
    playsound(directory + 'Ifeelgoodmyself_F' + extension)
  
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
    playsound(directory + 'Q1_tellmeaboutyourself_F' + extension)

def exchange2():
    
    ex2 = tkr.Label(bottomFrame, text="Exchange 2", bg="blue", fg="white", font=("", 16))
    
    tellme = tkr.Button(bottomFrame, text="Tell Me About", font=("", 14))
    tellme.bind("<Button-1>", tellMeAbout)
    
    ex2.grid(row=1, column=1)
    tellme.grid(row=2, column=1)

''' functions for q3 '''
# evaluate stress with verba likert scale
def evalStress(event):
    playsound(directory + 'Q2_stressfultime_F' + extension)
    playsound(directory + 'Q3_areyoustressednow_F' + extension)
    
# response to verbal likert scale
def respEvalStress(howentry):
    sympa2 = howentry.widget.get()

    if sympa2 == "1":
        playsound(directory + 'R1_greattohear_F' + extension)
    elif sympa2 == "2":
        playsound(directory + 'R2_gladyoudonthavemuchstress_F' + extension)
    elif sympa2 == "3":
        playsound(directory + 'R3_healthybalancebetween_F' + extension)
    elif sympa2 == "4":
        playsound(directory + 'R4_pretty_stressed_F' + extension)
    else:
        playsound(directory + 'R5_alotofstress_F' + extension)
    
def thankShare(event):
    
    playsound(directory + 'R6_thanksforsharingaboutyourstress_F' + extension)
    
def whyStress(howentry):
    currentStress = howentry.widget.get()

    if currentStress == "n" or currentStress == "N":
        playsound(directory + 'Q4_ifyoudontmind1_F' + extension)
    elif currentStress == "y" or currentStress == "Y":
        playsound(directory + 'Q4_ifyoudontmind2_F' + extension)
    
    
    
def thankLetMe(event):
    playsound(directory + 'R7_thanksforlettingmeknow_F' + extension)
    if sympa == True:
        playsound(directory + 'R8_hardtotalktostrangersaboutthese_F' + extension)
    
def binaryReduceStress(event):    
    playsound(directory + 'Q5_doinganythingtoreducethatstress_F' + extension)
    
def resolveStress(howentry):
    currentlyResolving = howentry.widget.get()
    
    if currentlyResolving == "y" or currentlyResolving == "Y":
        playsound(directory + 'Q6_Whatyoudoingnowtoreducethestress_F' + extension)
    elif currentlyResolving == "n" or currentlyResolving == "N":
        playsound(directory + 'Q7_Whatcouldyoudotoreducestress_F' + extension)

def appreciateTell(event):
    playsound(directory + 'Q8_Appreciatetellingmethis_F' + extension)
    
def final(howentry):
    playsound(directory + 'R9_Thankingagainfortakingthetime_F' + extension)
    stressLvl = howentry.widget.get()
    
    if stressLvl == "3" or stressLvl == "4" or stressLvl == "5":
        playsound(directory + 'R10_Hopeyouarelittlelessstressednow_F' + extension)
    elif stressLvl == "1" or stressLvl == "1":
        playsound(directory + 'R11_Hopeyoucontinuenotbestressed_F' + extension)
    
    localtime = time.localtime(time.time())
    hour = localtime[3]
    if hour < 12:
        playsound(directory + 'R12_Haveagoodmorning_F' + extension)
    elif hour > 18:
        playsound(directory + 'R13_Haveagoodevening_F' + extension)
    else:
        playsound(directory + 'R14_Haveagoodafternoon_F' + extension)
        
    playsound(directory + 'R15_Goodbye_F' + extension)

    
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
    playsound(directory + 'R16_Thankyou_F' + extension)
    
def abort(event):
    playsound(directory + 'R17_Notsurehowtoanswer_F' + extension)

def welcome(event):
    playsound(directory + 'R18_Youarewelcome_F' + extension)
    
def followUp(event):
    global count
    if count != 4:
        count = count + 1
    else:
        count = 0
    if count == 0:
        playsound(directory + 'R19_Pleasetellmemore_F' + extension)
    elif count == 1:
        playsound(directory + 'R20_SoundsinterestingLiketohearmore_F' + extension)
    elif count == 2:
        playsound(directory + 'Q9_Andthen_F' + extension)
    elif count == 3:
        playsound(directory + 'Q10_Couldyouexpandonthat_F' + extension)
    elif count == 4:
        playsound(directory + 'Q11_FascninatingTellmemore_F' + extension)

def letMeThink(event):
    global count1
    if count1 != 2:
        count1 = count1 + 1
    else:
        count1 = 0
    if count1 == 0:
        playsound(directory + 'R21_Letmethinkaboutthat_F' + extension)
    elif count1 == 1:
        playsound(directory + 'R22_Letmesee_Holdonasec_F' + extension)
    
def wildCardButtons():
    wild = tkr.Label(bottomFrame, text="Wild Cards", bg="magenta", fg="white", font=("", 16))
    thankyou = tkr.Button(bottomFrame, text="Generic Thank You", font=("", 14))
    idk = tkr.Button(bottomFrame, text="Don't know answer", font=("", 14))
    yourewelcome = tkr.Button(bottomFrame, text="Generic You're Welcome", font=("", 14))
    follow = tkr.Button(bottomFrame, text="Follow Up Quips", font=("", 14))
    think = tkr.Button(bottomFrame, text="Let Me Think", font=("", 14))
    
    thankyou.bind("<Button-1>", thankYou)
    idk.bind("<Button-1>", abort)
    yourewelcome.bind("<Button-1>", welcome)
    follow.bind("<Button-1>", followUp)
    think.bind("<Button-1>", letMeThink)
    
    wild.grid(row=1, column=3)
    thankyou.grid(row=2, column=3)
    idk.grid(row=3, column=3)
    yourewelcome.grid(row=4, column=3)
    follow.grid(row=5, column=3)
    think.grid(row=6, column=3)
    
''' GUI set up '''
if __name__ == "__main__":
    topFrame = tkr.Frame(root)
    topFrame.pack()
    bottomFrame = tkr.Frame(root)
    bottomFrame.pack(side="bottom")
    
    # set up main heading label
    titlelabel = tkr.Label(topFrame, text="Taylor Wizard of Oz Command Controls", bg="black", fg="white", font=("", 20))
    titlelabel.grid(row=0)
    count = 0
    count1 = 0
    exchange1()
    exchange2()
    exchange3()
    wildCardButtons()
    
    root.mainloop()