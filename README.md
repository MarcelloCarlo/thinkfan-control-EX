# Thinkfan Control

# Light Mode

![Screenshot](https://i.imgur.com/D9DKHVH.png)

# Dark Mode

![Screenshot](https://i.imgur.com/JrypfkB.png)

This is an application for controlling fan speed on IBM/Lenovo ThinkPads.

It can also monitor CPU temp and fan RPM.

It is written for Linux only. For windows, see https://sourceforge.net/projects/tp4xfancontrol/

## How it Works?
 + Parses `sensors` command to show CPU temp and fan RPM
 + Modifies `/proc/acpi/ibm/fan` to change fan speed
 + to autostart edit the install.sh file

## Dependencies
+ lm-sensors
+ python3
+ python-tk
+ pillow-tk


## Setup
+ to activate autostart edit install.sh line 11 removing the "#" and adding your user instead of [youruser]
+ chmod +x install.sh
+ sudo ./install.sh

---

Note: You are required to have the Linux kernel with `thinkpad-acpi` patch. (Ubuntu, Solus and a few others already seem to have this)
