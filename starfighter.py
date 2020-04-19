import curses
from curses import wrapper
from random import randint
from time import sleep

from level1 import meteors

from utils import get_logger

import curses_gamelib as g

log = get_logger(__name__)

pieces = {}

def load_pieces(meteors, level, screen):
  pieces = {}
  for i, meteor in enumerate(meteors[level]):
    size = meteor.get('size', 1)
    x = meteor['x']
    y = meteor['y']
    speed = meteor.get('speed', 1)
    piece = g.Meteor('planet%s' % i,
                     ['*' * size] * size,
                     int(screen.max_x * x),
                     int(screen.max_y * y),
                     speed)
    pieces[piece.label] = piece

  return pieces

def build_level(level, screen):
    pieces = load_pieces(meteors, level, screen)
    ship = g.Ship('ship', u"\U0001F680", 0, 0)
    ship.reset()
    pieces['ship'] = ship
    return pieces

game_over = """
   ____                         ___
  / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __
 | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
 | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |
  \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
"""

ouch = """
   ___  _   _  ____ _   _
  / _ \| | | |/ ___| | | |
 | | | | | | | |   | |_| |
 | |_| | |_| | |___|  _  |
  \___/ \___/ \____|_| |_|

""".split("\n")

def main(stdscr):

    screen = g.Screen(stdscr)
    level = 0
    pieces = build_level(level, screen)
    pass_level = g.PassLevel(screen, pieces, 'ship')

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
      for item in pieces.values():
        item.play(screen, key)
      # Check for collisions
      ship = pieces['ship']
      for piece in pieces.values():
        if piece.label != ship.label:
          if piece.collide(ship):
            piece.explode(ouch, 10)
            ship.reset()
      # Check to pass the level
      if pass_level.check():
        level += 1
        if level >= len(meteors):
          screen.addstr(0, 0, game_over)
          stdscr.refresh()
          key = 'q'
          sleep(3)
        else:
          pieces = build_level(level, screen)
          pass_level = g.PassLevel(screen, pieces, 'ship')

      stdscr.refresh()
      sleep(.05)

if __name__ == '__main__':
  wrapper(main)
