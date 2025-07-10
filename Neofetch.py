import os
import platform
import socket
from datetime import timedelta
from time import time

def get_uptime():
    try:
        with open("/proc/uptime", "r") as f:
            seconds = float(f.readline().split()[0])
            return str(timedelta(seconds=seconds)).split(".")[0]
    except:
        return "Unavailable"

def get_ram():
    try:
        meminfo = open("/proc/meminfo", "r").readlines()
        total = int(meminfo[0].split()[1]) // 1024
        free = int(meminfo[1].split()[1]) // 1024
        available = int(meminfo[2].split()[1]) // 1024
        used = total - available
        return f"{used}MB / {total}MB"
    except:
        return "Unavailable"

def neofetch():
    CYAN = "\033[96m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    user = os.getenv("USER") or os.getenv("LOGNAME") or "unknown"
    host = socket.gethostname()
    os_info = f"{platform.system()} {platform.release()}"
    uptime = get_uptime()
    ram = get_ram()

    print(f"\n{BOLD}{MAGENTA}🌐 RichixOS NeoFetch 💀{RESET}")
    print(f"{CYAN}👤 User:   {RESET}{user}")
    print(f"{CYAN}💻 Host:   {RESET}{host}")
    print(f"{CYAN}📀 OS:     {RESET}{os_info}")
    print(f"{CYAN}⏳ Uptime: {RESET}{uptime}")
    print(f"{CYAN}🧠 RAM:    {RESET}{ram}\n")
