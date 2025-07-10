import random
import shutil
import time
import os
import sys
import termios
import tty
import threading

green = '\033[1;32m'
reset = '\033[0m'

running = True

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def get_terminal_size():
    size = shutil.get_terminal_size((80, 20))
    return size.columns, size.lines

def generate_matrix_chars():
    return [chr(random.randint(33, 126)) for _ in range(100)]

def key_listener():
    global running
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)

    try:
        tty.setcbreak(fd)
        while running:
            ch = sys.stdin.read(1)
            if ch.lower() == 'q':
                running = False
                break
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

def run_matrix():
    global running
    clear()
    width, height = get_terminal_size()
    columns = int(width)
    drops = [random.randint(0, height) for _ in range(columns)]

    # Стартуем слушателя клавиш
    listener = threading.Thread(target=key_listener, daemon=True)
    listener.start()

    try:
        while running:
            print(green, end='')
            for i in range(columns):
                char = random.choice(generate_matrix_chars())
                if drops[i] < height:
                    print(f"\033[{drops[i]};{i}H{char}", end='')
                    drops[i] += 1
                else:
                    if random.random() > 0.975:
                        drops[i] = 0
            print(reset, end='')
            time.sleep(0.05)
    except KeyboardInterrupt:
        running = False
        clear()
        print("\n[✖] Матрица отключена через CTRL+C... Удачи, Нео 💊")
        return
    finally:
        if running:
            clear()
            print("\n[✖] Выход из Матрицы... До встречи, Нео 💊")

if __name__ == "__main__":
    run_matrix()
