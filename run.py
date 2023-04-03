import curses

# Set up the screen
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#Defining function to print centered text
def prin_centered(y, text, color_pair):
    x = int ((80 - len(text)) / 2)
    