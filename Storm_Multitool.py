import os
import sys
import socket
import colorama
from colorama import Fore
import pyfiglet

# Initialiser colorama
colorama.init(autoreset=True)

def display_title():
    ascii_art = pyfiglet.figlet_format("Storm", font="slant")  # Utiliser une police stylée
    print(Fore.BLUE + ascii_art)

def main_menu():
    print(Fore.BLUE + "Sélectionnez une fonctionnalité :")
    functionalities = [
        "├─ [01] Website Vulnerability Scanner",
        "├─ [02] Website Info Scanner",
        "├─ [03] Website Url Scanner",
        "├─ [04] Ip Scanner",
        "├─ [05] Ip Port Scanner",
        "├─ [06] Ip Pinger",
        "├─ [11] Dox Create",
        "├─ [12] Dox Tracker",
        "├─ [13] Username Tracker",
        "├─ [14] Email Tracker",
        "├─ [15] Email Lookup",
        "├─ [16] Phone Number Lookup",
        "├─ [21] Phishing Attack",
        "├─ [22] Password Decrypted Attack",
        "├─ [23] Password Encrypted",
        "├─ [24] Search In DataBase",
        "├─ [25] Dark Web Links",
        "└─ [26] Ip Generator",
        "└─ [31] Quitter"
    ]
    
    # Afficher les fonctionnalités horizontalement
    print(Fore.WHITE + "\n".join(functionalities))

def port_scanner(target):
    print(f"Scanning ports on {target}...")
    for port in range(1, 1025):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex((target, port))
        if result == 0:
            print(f"Port {port} is open")
        s.close()
    input(Fore.WHITE + "Tapez 'exit' pour revenir au menu principal : ")

def vulnerability_analysis(target):
    print(f"Analyse des vulnérabilités sur {target}...")
    # Implémente l'analyse de vulnérabilités
    input(Fore.WHITE + "Tapez 'exit' pour revenir au menu principal : ")

def website_info_scanner(target):
    print(f"Scanning information for {target}...")
    # Implémente l'analyse d'informations de site
    input(Fore.WHITE + "Tapez 'exit' pour revenir au menu principal : ")

def website_url_scanner(target):
    print(f"Scanning URL for {target}...")
    # Implémente l'analyse d'URL
    input(Fore.WHITE + "Tapez 'exit' pour revenir au menu principal : ")

def ip_scanner(target):
    print(f"Scanning IP {target}...")
    # Implémente l'analyse IP
    input(Fore.WHITE + "Tapez 'exit' pour revenir au menu principal : ")

def ip_port_scanner(target):
    print(f"Scanning ports on {target}...")
    # Implémente le scanner de ports IP
    input(Fore.WHITE + "Tapez 'exit' pour revenir au menu principal : ")

def ip_pinger(target):
    print(f"Pinging {target}...")
    # Implémente le ping IP
    input(Fore.WHITE + "Tapez 'exit' pour revenir au menu principal : ")

# Ajoutez d'autres fonctionnalités comme Dox Create, Phishing Attack, etc. ici...

if __name__ == "__main__":
    display_title()
    while True:
        main_menu()
        choice = input(Fore.BLUE + "Entrez votre choix : ")
        if choice == "1":
            target = input("Entrez l'adresse IP cible : ")
            port_scanner(target)
        elif choice == "2":
            target = input("Entrez l'adresse IP cible : ")
            website_info_scanner(target)
        elif choice == "3":
            target = input("Entrez l'adresse cible : ")
            website_url_scanner(target)
        elif choice == "4":
            target = input("Entrez l'adresse IP cible : ")
            ip_scanner(target)
        elif choice == "5":
            target = input("Entrez l'adresse IP cible : ")
            ip_port_scanner(target)
        elif choice == "6":
            target = input("Entrez l'adresse IP cible : ")
            ip_pinger(target)
        elif choice == "31":
            print("Au revoir !")
            break  # Sortir de la boucle pour quitter le tool
        else:
            print("Choix invalide, veuillez réessayer.")
