"""
Made by Ezzeldin Ismail
This is a program which uses the l system to draw fractals.
The l system works by having a starter string and changing it iteratively using
a set of rules.
To learn more about the l system you can go to:
https://en.wikipedia.org/wiki/L-system

To test it out just uncomment the type of map and rule that you wish to try
and assign the starter string to the respective string.
"""

from turtle import *
from time import sleep
from functools import partial
# Koch curve
# map = {"F": partial(forward, 10), "+": partial(left, 90), "-": partial(right, 90), }
# rule = {"F": "F+F-F-F+F"}
koch = "F"

# Sierpinski triangle
# map = {"F": partial(forward, 10), "G": partial(forward, 10), "+": partial(right, 120), "-": partial(left, 120),}
# rule = {"F": "F-G+F+G-F", "G": "GG"}
sierpinski = "F-G-G"

# Dragon curve
# map = {"F": partial(forward, 10), "+": partial(left, 90), "-": partial(right, 90), "X": lambda : (1), "Y": lambda : (1)}
# rule = {"X": "X+YF+", "Y": "-FX-Y"}
dragon = "FX"


screensize(canvwidth=5000, canvheight=5000, bg=None)
speed(0)
starter_string = dragon

def new(str):
    n = ""
    for s in str:
        if rule.get(s):
            n += rule[s]
        else:
            n+= s

    return n

def draw():
    global starter_string
    penup()
    goto(0, 0)
    pendown()
    for s in starter_string:
        map[s]()
    print(starter_string)
    starter_string = new(starter_string)


while True:
    draw()
    sleep(1)
    clear()
