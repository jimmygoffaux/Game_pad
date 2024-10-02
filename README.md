# Game_pad
use for update raspberry pi (3) in game pad programmer for slider (KNX) 

## install rasbian
Installing raspbian on raspberry pi (used raspberry pi imager) 
https://www.raspberrypi.com/software/
Don't forget to active SSH before download : 
![image](https://github.com/user-attachments/assets/ef2ba6f3-4771-4200-8363-def7cde9b519)

## for remote acces on raspberry pi 
```
sudo apt install tightvncserver
sudo apt install xrdp
```

## copy all file on raspberry pi 
import all file on raspberry pi from Github 
install git on raspberry pi : 
```
sudo apt-get install git
```
go to the location where you want to copy the files
```
cd /home/tester/Desktop
git clone https://github.com/jimmygoffaux/Game_pad.git
```

## install all the librairie 
copy the pip_install.txt file to the raspberry pi and run the following command from the file location:
```
pip install -r pip_install.txt
```

## configur the HDMI port for game pad 
```
sudo nano /boot/config.txt
```
=> add line : 
#hdmi_force_hotplug=1
#hdmi_drive=2

## launch script at start up
allows you to launch the script to use the game pad buttons and launch the script to update the sliders
```
sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
```
=> add line : 
@lxterminal -e /usr/bin/python /home/tester/Desktop/test.py
@lxterminal -e /home/tester/Desktop/Run_update.sh

## add software for update slider 
The software versions used must be placed in the KNX_updater directory and in .BIN format
If you need to convert a .HEX file to a .BIN file you can use binutils :
```
sudo apt-get install binutils
objcopy -I ihex -O binary fichier.hex fichier.bin
```
/!\ don't forget to change the name of the programming file in the StartDFU.py file:
![image](https://github.com/user-attachments/assets/a1ccdc7e-a1f1-4afc-87bb-5041dd25fe2c)

