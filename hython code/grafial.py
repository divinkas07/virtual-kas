### grafical whit  tkinter

from tkinter import*
import webbrowser
def connect():
    webbrowser.open_new("https://chatgpt.com/")
window = Tk()
boite = Frame(window,background="#0076d1")
boite.pack(expand=YES)
window.geometry("1080x720")
window.minsize(600,400)
window.title("leaning the AI with hikas tech")
window.iconbitmap("hikas python/microsoftlogo_scale_100_Uus_icon.ico")
window.config(background="#0076d1")
text = Label(boite, text="HIKAS SCIENCE-DATA SCHOOL",font=("monospace",32),bg="#0076d1",fg="white")
text.pack()
subtext = Label(boite, text="introduction in AI with python",font=("lucida",20),bg="#0076d1",fg="white")
subtext.pack()
Boutton = Button(boite, text="started chatgpt",font=("monospace",16) ,bg="#011f5c",fg="white",command=connect)
Boutton.pack()

window.mainloop()