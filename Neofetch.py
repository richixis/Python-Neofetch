import platform, os

def fetch():
    os.system("clear")
    print("=== 🌈 MiniPyFetch ===")
    print(f"👤 User:   {get_username()}")
    print(f"🧠 Kernel: {platform.release()}")
    print(f"📀 OS:     {platform.system()} {platform.version()}")
    print(f"⚙️  CPU:    {get_cpu_model()}")
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

# ✅ Запуск только если это основной файл
if __name__ == "__main__":
    fetch()
