#!/bin/sh
install_folder=/opt/fancontrol
mkdir $install_folder
mkdir $install_folder/src
echo "Enter 1 for light mode or 2 for dark mode"
read mode 
case "$mode" in
    1) cp src/fan.py $install_folder/src/fan.py ;;
    2) cp src/fan-dark.py $install_folder/src/fan.py ;;
    *) echo "Input not valid" ;;
esac
echo "Enter 1 for ElementaryOS, 2 for Gnome, 3 for KDE or 4 for LXDE"
read mode
case "$mode" in
    1) cp Resources/thinkfan-pantheon.desktop /usr/share/applications/thinkfan.desktop ;;
    2) cp Resources/thinkfan-gnome.desktop /usr/share/applications/thinkfan.desktop ;;
    3) cp Resources/thinkfan-kde.desktop /usr/share/applications/thinkfan.desktop ;;
    4) cp Resources/thinkfan-lxde.desktop /usr/share/applications/thinkfan.desktop ;;
    *) echo "Input not valid" ;;
esac
cp fancontrol $install_folder/fancontrol
rm /bin/fancontrol
ln -s $install_folder/fancontrol /bin/fancontrol
mkdir $install_folder/Resources
cp Resources/icon.png $install_folder/Resources/icon.png
cp Resources/thinkfan.desktop
touch /etc/modprobe.d/thinkpad_acpi.conf
echo "options thinkpad_acpi fan_control=1" > /etc/modprobe.d/thinkpad_acpi.conf
: 'cp Thinkfan.policy /usr/share/polkit-1/actions/Thinkfan.policy
cp fan-pkexec $install_folder/fan-pkexec'
