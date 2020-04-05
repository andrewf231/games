chapter1 = """start:
You enter the mansion as directed by the 
stranger. The front door creaks silently closed. In front of you
are stairs to the second level and rooms to the left and right.
up, left, right
2nd, bedroom, parlor

bedroom:
You are in a bedroom. The bed is small and over it hangs
a picture of a Hawaiian beach.
back
intro

parlor:
You enter a small parlor. A sofa, chairs and small armtables fill
the space. A TV hangs on the wall with an old VHS cassette of "Hawaii 5 0" 
on the vcr below it. A door stands open at the far end.
continue, back
intro, kitchen
"""

class Scene(object):
  def __init__(self, txt):
    data = txt.split("\n")
    self.story = "\n".join(data[1:-2])
    self.key = data[0].strip().strip(":")
    prompt = data[-2].split(",")
    locations = data[-1].split(",")
    prompt = map(str.strip, prompt)
    locations = map(str.strip, locations)
    self.prompt = dict(zip(prompt, locations))

  def __str__(self):
    return self.key + str(self.prompt)

def parse(data):
  chapter = {}
  data = data.split("\n\n")
  for scene in data:
    s = Scene(scene)
    chapter[s.key] = s
  return chapter

def main():
  tree = parse(chapter1)
  for k,v in tree.items():
    print(k, str(v))
  key = "start"
  while True:
    current = tree[key]
    print(current.story)
    action = raw_input("Choose action: " + ", ".join(current.prompt.keys()))
    if action in current.prompt:
      key = current.prompt[action]
   

if __name__ == "__main__":
  main()

