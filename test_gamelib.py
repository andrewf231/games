from unittest.mock import patch

import gamelib as g

import pytest


data = """parlor:
You enter a small parlor. A sofa, chairs and small armtables fill
the space. A TV hangs on the wall with an old VHS cassette of "Hawaii 5 0"
on the vcr below it. A door stands open at the far end.
continue, back
intro, kitchen"""

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

@pytest.fixture
def scene():
    return g.Scene(data)

@pytest.fixture
def chapter():
    return g.Chapter(chapter1)

def test_scene_parse_key(scene):
    assert scene.key == "parlor"

def test_scene_parse_description(scene):
    assert scene.story.endswith("A door stands open at the far end.")
    assert scene.story.startswith("You enter a small parlor.")

def test_scene_parse_action(scene):
    locations = [pair[0] for pair in scene.actions]
    descriptions = [pair[1] for pair in scene.actions]
    assert descriptions == ['continue', 'back']
    assert locations == ['intro', 'kitchen']

def test_scenes(chapter):
    assert len(chapter.scenes) == 3

def test_prompt(scene):
    p = scene.prompt()
    assert "continue (1), back (2)" in p

def test_play(chapter):
  with patch('builtins.input', new = lambda *x: 1):
    result = chapter.play()
    assert result == "2nd"
