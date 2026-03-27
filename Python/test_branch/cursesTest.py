import curses
import time

scr = curses.initscr()

# disable the displaying of stdin to terminal
curses.noecho()

# non-blocking mode
#curses.cbreak()

# terminal beep sound
curses.beep()

# flash the screen white for a bit
curses.flash()

# set the cursor to be invisible
curses.curs_set(0)

# writing to the terminal, (y,x,text)
scr.addstr(0,0,"Test")
scr.addstr(1,0,"Press any key to continue")

# update terminal screen
scr.refresh()

# get a character of input 
inpt = scr.getstr()
scr.addstr(2,0,inpt)
scr.refresh()

time.sleep(2)

curses.nocbreak()
curses.echo()
curses.curs_set(1)
curses.endwin()