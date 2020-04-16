import curses
from curses import wrapper
from random import randint
from time import sleep

from level1 import meteors

from utils import get_logger

import curses_gamelib as g

log = get_logger(__name__)

pieces = []

def main(stdscr):
    pieces.append(g.Ship('ship', u"\U0001F680", 0, 0))
    screen = g.Screen(stdscr)
    for i, meteor in enumerate(meteors):
      size = meteor.get('size', 1)
      x = meteor['x']
      y = meteor['y']
      speed = meteor.get('speed', 1)
      pieces.append(g.Meteor('planet%s' % i,
                             ['*' * size] * size,
                             int(screen.max_x * x),
                             int(screen.max_y * y),
                             speed))

    stdscr.nodelay(True)
    curses.curs_set(0)
    # Clear screen
    key = ""
    while key != 'q':
      try:
        key = stdscr.getkey()
      except Exception:
        key = ""
      stdscr.clear()
      for item in pieces:
        item.play(screen, key)
      stdscr.refresh()
      sleep(.05)

if __name__ == '__main__':
  wrapper(main)
