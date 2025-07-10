import os
import random
import time
import shutil
import sys

# Цвета ANSI
GREEN = '\033[32m'
RESET = '\033[0m'

def clear():
    os.system('clear' if os.name != 'nt' else 'cls')

def main():
    width, height = shutil.get_terminal_size((80, 24))
    columns = width
    drops = [random.randint(-height, 0) for _ in range(columns)]

    try:
        clear()
        while True:
            line = [' '] * width
            for i in range(columns):
                if drops[i] >= 0 and drops[i] < height:
                    line[i] = chr(random.randint(33, 126))
                drops[i] += 1
                if drops[i] > height and random.random() > 0.975:
                    drops[i] = 0
            print(GREEN + ''.join(line) + RESET)
            time.sleep(0.05)
    except KeyboardInterrupt:
        clear()
        print("Матрица остановлена. До встречи, Нео!")

if __name__ == '__main__':
    main()
