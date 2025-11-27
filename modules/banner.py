#!/usr/bin/env python3
import pyfiglet
import os
from colorama import Fore, Style, init
init(autoreset=True)



def display_banner():
    os.system("clear")
    # Banner mətnini yaradıb çap edirik
    banner_text = pyfiglet.figlet_format("Holberton ToolKIT", font="ascii9")
    print(Fore.LIGHTRED_EX + banner_text)

def bosluk():
    print(" ")

if __name__ == "__main__":
    # Faylı birbaşa işə salanda banner çıxsın
    display_banner()
