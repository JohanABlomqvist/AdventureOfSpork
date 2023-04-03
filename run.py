import curses

# Set up the screen
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

# Set up colors
curses.start_color()
curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE)

#Defining function to print centered text
def prin_centered(y, text, color_pair):
    x = int ((80 - len(text)) / 2)
    screen.addstr(y, x, text, color_pair)