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
start

parlor:
You enter a small parlor. A sofa, chairs and small armtables fill
the space. A TV hangs on the wall with an old VHS cassette of "Hawaii 5 0"
on the vcr below it. A door stands open at the far end.
continue, back
start, kitchen
"""

import gamelib

if __name__ == "__main__":
  gamelib.main(chapter1)
