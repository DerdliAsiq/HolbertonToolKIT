from colorama import init, Fore, Back, Style
import time
from modules.banner import display_banner, bosluk
from modules.info_gather import info_gather_module, info_gather_menu
import os

init(autoreset=True)


def main_menu():
    menu = ("\n\n\t1. Information Gathering\n\t2. Vulnerability Analysis\n\t3. Web Application Analysis\n\t4. Database Assessment\n\t5. Password Attacks\n\t6. Wireless Attacks\n\t7. Exploitation Tools\n\t8. Sniffing & Spoofing\n\t9. Post Exploitation\n\t10. Forensics\n\t11. Social Engineering Tools")
    print(menu)

def animate_message(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.0002)  
    print() 


display_banner()


display_banner() #Banner gelir
print(Fore.BLUE + "                             Developed by Holberton Hack Team")
bosluk()



animate_message( """
This tool is intended solely for educational and ethical hacking purposes.
Unauthorized scanning is against the law and constitutes a criminal offense.
The development team and Holberton School are not responsible for any actions
carried out using this tool.
""")

main_menu()
main_choice = int(input('Choice: '))
if main_choice == 1:
    info_gather_module()
    info_gather_menu()