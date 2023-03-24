from pypresence import Presence
import os
import urllib.request
import time
import pyfiglet
import sys
import subprocess

__version__ = "1.0.0"
__author__ = "Moo Man"
__name__ = "PyWWW"

with open("data/discord.txt", "r") as f:
    code = f.read()
    exec(code)

print("Thank you for using", __name__)
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
    
    loading_message = f"Loading... {progress:.1f}%"
    
    print(loading_message, end="\r")
    time.sleep(0.5)

os.system("cls" if os.name == "nt" else "clear")

big_text = pyfiglet.figlet_format(__name__, font="slant", width=80, justify="center")

print(big_text)


url = input("Enter the URL to download: ")
file_name = os.path.basename(url)
save_path = input("Enter the path to save the file to: ")

# Create the save directory if it doesn't exist
if not os.path.exists(save_path):
    os.makedirs(save_path)

file_path = os.path.join(save_path, file_name)

# Download the file
urllib.request.urlretrieve(url, file_path)

python = sys.executable
os.execl(python, python, *sys.argv)