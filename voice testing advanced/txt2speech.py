from tkinter import *
from gtts import gTTS
from playground import playsound

##########Initialize Window##########
root = Tk()
root.title("Deberryz - TEXT_2_SPEECH")
root.geometry("350x300")

##heading
root.configure(bg='ghost white')
root.title("Deberryz - TEXT TO SPEECH")
##
Label (root, text = "TEXT_TO_SPEECH", font = "arial 20 bold, bg= ('whitesmoke').pack()

##text variable
Msg = StringVar()
Label(root,text ="Enter Text", font = 'arial 15 bold' , bg (='whitesmoke').place(x=20,y=60)

#Entry
entry_field = Entry(root, textvariable = Msg, width ='50')
entry_field.place(x=20 ,y=100)


def Text_2_Speech():
    Message = entry_field.get()
    speech = gTTS('Deberryz.mp3'), lang = 'en', slow=False
    playsound('Deberryz.mp3')

def Exit():
    root.destroy()

def Reset():
    Msg.set("")
