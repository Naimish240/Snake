import time
import curses

opts = ['Home', 'Play', 'Scoreboard', 'Exit']

def print_menu(scr, row):
    scr.clear()
    curses.curs_set(0)
    h, w = scr.getmaxyx()

    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)

    for i, j in enumerate(opts):
        x = w//2 - len(j)//2
        y = h//2 - len(opts)//2 + i
        if i == row:
            scr.attron(curses.color_pair(1))
            scr.addstr(y, x, j)
            scr.attroff(curses.color_pair(1))
        else:
            scr.addstr(y, x, j)

    scr.refresh()

def navigation(scr):
    row = 0
    scr.clear()
    curses.curs_set(0)
    print_menu(scr, row)
    
    while True:
        key = scr.getch()
        scr.clear()
        if key == curses.KEY_UP and row > 0:
            row -= 1
        elif key == curses.KEY_DOWN and row < len(opts) - 1:
            row += 1
        elif key == curses.KEY_ENTER or key in [10, 13]:
            scr.addstr(0, 0, "You Selected {}".format(opts[row]))
            scr.refresh()
            ch = scr.getch()
        else:
            scr.addstr(0, 0, "INVALID")
        print_menu(scr, row)
        scr.refresh()

curses.wrapper(navigation)                    # Wraps the main function with curses
