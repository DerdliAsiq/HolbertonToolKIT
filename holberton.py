from colorama import init, Fore, Back, Style
import time
from modules.banner import display_banner, bosluk
import os
import numpy
init(autoreset=True)
display_banner() #Banner gelir
print("                             Developed by Holberton Hack Team")
bosluk()
disclaimer = """
This tool is intended solely for educational and ethical hacking purposes.
Unauthorized scanning is against the law and constitutes a criminal offense.
The development team and Holberton School are not responsible for any actions
carried out using this tool.
"""

print(
    Back.WHITE + Fore.BLACK + Style.BRIGHT + disclaimer + Style.RESET_ALL
)

def main_menu():
    menu = ("\n\n\t1. Information Gathering\n\t2. Vulnerability Analysis\n\t3. Web Application Analysis\n\t4. Database Assessment\n\t5. Password Attacks\n\t6. Wireless Attacks\n\t7. Exploitation Tools\n\t8. Sniffing & Spoofing\n\t9. Post Exploitation\n\t10. Forensics\n\t11. Social Engineering Tools")
    print(menu)
main_menu()