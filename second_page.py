from tkinter import *
from tkinter import messagebox
import tkinter.font as font

def sec_page():

    sec_root = Tk()

    def fun_height():
        height_status = messagebox.askquestion("Confirm","Click YES and please stand straight for 2-5 seconds")
        if height_status == "YES":
            return(150)

    def fun_temp():
        temp_status = messagebox.askquestion("Confirm","Click YES and place your finger on the tip of temperature sensor ")
        if temp_status == "YES":
            return(150)

    def fun_heart():
        heart_status = messagebox.askquestion("Confirm","Click YES and place your thumb on heart rate sensor")
        if  heart_status == "YES":
            return(150)

    #root.attributes('-fullscreen',True)
    sec_root.configure(background = "grey")
    gap_size = font.Font(size = 13,weight = 'bold')
    heading = font.Font(size = 60,weight = 'bold')
    heading1 = font.Font(size = 30,weight = 'bold')
    entry = font.Font(size = 25)
    entryfontname = ('verdana',15)
    entryfontage = ('verdana',16)

    top = Frame(sec_root)
    top.pack()
    top2 = Frame(sec_root)
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

    labelheight = Label(text='Click proceed if you want to check you height',bg = "grey")
    labelheight['font'] = entry
    labelheight.pack()

    #bmistatus = messagebox.askquestion("Please stand and Click YES and wait for 2 - 5 seconds")

    gap2 = Label(bg = 'grey')
    gap2['font'] = gap_size
    gap2.pack(fill = X)

    but_height = Button(sec_root,text = "Proceed",font = entryfontage,bg = "blue",command = fun_height)
    but_height.pack()

    gap3 = Label(bg = 'grey')
    gap3['font'] = gap_size
    gap3.pack(fill = X)

    labelweight = Label(text='Click proceed if you want to check you weight',bg = "grey")
    labelweight['font'] = entry
    labelweight.pack()

    gap4 = Label(bg = 'grey')
    gap4['font'] = gap_size
    gap4.pack(fill = X)

    but_weight = Button(sec_root,text = "Proceed",font = entryfontage,bg = "blue",command = fun_height)
    but_weight.pack()

    gap5 = Label(bg = 'grey')
    gap5['font'] = gap_size
    gap5.pack(fill = X)

    labeltemp = Label(text='Click proceed if you want to check you body temperature',bg = "grey")
    labeltemp['font'] = entry
    labeltemp.pack()

    gap6 = Label(bg = 'grey')
    gap6['font'] = gap_size
    gap6.pack(fill = X)

    but_temp = Button(sec_root,text = "Proceed",font = entryfontage,bg = "blue",command = fun_temp)
    but_temp.pack()

    gap7 = Label(bg = 'grey')
    gap7['font'] = gap_size
    gap7.pack(fill = X)

    labelheart = Label(text='Click proceed if you want to check your Heart rate and body temperatuere',bg = "grey")
    labelheart['font'] = entry
    labelheart.pack()

    gap8 = Label(bg = 'grey')
    gap8['font'] = gap_size
    gap8.pack(fill = X)

    but_heart = Button(sec_root,text = "Proceed",font = entryfontage,bg = "blue",command = fun_heart)
    but_heart.pack()

    gap9 = Label(bg = 'grey')
    gap9['font'] = gap_size
    gap9.pack(fill = X)

    but_results = Button(sec_root,text = "Proceed",font = entryfontage,bg = "blue",command = final_page)
    but_heart.pack()

    sec_root.mainloop()