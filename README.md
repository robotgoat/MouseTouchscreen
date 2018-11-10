# Raspberry Pi Touchscreen: Experiments for Mice

## Goal
The purpose of this project is to create a flexible and extensiable tool to design interactive touch based experiments for mice. For this, the open source NUI framework optimized for touch input called Kivy is used. 

## Setup Guide
### Parts Used For This Setup
1. Raspberry Pi 3 Model B
2. Element14 7 inch touchscreen display
3. Touchscreen enclosure

## Useful Prerequisites
If you are not used to a GNU-Linux type environment or the Raspberry Pi, here are some good guides that can help. 

Raspberry Pi:
- http://engr.uconn.edu/~song/classes/nes/slides/Pi-I.pdf

Linux:
- https://www.funtoo.org/Linux_Fundamentals,_Part_1
- http://www.ee.surrey.ac.uk/Teaching/Unix/unixintro.html

## Raspberry Pi Setup
The steps that follow describe how to prepare the Raspberry Pi for Kivy.
For this, we will use Raspbian as our OS installed on a micro SD card. The full Raspbian version will used and can be downloaded from here: https://www.raspberrypi.org/downloads/raspbian/. To make the image on the micro SD card, it is recommended to use the tool called Etcher: https://www.balena.io/etcher/. Once Raspbian (Stretch used in for this project) is written, it can be inserted into the Pi's SD card slot. It will then boot and ask you to setup with a new root password and time as well as updates. Next, we will setup the OS so Kivy projects such as the one in this repository can run.

## Installing Kivy (version 1.11.0.dev0 as of writing this guide)
Kivy can be installed for the most part by following the guide in the docs: https://kivy.org/doc/stable/installation/installation-rpi.html. For this installation, it was found Kivy works best by installing globally. First, open terminal and run in order:
- `sudo apt-get update`
- `sudo apt-get install libsdl2-dev libsdl2-image-dev libsdl2-mixer-dev libsdl2-ttf-dev \
   pkg-config libgl1-mesa-dev libgles2-mesa-dev \
   python-setuptools libgstreamer1.0-dev git-core \
   gstreamer1.0-plugins-{bad,base,good,ugly} \
   gstreamer1.0-{omx,alsa} python-dev libmtdev-dev \
   xclip xsel`

We then have to install the dependancies for Kivy and this project. Kivy utilizes Cython, a package that optimzes Python code by calling native C or C++ functions for ultimately more efficient memory and CPU usage. Along with Cython, install Pandas. This process will take a while, so feel free to do other tasks as the packages compile and install.
- `sudo pip install Cython Pandas`

Next, the Rpi is ready to install Kivy globally.
- `sudo pip install git+https://github.com/kivy/kivy.git@master`

Now, we have to change the config file for Kivy to tell it to accept touch input from the touchscreen. Open the config file with a text editor such as Vim using:
- `vim ~/.kivy/config.ini`

Find the `[input]` section and add the following lines:
```
mouse = mouse 
mtdev_%(name)s = probesysfs,provider=mtdev
hid_%(name)s = probesysfs,provider=hidinput
```

There is also an error with this version of Rasbian or Kivy not using openGL as the default renderer. To set it, add the line `export KIVY_GL_BACKEND=gl` in your `.profile` file and restart the Pi. Now, the system is ready to run the Kivy application.

## Kivy Application 
Copy this repository by copying the URL and performing a `git {url name}` in a directory of your choice. Then go into it with `cd {name of folder}`. Run `ls` to verify all the files are there, and lastly, run the program with `python main.py`. To exit the program, you can either use the Esc key or `ctrl-c`. 

The app shows a circle and square in two halves of the screen with a black background. It records how many times and at what time each button is pressed. The output of this recording is in a file called `mouse_game_results.csv`. Note, these buttons do not have any visual indication showing that they have been touched.

## Software, References, and Links
1. Kivy: https://kivy.org/#home 
2. Etcher: https://www.balena.io/etcher/
3. Kivy Docs: https://kivy.org/doc/stable/guide/basic.html