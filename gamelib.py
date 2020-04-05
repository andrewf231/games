class Chapter(object):
  def __init__(self, chapter_text):
    scenes = chapter_text.split("\n\n")
    scenes = map(Scene, scenes)
    self.scenes = dict([(scene.key, scene) for scene in scenes])
    self.key = 'start'

  def play(self):
    current = self.scenes[self.key]
    print(current.story)
    action = int(input(current.prompt())) - 1
    if action in range(len(current.actions)):
      key = current.actions[action]
      self.key = key[0]
    return self.key


class Scene(object):
  def __init__(self, txt):
    data = txt.split("\n")
    self.story = "\n".join(data[1:-2])
    self.key = data[0].strip().strip(":")
    prompt = data[-2].split(",")
    locations = data[-1].split(",")
    prompt = map(str.strip, prompt)
    locations = map(str.strip, locations)
    self.actions = list(zip(locations, prompt))

  def __str__(self):
    return "%s: %s" % (self.key, str(self.prompt))

  def prompt(self):
    p  = "Choose an action: "
    actions = []
    for i, pair in enumerate(self.actions):
      loc, desc = pair
      actions.append("%s (%i)" % (desc, i + 1))
    return "%s %s: " % (p, ", ".join(actions))

  def select(self, action):
    action = int(action)
    if action in range(len(self.actions)):
      return self.actions.values

def main(chapter):
  chapter = Chapter(chapter)
  while True:
    current = chapter.play()
