import curses

# Set up the screen
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

