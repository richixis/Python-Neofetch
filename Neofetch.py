import platform, os

def fetch():
    os.system("clear")
    print("=== MiniPyFetch ===")
    print(f"User: {os.getlogin()}")
    print(f"Kernel: {platform.release()}")
    print(f"OS: {platform.system()} {platform.version()}")
    print(f"CPU: {get_cpu_model()}")
    print(f"WM: {os.environ.get('XDG_CURRENT_DESKTOP', 'N/A')}")

def get_cpu_model():
    with open("/proc/cpuinfo") as f:
        for line in f:
            if "model name" in line:
                return line.strip().split(":")[1]

fetch()
