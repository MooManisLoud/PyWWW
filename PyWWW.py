from pypresence import Presence
import os
import urllib.request
import time
import pyfiglet
import sys
import subprocess
import requests
import datetime
import getpass
from keyboard import press
import threading

__version__ = "1.1.0"
__author__ = "Moo Man"
__name__ = "PyWWW"
__logfile__ = "log/mylog.txt"
logo_text = pyfiglet.figlet_format(__name__, font="slant", width=80, justify="center")
__user__ = getpass.getuser()

# with open("plugins\discordrpc\source\ThirdParty\DiscordRpcLibrary\Include\discord.txt", "r") as f:
#    code = f.read()
#    exec(code)

os.system("cls" if os.name == "nt" else "clear")

if os.name == "nt":
    os.system("title PyWWW")
else:
    print("\033]0;PyWWW\007")

print(logo_text)
print("PyWWW is experiencing some technical difficulties with code and could overwrite files, dont name the file the same as anther file that is important overwriting deletes the file.")
print("")
print(" ")
wtc = input("Are you sure you want to continue? (Y/N): ")

if wtc.lower() == "y":
    os.system("cls" if os.name == "nt" else "clear")
else:
    os.system('taskkill /IM python.exe /F')

    log_file = open(__logfile__, "a")

    log_file.write(str(datetime.datetime.now()) + "\n")

    log_file.write("PyWWW has seemed to have crashed or has been asked to close by another process\n")
    log_file.write("\n")

    log_file.close()

print(logo_text)
print(" ")
print("Created by:", __author__)
print("Version:", __version__)
print(" ")
print(__name__,"will start opening when pressing enter, if you want to cancel press the X in the top right!")
input("")

os.system("cls" if os.name == "nt" else "clear")

total_iterations = 10

for i in range(total_iterations):

    progress = (i + 1) / total_iterations * 100
    
    loading_message = f"{progress:.1f}%"
    
    print(loading_message, end="\r")
    time.sleep(0.5)

os.system("cls" if os.name == "nt" else "clear")

logo_text = pyfiglet.figlet_format(__name__, font="slant", width=80, justify="center")

print(logo_text)

print("")

print("[1] Info | [2] PyInjector | [3] Coming Soon")
print("")

while True:
    number = input("Pick a number (or 'q' to quit): ")
    
    if number == "q":
        break
    
    if number == "1":
        print("Version =", __version__)
        print("Creator =", __author__)
        print("Name =", __name__)
        print("File =", __file__)
        os.system("echo.")
    input("")
    press("enter")

    if number == "2":
        os.system("pip install pyinjector")
        os.system("pip install injector")
        print("Injector is being worked on!")
        input("")
        break

    if number == "3":
        print("Coming Soon")
        break