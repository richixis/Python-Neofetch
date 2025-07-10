import os
import platform
import getpass

def neofetch():
    username = getpass.getuser()
    system = platform.system()
    release = platform.release()
    termux_info = "Termux" if "com.termux" in os.getenv("HOME", "") else system

    print(f"""
┌──[ {username} ]──────
│ OS: {termux_info} {release}
│ Shell: Python
│ Devs: Richix, FreeC
└──────────────────────
""")