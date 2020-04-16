chapter1 = """start:
You enter the mansion as directed by the
stranger. The front door creaks silently closed. In front of you
are stairs to the second level and rooms to the left and right.
up, left, or right
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
back
start

2nd:
There is a huge dining table with a chandelier with blue candles the size of
light bulbs.There is a picture of picasso.The carpet is green with purple spots
on it every so often.There is a bearskin rug in the entry. Wait... there is a
camoflouged gray button on the wall
touch the button, go back
button, start

button:
A sliding door opens as you slowly go in. Its a long deep stairway down.
You see cobwebs every way you turn. Its is very dark. The stairway is very
dusty.it seems very gloomy in this deep dark dusty place but then you see a
door.
enter the secret room, go back to the living room
secretroom, 2nd

secretroom:
This is a very dark and open space. you finally see a torch. You happen to
have a match you light it.Once it light up you see that there are very many
chests. As you look on the century old walls yoi see pictures of famous people
in hawaii. you see a globe!
examine the globe,examine the chests
globe,chests

chests:
nothing in these dusty old chests
back
secretroom

globe:
You turn the globe around your finger slips on the island hawaii! the globe
springs open. inside is a piece of paper with the islands hawaii new zealand
australia and japan.
examine japan,new zealand,australia, or hawaii
japan, nz, aus, hawaii

japan:
no clues
back
globe

nz:
no clues
back
globe

aus:
no clues
back
globe

hawaii:
As you touch the island hawaii a big X appears over it. Now it all makes sense!
you say. Its a treasure map!
go on to chapter 2
chapter2

chapter2:
Welcome to chapter 2 One and all! thank you so much for playing this game!
After this chapter there will be One more! And in case your wondering,NO
SPOILERS!
go to the chapter2 start
chapter2 start

chapter2 start:
You go out of the mansion. The stranger says "I knew you would find the
treasure map! I will accompany you the rest of the way. Now lets go to the
forest!
trust him and go into the forest, don't trust him and go without him
forest with him, forest without him

forest without him:
we'll i am very sorry but i WILL HAVE TO KILL YOU SINCE YOU DONT TRUST ME!
you died.
back
chapter2 start

forest with him:
You go into the forest.  Ahead you see a sign it says go left to the docks and
go right to the city.The city slopes up. the docks slope down.
left, right
docks,city

city:
uh oh, ROBBERS! stick em up the robbers said. oh no you lost the map
back
chapter2 start

Docks:
The stranger says here i have enough money to buy a STEAMSHIP WITH CANNONS AND
AN ARMY IN IT!nice you say lets get to sea!You soon sail out.You see pirates to
the left blocking the way.
go around them, fight them
fight, RUN!

RUN!:
You try to go around them.They just fire cannons at you and you sink you died!
back
docks

fight:
You fought. You got captured. The pirates have taken your treasure map and you
will be FORCED TO WALK THE PLANK!
escape the ship, surrender and walk the plank
escape,plank

plank:
You and stranger walked the plank and eaten by sharks. YOU DIED
back,
fight
"""

import gamelib

if __name__ == "__main__":
  gamelib.main(chapter1)

