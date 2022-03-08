#!/bin/sh
install_folder=/opt/fancontrol
mkdir $install_folder
mkdir $install_folder/src
cp src/fan.py $install_folder/src/fan.py ;;
cp Resources/thinkfan.desktop /usr/share/applications/thinkfan.desktop
cp src/fancontrol $install_folder/fancontrol
ln -s $install_folder/fancontrol /bin/fancontrol
mkdir $install_folder/Resources
cp Resources/icon.png $install_folder/Resources/icon.png
cp Resources/on.png $install_folder/Resources/on.png
cp Resources/off.png $install_folder/Resources/off.png
chmod +r $install_folder/Resources/off.png
touch /etc/modprobe.d/thinkpad_acpi.conf
echo "options thinkpad_acpi fan_control=1" > /etc/modprobe.d/thinkpad_acpi.conf
