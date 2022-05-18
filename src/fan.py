#!/usr/bin/python3
import tkinter as tk
import subprocess
import threading
from tkinter import *
from time import sleep
from threading import Thread
from PIL import Image, ImageTk
import subprocess as sub


def set_speed(speed=None):
    """
    Set speed of fan by changing level at /proc/acpi/ibm/fan
    speed: 0-7, auto, disengaged, full-speed
    """
    return subprocess.check_output(
        'echo level {0} | sudo tee "/proc/acpi/ibm/fan"'.format(speed),
        shell=True
    ).decode()


def get_info():
    #gets sensor information
    info_lines = subprocess.check_output("sensors").decode("utf-8").split("\n")
    result = []
    count = 0
    for i in info_lines:
        if "Core" in i:
            result.append("Core %d: " % count + i.split(":")[-1].split("(")[0].strip())
            count += 1

        if "fan" in i:
            result.append("Fan : " + i.split(":")[-1].strip())
            count += 1
    return result
def get_level():
    #gets level information
    level_lines = subprocess.check_output(['less', '/proc/acpi/ibm/fan']).decode("utf-8").split("\n")
    levelresult = []
    count = 0
    for j in level_lines:
        if "level:" in j:
            levelresult.append("Level : " + j.split(":")[-1].strip())
            count += 1
    return levelresult

is_on = True

def close_win(e):
   root.destroy()

class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.minsize(width=100, height=100)
        Colour = StringVar()
        Colour.set('#000000')
        Colour2 = StringVar()
        Colour2.set('#FFFFFF')

        level_label = tk.Label(parent, text="", bg=Colour.get(), fg=Colour2.get())
        level_label.grid(row=1, column=0)

        main_label = tk.Label(parent, text="", bg=Colour.get(), fg=Colour2.get())
        main_label.grid(row=2, column=0)




        row1 = tk.Frame()
        row1.grid()

        button0 = tk.Button(row1, text="0", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("0"))
        button0.grid(row=0, column=0)

        button1 = tk.Button(row1, text="1", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("1"))
        button1.grid(row=0, column=1)

        button2 = tk.Button(row1, text="2", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("2"))
        button2.grid(row=0, column=2)

        button3 = tk.Button(row1, text="3", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("3"))
        button3.grid(row=0, column=3)

        button4 = tk.Button(row1, text="4", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("4"))
        button4.grid(row=0, column=4)

        button5 = tk.Button(row1, text="5", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("5"))
        button5.grid(row=0, column=5)

        button6 = tk.Button(row1, text="6", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("6"))
        button6.grid(row=0, column=6)

        button7 = tk.Button(row1, text="7", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("7"))
        button7.grid(row=0, column=7)

        row2 = tk.Frame()
        row2.grid()


        buttonA = tk.Button(row2, text="Auto", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("auto"))
        buttonA.grid(row=0, column=1)

        buttonF = tk.Button(row2, text="Full", highlightbackground="#6F7170", bg="#000000", fg="#FFFFFF", highlightcolor="#6F7170", highlightthickness=1, bd=0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("full-speed"))
        buttonF.grid(row=0, column=2)

        row3 = tk.Frame()
        row3.grid(sticky=E)

        def button_mode():
            global is_on

        #Determine it is on or off and theming
            if is_on:
                on_.config(image=off, borderwidth=0, bg="#FFFFFF",  activebackground="#FFFFFF")
                main_label.config(bg='white')
                level_label.config(bg='white')
                button0.config(bg='white')
                button1.config(bg='white')
                button2.config(bg='white')
                button3.config(bg='white')
                button4.config(bg='white')
                button5.config(bg='white')
                button6.config(bg='white')
                button7.config(bg='white')
                buttonA.config(bg='white')
                buttonF.config(bg='white')
                main_label.config(fg='black')
                level_label.config(fg='black')
                button0.config(fg='black')
                button1.config(fg='black')
                button2.config(fg='black')
                button3.config(fg='black')
                button4.config(fg='black')
                button5.config(fg='black')
                button6.config(fg='black')
                button7.config(fg='black')
                buttonA.config(fg='black')
                buttonF.config(fg='black')
                self.master.configure(background="white")
                is_on = False
            else:
                on_.config(image=on, borderwidth=0, bg="#000000", activebackground="#000000")
                main_label.config(bg='black')
                level_label.config(bg='black')
                button0.config(bg='black')
                button0.config(bg='black')
                button1.config(bg='black')
                button2.config(bg='black')
                button3.config(bg='black')
                button4.config(bg='black')
                button5.config(bg='black')
                button6.config(bg='black')
                button7.config(bg='black')
                buttonA.config(bg='black')
                buttonF.config(bg='black')
                main_label.config(fg='white')
                level_label.config(fg='white')
                button0.config(fg='white')
                button0.config(fg='white')
                button1.config(fg='white')
                button2.config(fg='white')
                button3.config(fg='white')
                button4.config(fg='white')
                button5.config(fg='white')
                button6.config(fg='white')
                button7.config(fg='white')
                buttonA.config(fg='white')
                buttonF.config(fg='white')
                self.master.configure(background="black")
                is_on = True

        on = PhotoImage(file="/opt/fancontrol/Resources/on.png")
        off = PhotoImage(file="/opt/fancontrol/Resources/off.png")

        on_ = Button(row3, image=on, bd=0, highlightthickness=0, borderwidth=0, bg=("#000000"), activebackground="#000000", command=button_mode)
        on_.pack()

        def display_loop():
            while True:
                sleep(0.5)
                main_label["text"] = "\n".join(get_info())
                level_label["text"] = "\n".join(get_level())



        thread = threading.Thread(target=display_loop)
        thread.daemon = True
        thread.start()



if __name__ == "__main__":

    root = tk.Tk(className='ThinkFan Control')
    root.bind('<Control-q>', lambda e: close_win(e))
    root.configure(background='black')
    img = tk.Image("photo", file='/opt/fancontrol/Resources/icon.png')
    root.protocol('WM_DELETE_WINDOW')
    root.resizable(False, False)
    root.tk.call('wm', 'iconphoto', root._w, img)
    root.title("ThinkFan Control")
    MainApplication(root).grid()
    root.mainloop()
