# Thinkpad Fan Control GUI

# Light Mode

![Screenshot](https://i.imgur.com/2YNm0CD.png)

# Dark Mode

![Screenshot](https://i.imgur.com/I0oDYrX.png)

This is an application for controlling fan speed on IBM/Lenovo ThinkPads.

It can also monitor CPU temp and fan RPM.

It is written for Linux only. For windows, see http://www.almico.com/speedfan.php

## How it Works?
 + Parses `sensors` command to show CPU temp and fan RPM
 + Modifies `/proc/acpi/ibm/fan` to change fan speed

## Dependencies
+ lm-sensors
+ python3
+ python-tk
+ pystray
+ gksu


## Setup
+ chmod +x install.sh
+ sudo ./install.sh

---

Note: You are required to have the Linux kernel with `thinkpad-acpi` patch. (Ubuntu, Solus and a few others already seem to have this)
