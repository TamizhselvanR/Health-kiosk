from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from chatterbot import ChatBot
import pyttsx3

faq_root = Tk()
faq_root.geometry("400x600")
faq_root.configure(background="grey")
faq_root.title('Chatbot')

gap = Label(faq_root, bg='green')
gap.config(font=(5))
gap.pack(fill=X)


faq_root.mainloop()
