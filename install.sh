#!/bin/sh
sudo mkdir /opt/fancontrol
sudo cp fan.py /opt/fancontrol/fan.py
sudo cp fan-pkexec /opt/fancontrol/fan-pkexec
sudo cp icon.png /opt/fancontrol/icon.png
sudo cp thinkfan.desktop /usr/share/applications/thinkfan.desktop
sudo cp Thinkfan.policy /usr/share/polkit-1/actions/Thinkfan.policy
sudo touch /etc/modprobe.d/thinkpad_acpi.conf
sudo echo "options thinkpad_acpi fan_control=1" > /etc/modprobe.d/thinkpad_acpi.conf
