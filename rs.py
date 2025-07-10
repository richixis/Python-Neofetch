#!/data/data/com.termux/files/usr/bin/python

import os
import sys
import urllib.request

# Словарь пакетов
packages = {
    "neofetch": "https://raw.githubusercontent.com/richixis/Python-Neofetch/main/Neofetch.py",
}

# Проверка аргументов
if len(sys.argv) < 2:
    print("Usage: rs install <package>")
    sys.exit()

command = sys.argv[1].lower()

if command == "install":
    if len(sys.argv) < 3:
        print("Usage: rs install <package>")
        sys.exit()

    package = sys.argv[2].lower()
    if package in packages:
        url = packages[package]
        filename = package.capitalize() + ".py"

        print(f"[+] Installing {package}...")
        try:
            urllib.request.urlretrieve(url, filename)
            print(f"[✔] Installed as {filename}")
        except Exception as e:
            print(f"[✘] Download failed: {e}")
    else:
        print(f"[!] Package '{package}' not found.")
else:
    print(f"[!] Unknown command: {command}")
