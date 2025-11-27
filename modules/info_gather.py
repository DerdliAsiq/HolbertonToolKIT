from .banner import display_banner, bosluk  # nisbi import
from colorama import Fore, Back, Style, init

init(autoreset=True)

def animate_message(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.0002)  
    print() 

def info_gather_module():
    display_banner()
    print(Fore.RED + "\t- INFO GATHERING MODULE -")
    bosluk()
    # buradan sonra menu, tools və s.

def info_gather_menu():
    print(Fore.BLUE + Style.BRIGHT + "\n\n\t1. Nmap port scan\n\t2. Whois\n\t3. Web infrastructure detect\n\t")

def main():
    info_gather_module()
    info_gather_menu()
    print("DENEME")

if __name__ == "__main__":
    main()
