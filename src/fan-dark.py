#!/usr/bin/python3
import tkinter as tk
import os
import subprocess
from tkinter import *
from time import sleep
from threading import Thread


#Get system info
import subprocess as sub

def set_speed(speed=None):
    """
    Set speed of fan by changing level at /proc/acpi/ibm/fan
    speed: 0-7, auto, disengaged, full-speed
    """
    print("set level to %r" % speed)
    return subprocess.check_output(
        'echo level {0} | sudo tee "/proc/acpi/ibm/fan"'.format(speed),
        shell=True
    ).decode()
    
def get_info():
    info_lines = subprocess.check_output("sensors").decode("utf-8").split("\n")
    result = []
    count = 0
    for i in info_lines:
        if "Core" in i:
            result.append("Core %d: " % count + i.split(":")[-1].split("(")[0].strip())
            count += 1

        if "fan" in i:
            result.append("Fan : " + i.split(":")[-1].strip())
            count +=1

        if "Level" in i:
            result.append(("Level : %r" % speed) + i.split(":")[1].strip())
    return result

def printLevel():
    print("set level to %r" % speed)


class MainApplication(tk.Frame):
    def __init__(self, parent, *args, **kwargs):
        root.configure(background='black')
        tk.Frame.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.parent.minsize(width=100, height=100)

        main_label = tk.Label(parent, text="",bg="#000000", fg="white")
        main_label.grid(row=0, column=0)


        row1 = tk.Frame()
        row1.grid()

        for i in range(8):
            tk.Button(row1, text=str(i), highlightbackground="#1A1C1A", bg="#000000", fg="white", highlightcolor="#1A1C1A", highlightthickness=3, bd=0, activebackground="#e60012", activeforeground="white", command=lambda x=i: set_speed(x)).grid(
                row=0, column=i + 1
            )


        row2 = tk.Frame()
        row2.grid()


        tk.Button(row2, text="Auto", highlightbackground="#1A1C1A", bg="#000000", fg="white", highlightcolor="#1A1C1A", highlightthickness = 3, bd = 0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("auto")).grid(
            row=0, column=0
        )
        tk.Button(row2, text="Full", highlightbackground="#1A1C1A", bg="#000000", fg="white", highlightcolor="#1A1C1A", highlightthickness = 3, bd = 0, activebackground="#e60012", activeforeground="white", command=lambda: set_speed("full-speed")).grid(
            row=0, column=1
        )




        def display_loop():
            while True:
                sleep(0.5)
                main_label["text"] = "\n".join(get_info())

        Thread(target=display_loop).start()


if __name__ == "__main__":

    root = tk.Tk()
    img = tk.Image("photo", file='/opt/fancontrol/Resources/icon.png')
    root.tk.call('wm','iconphoto',root._w,img)
    root.title("Thinkfan Control")
    MainApplication(root).grid()
    root.mainloop()

