import time
import sys
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

def clear_eol(y: int, x: int, scr: curses.window) -> None:
    scr.move(y,x)
    scr.clrtoeol()

def update_current_time(prevTime: str, currentTime: str, scr: curses.window) -> None:
    if currentTime != prevTime:
        scr.addstr(0,14,currentTime)
        prevTime = currentTime 
    
def get_input(cmd: str,inputQueue: queue.Queue,scr: curses.window) -> str:
    ch = scr.getch()
    if ch == curses.KEY_BACKSPACE or ch == 127:
        cmd = cmd[:-1]
        clear_eol(1,18,scr)
        scr.addstr(1,18,cmd)
        return cmd
    elif ch == curses.KEY_ENTER or ch == 10:
        inputQueue.put(cmd)
        clear_eol(1,18,scr)
        return cmd
    elif ch != curses.ERR and ch != -1:
        cmd += chr(ch)
        scr.addstr(1,18,cmd)
        return cmd
    else:
        return cmd



def main(scr) -> None:

    curses.assume_default_colors(-1,-1)

    # set cursor to be invis
    curses.curs_set(0)

    scr.nodelay(True)

    prevTime = time.strftime("%H:%M",time.gmtime())
    currentTime = time.strftime("%H:%M",time.gmtime())
    cmd = ""
    alarmTime = ""
    alarmTimeFormat = r'^\b(?:[01]\d|2[0-3]):[0-5]\d\b'
    inputQueue = queue.Queue()

    scr.addstr(0,0,f"Current Time: {prevTime}")
    scr.addstr(1,0,"Enter alarm time: ")

    scr.refresh()

    while True:
        currentTime = time.strftime("%H:%M",time.gmtime())
        update_current_time(prevTime,currentTime,scr)

        if currentTime == alarmTime:
            scr.addstr(3,0,"Alarm!!!")
            alarmTime = ""

        cmd = get_input(cmd,inputQueue,scr)
        
        scr.refresh()

        if not inputQueue.empty():

            cmd = inputQueue.get()

            if cmd == "quit" or cmd == "exit":
                break

            if cmd == "snooze":
                clear_eol(3,0,scr)
                clear_eol(2,0,scr)

            if re.fullmatch(alarmTimeFormat,cmd):

                alarmTime = cmd
                clear_eol(2,0,scr)
                scr.addstr(2,0,f"Alarm set for: {alarmTime}")
                clear_eol(3,0,scr)
            else:
                scr.addstr(1,0,"Enter alarm time: ")
    
            cmd = ""

    curses.raw()
    curses.echo()
    curses.nocbreak()
    curses.curs_set(1)
    curses.endwin()


if __name__ == "__main__":
    curses.wrapper(main)

