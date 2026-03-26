import sys
import subprocess
import time

def move_cursor_to(x,y):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

clear_screen()

print(sys.stdout.isatty())

move_cursor_to(1,1)
sys.stdout.write("1")
time.sleep(1)
move_cursor_to(2,1)
sys.stdout.write("1")
time.sleep(1)
move_cursor_to(1,2)
sys.stdout.write("1")
time.sleep(1)

