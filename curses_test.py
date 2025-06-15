# curses_test 
# 測試 curses 
import curses 
from curses import wrapper

def main(stdscr):
    stdscr.clear()
    stdscr.addstr(10,10,"Hello ")
    stdscr.addstr(11,10,"World ")
    stdscr.refresh()
    stdscr.getch()
wrapper(main)