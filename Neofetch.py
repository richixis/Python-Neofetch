import os
import platform
import socket
import psutil
from datetime import timedelta
from time import time

def neofetch():
    user = os.getenv("USER") or os.getenv("LOGNAME") or "unknown"
    host = socket.gethostname()
    os_info = f"{platform.system()} {platform.release()}"
    uptime_seconds = time() - psutil.boot_time()
    uptime = str(timedelta(seconds=uptime_seconds)).split('.')[0]

    cpu = platform.processor() or "Unknown"
    ram = psutil.virtual_memory()

    used_ram = ram.used // 1024 // 1024
    total_ram = ram.total // 1024 // 1024

    # Цвета ANSI
    CYAN = "\033[96m"
    GREEN = "\033[92m"
    MAGENTA = "\033[95m"
    RESET = "\033[0m"
    BOLD = "\033[1m"

    print()
    print(f"{BOLD}{MAGENTA}🌐 RichixOS NeoFetch 💀{RESET}")
    print(f"{CYAN}👤 User:   {RESET}{user}")
    print(f"{CYAN}💻 Host:   {RESET}{host}")
    print(f"{CYAN}📀 OS:     {RESET}{os_info}")
    print(f"{CYAN}⏳ Uptime: {RESET}{uptime}")
    print(f"{CYAN}⚙️  CPU:    {RESET}{cpu}")
    print(f"{CYAN}🧠 RAM:    {RESET}{used_ram}MB / {total_ram}MB")
    print()
