import curses

# Get the curses window, turn off echoing of keyboard to screen, turn on
# instant (no waiting) key response, and use special values for cursor keys
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

screen.addstr(0, 0, 'Press a cursor key, or press "q" key to stop.\n')

try:
    while True:
        char = screen.getch()
        if char == ord('q'):
            print("quit\r")
            break
        elif char == curses.KEY_UP:
            print("up\r")
        elif char == curses.KEY_DOWN:
            print("down\r")
        elif char == curses.KEY_RIGHT:
            print("right\r")
        elif char == curses.KEY_LEFT:
            print("left\r")
        elif char == 10:    # <Enter>
            print("stop\r")

finally:
    curses.nocbreak()
    curses.echo()
    screen.keypad(0)
    curses.endwin()
