from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN

from utils import get_logger
import attr

log = get_logger(__name__)

class Event(object):
  def __init__(self, window, pieces):
    self.window = window
    self.pieces = pieces

  def check(self):
    pass

class PassLevel(Event):
  def __init__(self, window, pieces, piece):
    super().__init__(window, pieces)
    self.piece = piece

  def check(self):
    player = self.pieces[self.piece]
    if player.x >= self.window.max_x - 1:
      return True

class Screen(object):
  def __init__(self, window):
    max_y, max_x = window.getmaxyx()
    self.max_x = max_x
    self.max_y = max_y
    self.window = window

  def contain(self, gameobj):
    """Constrain x,y to within 0, max values."""
    x, y = gameobj.x, gameobj.y
    if x < 0:
      x = 0
    if x + gameobj.width > self.max_x:
      x = self.max_x - gameobj.width
    if y < 0:
      y = 0
    if y + gameobj.height > self.max_y:
      y = self.max_y - gameobj.height
    return x, y

  def addstr(self, x, y, data):
    if isinstance(data, list):
      for i, line in enumerate(data):
        self.window.addstr(y + i, x, line)
    else:
      self.window.addstr(y, x, data)

@attr.s
class Tick(object):
  length: int = 0
  current: int = 0

  def tick(self):
    if self.length == 0:
      return False
    r = False
    self.current += 1
    if self.current >= self.length:
      self.current = 0
      r = True
    return r

  def set(self, length):
    self.length = length


class Velocity(object):
  """Max velocity is to move every time. 0 velocity doesn't move. Can have negative velocity."""
  def __init__(self, current=0, min=0, max=10):
    self.min = min
    self.max = max
    self.tick = Tick()
    self.set(current)

  def incr(self):
    self.set(self.current + 1)

  def decr(self):
    self.set(self.current - 1)

  def set(self, current):
    # Can't set speed less than min, more than max
    current = min(current, self.max)
    current = max(self.min, current)
    self.current = current
    if current == 0:
      self.tick.set(0)
    else:
      self.tick.set(self.max - abs(current) + 1)

  def move(self):
    return self.tick.tick()

  @property
  def direction(self):
    return -1 if self.current < 0 else +1

  def flip(self):
    self.set(self.current * -1)

class GameObject(object):
  def __init__(self, label, data, x, y):
    self.x = x
    self.y = y
    self.data = data
    self.label = label

  @property
  def box(self):
    return (self.x, self.y, self.x + self.width, self.y + self.height)

  @property
  def height(self):
    if isinstance(self.data, list):
      return len(self.data)
    return 1

  @property
  def width(self):
    if isinstance(self.data, list):
      return max(map(len,self.data))
    return len(self.data)

  def collide(self, other):
    tx, ty, bx, by = self.box
    if tx <= other.x <= bx:
      if ty <= other.y <= by:
        return True

  def play(self, window, key):
    window.addstr(self.x, self.y, self.data)

  def __str__(self):
    return "{label} ({x},{y})".format(**self.__dict__)


class Meteor(GameObject):
  def __init__(self, label, data, x, y, velocity=1):
    super().__init__(label, data, x, y)
    self.data_backup = None
    self.anim_length = 0
    self.velocity = Velocity(velocity, -10, 10)

  def explode(self, text, length=10):
    self.data_backup = self.data
    self.data = text
    self.anim_length = length

  def play(self, window, key):
    if self.velocity.move():
      self.y += 1 * self.velocity.direction
    x,y = window.contain(self)
    if (x,y) != (self.x, self.y):
      self.velocity.flip()
      self.x, self.y = x, y
    if self.data_backup:
      if self.anim_length > 0:
        self.anim_length -= 1
      else:
        self.data = self.data_backup
        self.data_backup = None
    super().play(window, key)

class Ship(GameObject):
  def __init__(self, label, data, x, y):
    super().__init__(label, data, x, y)

    self.x_velocity = Velocity(0, -10, 10)
    self.y_velocity = Velocity(0, -10, 10)


  def reset(self):
    self.x, self.y = 0, 0

  def play(self, window, key):
    # Handle 4 arrow keys
    if key == 'KEY_DOWN':
      self.y_velocity.incr()
    elif key == 'KEY_LEFT':
      self.x_velocity.decr()
    elif key == 'KEY_RIGHT':
      self.x_velocity.incr()
    elif key == 'KEY_UP':
      self.y_velocity.decr()

    # Move in direction of velocity
    if self.x_velocity.move():
      self.x = self.x + self.x_velocity.direction
    if self.y_velocity.move():
      self.y = self.y + self.y_velocity.direction
    self.x, self.y = window.contain(self)
    super().play(window, key)
