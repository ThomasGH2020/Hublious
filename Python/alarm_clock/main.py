import time
import sys
import threading
import queue
import re
import curses

"""
mytime = time.time()
mylocaltime = time.localtime(mytime)
currentLocalTime = f"{mylocaltime.tm_hour}:{mylocaltime.tm_min}"
mycustomtime = "16:20"

while 1 > 0:
    alarmReached = False
    alarm = input("Set alarm time: ")

    while alarmReached == False:
        mylocaltime = time.localtime(time.time())
        currentLocalTime = f"{mylocaltime.tm_hour}:{mylocaltime.tm_min}"
        print(f"Current Time: {currentLocalTime}")
        if currentLocalTime == alarm:
            print("Alarm reached")
            break
        time.sleep(1)

"""

console_lock = threading.Lock()

def clear_screen():
    sys.stdout.write("\033[2J\033[H")
    sys.stdout.flush()

def move_cursor_to(x,y):
    sys.stdout.write(f"\033[{y};{x}H")
    sys.stdout.flush()

def update_current_time(prevTime,currentTime):
    if currentTime != prevTime:
        with console_lock:
            move_cursor_to(15,0)
            print(currentTime,end="")
            prevTime = currentTime 
    
def get_input(inputQueue):
    cmd = input()
    inputQueue.put(cmd)
    with console_lock:
        move_cursor_to(1,3)
        print(f"Alarm set for: {cmd}",end="")



def main():
    """# init screen
    scr = curses.initscr()

    # disable echoing stdin
    curses.noecho()

    # enable non-blocking mode
    curses.cbreak()"""


    prevTime = time.strftime("%H:%M",time.gmtime())
    currentTime = time.strftime("%H:%M",time.gmtime())
    cmd = ""
    alarmTime = ""
    alarmTimeFormat = r'^\d{2}:\d{2}$'
    inputQueue = queue.Queue()

    input_thread = threading.Thread(target=get_input,args=[inputQueue])


    with console_lock:
        move_cursor_to(1,1)
        sys.stdout.write(f"Current Time: {prevTime}")
        move_cursor_to(1,2)
        sys.stdout.write("Enter alarm time: ")

    input_thread.start()

    while True:
        currentTime = time.strftime("%H:%M",time.gmtime())
        update_current_time(prevTime,currentTime)

        if currentTime == alarmTime:
            with console_lock:
                move_cursor_to(1,3)
                print("Alarm!!!")

        if not inputQueue.empty():

            input_thread.join()
            cmd = inputQueue.get()

            if cmd == "quit" or cmd == "exit":
                break

            if re.fullmatch(alarmTimeFormat,cmd):

                alarmTime = cmd

                with console_lock:
                    move_cursor_to(1,3)
                    print(f"Alarm set for: {alarmTime}")
            else:
                with console_lock:
                    move_cursor_to(1,2)
                    print("Enter alarm time: ")
                input_thread.start()
    

    curses.nocbreak()
    curses.echo()
    curses.curs_set(1)
    curses.endwin()


if __name__ == "__main__":
    sys.exit(main())

