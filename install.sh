#!/bin/sh
install_folder=/opt/fancontrol
mkdir $install_folder
echo "Enter 1 for light mode or 2 for dark mode"
read mode 
case "$mode" in
    1) cp fan.py $install_folder/fan.py ;;
    2) cp fan-dark.py $install_folder/fan.py ;;
    *) echo "Input not valid" ;;
esac
cp fan-pkexec $install_folder/fan-pkexec
cp icon.png $install_folder/icon.png
cp thinkfan.desktop /usr/share/applications/thinkfan.desktop
cp Thinkfan.policy /usr/share/polkit-1/actions/Thinkfan.policy
touch /etc/modprobe.d/thinkpad_acpi.conf
echo "options thinkpad_acpi fan_control=1" > /etc/modprobe.d/thinkpad_acpi.conf
