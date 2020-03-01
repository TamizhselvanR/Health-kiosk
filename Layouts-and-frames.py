from tkinter import *
from tkinter import messagebox
import tkinter.font as font
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer,ChatterBotCorpusTrainer
import os
import pyttsx3


root = Tk()
root.state('zoomed')
root.configure(background = "grey")

def start():

    ever_married = m_status.get()
    work_type = w_status.get()
    gender = g_status.get()
    name = entry_name.get()
    age = entry_age.get()
    entry_name.delete(0,END)
    entry_age.delete(0,END)
    bmistatus = messagebox.askquestion("Confirm", 'Do you want to check your heart beat?')

    if bmistatus == "yes":

        gap8 = Label(bg='grey')
        gap8.pack(fill=X)

        head3 = Label(top2, text="Put your fingers on the chip to check your heartbeat", fg="black", bg='grey')
        head3['font'] = heading1
        head3.grid()

def faqstart():

    msg = []

    faq = Tk()
    faq.geometry("500x750")
    faq.configure(background="white")



    faq.mainloop()
    engine = pyttsx3.init()
    bot = ChatBot('bot',
              logic_adapters = [
                  {
                      'import_path':'chatterbot.logic.BestMatch',
                      'default_response':'I am sorry..But I Do not understand.',
                      'maximum_similarity_threshold':0.80
                  }
              ]
              )
    while True:
        message = input("You:")
        if message.strip() == 'Bye':
            print("Bot:See you later buddy")
        else:
            reply = bot.get_response(message)
            print("Bot:",reply)
            engine.say(reply)
            engine.runAndWait()


gap_size = font.Font(size = 1,weight = 'bold')
heading = font.Font(size = 60,weight = 'bold')
heading1 = font.Font(size = 30,weight = 'bold')
entry = font.Font(size = 25)
entryfontname = ('verdana',15)
entryfontage = ('verdana',8)

top = Frame(root)
top.pack()
top2 = Frame(root)
top2.pack()

gap = Label(top,bg = 'grey')
gap['font'] = gap_size
gap.pack(fill = X)

head1 = Label(top,text = "Health",fg = "red",bg = 'grey')
head1['font'] = heading
head1.pack(side = LEFT)

head2 = Label(top,text = "Kiosk",fg = "black",bg = 'grey')
head2['font'] = heading
head2.pack()

gap1 = Label(bg = 'grey')
gap1['font'] = gap_size
gap1.pack(fill = X)

labelname = Label(text='Enter your name',bg = "grey")
labelname['font'] = entry
labelname.pack()

gap2 = Label(bg = 'grey')
gap2['font'] = gap_size
gap2.pack(fill = X)

entry_name = Entry(root,font = entryfontname)
entry_name.pack()

gap3 = Label(bg = 'grey')
gap3['font'] = gap_size
gap3.pack(fill = X)

gap4 = Label(bg = 'grey')
gap4['font'] = gap_size
gap4.pack(fill = X)

labelage = Label(text = "Enter your Age",bg = "grey")
labelage['font'] = entry
labelage.pack()

gap5 = Label(bg = 'grey')
gap5['font'] = gap_size
gap5.pack(fill = X)


entry_age = Entry(root,font = entryfontage)
entry_age.pack(ipady = 8)

gap6 = Label(bg = 'grey')
gap6['font'] = gap_size

gap6.pack(fill = X)


labelgender = Label(text = "Select your Gender",bg = "grey")
labelgender['font'] = entry
labelgender.pack()


gap7 = Label(bg = 'grey')
gap7['font'] = gap_size

gap7.pack(fill = X)


g_status = StringVar(root)
g_status.set("Male") # default value
g = OptionMenu(root,g_status,"Male","Female","Rather not say")
g.pack(ipady = 1)

gap8 = Label(bg = 'grey')
gap8['font'] = gap_size
gap8.pack(fill = X)

labelmaritalstatus = Label(text = "Select your Marital status",bg = "grey")
labelmaritalstatus['font'] = entry
labelmaritalstatus.pack()


gap9 = Label(bg = 'grey')
gap9['font'] = gap_size
gap9.pack(fill = X)


m_status = StringVar(root)
m_status.set("No") # default value
w = OptionMenu(root,m_status,"Yes","No")
w.pack(ipady = 1)


gap10 = Label(bg = 'grey')
gap10['font'] = gap_size
gap10.pack(fill = X)


labelworkingstatus = Label(text = "Select your professional status",bg = "grey")
labelworkingstatus['font'] = entry
labelworkingstatus.pack()


gap11 = Label(bg = 'grey')
gap11['font'] = gap_size
gap11.pack(fill = X)


w_status = StringVar(root)
w_status.set("Never_worked") # default value
w_down = OptionMenu(root,w_status,"children","Private",'Self-employed','Govt_job')
w_down.pack(ipady = 1)


gap12 = Label(bg = 'grey')
gap12['font'] = gap_size
gap12.pack(fill = X)


labelarea = Label(text = "Living Area",bg = "grey")
labelarea['font'] = entry
labelarea.pack()


gap13 = Label(bg = 'grey')
gap13['font'] = gap_size
gap13.pack(fill = X)


living_status = StringVar(root)
living_status.set("Rural") # default value
l_down = OptionMenu(root,living_status,"Rural","Urban")
l_down.pack(ipady = 1)


gap14 = Label(bg = 'grey')
gap14['font'] = gap_size
gap14.pack(fill = X)


gap15 = Label(bg = 'grey')
gap15['font'] = gap_size
gap15.pack(fill = X)

but = Button(root,text = "next",font = entry_age,bg = "blue",command = start)
but.pack()


gap16 = Label(bg = 'grey')
gap16['font'] = gap_size
gap16.pack(fill = X)

gap17 = Label(bg = 'grey')
gap17['font'] = gap_size
gap17.pack(fill = X)


but = Button(root,text = "FAQ",font = entry_age,bg = "blue",command = faqstart)
but.pack()


root.mainloop()