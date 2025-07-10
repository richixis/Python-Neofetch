import platform, os, socket, time

def fetch():
    os.system("clear")
    print("=== 🌈 MiniPyFetch ===")
    print(f"👤 User:   {get_username()}")
    print(f"🧠 Kernel: {platform.release()}")
    print(f"📀 OS:     {platform.system()} {platform.version()}")
    print(f"⚙️  CPU:    {get_cpu_model()}")
    print(f"📡 IP:     {get_local_ip()}")
    print(f"⏱️ Uptime: {get_uptime()}")
    print(f"🖥  WM:     {os.environ.get('XDG_CURRENT_DESKTOP', 'N/A')}")

def get_username():
    return os.getenv("USER") or os.getenv("LOGNAME") or "unknown"

def get_cpu_model():
    try:
        with open("/proc/cpuinfo") as f:
            for line in f:
                if any(key in line for key in ["model name", "Hardware", "Processor"]):
                    return line.strip().split(":")[1].strip()
        return "Unknown"
    except:
        return "Unavailable"

def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
        return ip
    except:
        return "127.0.0.1"

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])
            days = int(uptime_seconds // (24 * 3600))
            hours = int((uptime_seconds % (24 * 3600)) // 3600)
            minutes = int((uptime_seconds % 3600) // 60)
            return f"{days}d {hours}h {minutes}m"
    except:
        return "Unknown"

fetch()
