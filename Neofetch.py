import platform, os, socket, subprocess, psutil

def os_info():
    try: return platform.system() + " " + platform.release()
    except: return "Unknown"

def uptime():
    try:
        out = subprocess.check_output(["uptime", "-p"], text=True).strip()
        return out[3:] if out.lower().startswith("up ") else out
    except: return "Unknown"

def cpu_info():
    try:
        with open("/proc/cpuinfo") as f:
            for l in f:
                if l.startswith("Hardware"):
                    return l.split(":")[1].strip()
    except: pass
    return platform.processor() or "Unknown"

def ram_info():
    try:
        m = psutil.virtual_memory()
        return f"{m.used//(1024**2)}MB / {m.total//(1024**2)}MB"
    except: return "Unknown"
print("")
print(f"User: {os.getenv('USER','unknown')}")
print(f"Host: {socket.gethostname()}")
print(f"OS: {os_info()}")
print(f"Uptime: {uptime()}")
print(f"CPU: {cpu_info()}")
print(f"RAM: {ram_info()}")
