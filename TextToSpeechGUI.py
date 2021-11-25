from tkinter import *
from tkinter import messagebox
import pyttsx3

root=Tk()
root.config(bg="black")
root.title("Text To Speech Convertor")
root.geometry("400x200")
root.resizable(False,False)

def speech():
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[1].id)
    engine.setProperty('rate', 150)
    engine.say(txtent.get())
    engine.runAndWait()
    txtent.delete(0,END)

#ABOUT FUNCTION
def info():
    messagebox.showinfo("About",f"This project was made by Sabir Khan\n His social handles\nInstagram-@the_sigma_programmer\nFacebook-Sabir Khan\nTwitter-@sabir_khan58\nTelegram-@INFINIXEL")

#MENU WIDGET
menubar= Menu(root)
menubar.add_cascade(label="About",command=info)
root.config(menu=menubar)

txtlbl=Label(root,text="Enter Text\n Below :", font=("comicsans", 15, "bold"), bg="black", fg="#00FF00").pack(pady=10)
txtent=Entry(root,font=("comicsans", 18, "bold"), bg="black", fg="#00FF00")
txtent.pack(pady=15)
b1=Button(text="Convert", font=("comicsans", 13, "bold"),  relief=GROOVE, command=speech, bg="black", fg="#00FF00", borderwidth=1).pack(pady=10)

root.mainloop()