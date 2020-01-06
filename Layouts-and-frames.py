from tkinter import *
from tkinter import messagebox
import tkinter.font as font


root = Tk()
root.configure(background = "grey")

def start():
    name = entry_name.get()
    age = entry_age.get()
    entry_name.delete(0,END)
    entry_age.delete(0,END)

    bmistatus = messagebox.askquestion('BMI','Do you want to check your BMI?')
    if(bmistatus == 'yes'):
        bmicalculator()

    bmistatus = messagebox.askquestion('BMI', 'Do you want to check your BMI?')


heading = font.Font(size = 60,weight = 'bold')
entry = font.Font(size = 25)
entryfontname = ('verdana',15)
entryfontage = ('verdana',8)

top = Frame(root)
top.pack()

gap = Label(top,bg = 'grey')
gap.pack(fill = X)

head1 = Label(top,text = "Health",fg = "red",bg = 'grey')
head1['font'] = heading
head1.pack(side = LEFT)

head2 = Label(top,text = "Kiosk",fg = "black",bg = 'grey')
head2['font'] = heading
head2.pack()


gap1 = Label(bg = 'grey')
gap1.pack(fill = X)
gap2 = Label(bg = 'grey')
gap2.pack(fill = X)


labelname = Label(text = "Enter your Name",bg = "grey")
labelname['font'] = entry
labelname.pack()

gap3 = Label(bg = 'grey')
gap3.pack(fill = X)


entry_name = Entry(root,font = entryfontname)
entry_name.pack()

gap4 = Label(bg = 'grey')
gap4.pack(fill = X)
gap5 = Label(bg = 'grey')
gap5.pack(fill = X)


labelage = Label(text = "Enter your Age",bg = "grey")
labelage['font'] = entry
labelage.pack()

gap6 = Label(bg = 'grey')
gap6.pack(fill = X)


entry_age = Entry(root,font = entryfontage)
entry_age.pack(ipady = 8)

gap7 = Label(bg = 'grey')
gap7.pack(fill = X)

but = Button(root,text = "next",font = entry_age,bg = "blue",command = start)
but.pack()

root.mainloop()