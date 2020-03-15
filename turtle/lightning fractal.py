from turtle import *
from random import choice
from random import randint
mode("logo")
start_length = 200   # 200

n = 100
percentage = .5
colours = ["Red", "Yellow", "Green", "Blue", "Purple"]
screensize(canvwidth=5000, canvheight=5000, bg=None)
def reset(cp, hd):
    penup()
    setpos(*cp)
    setheading(hd)
    pendown()

def rec_light(length):
    if length < 4:
        return
    n = randint(5, 90)
    forward(length)
    cp = pos()
    hd = heading()
    right(n)
    rec_light(length * percentage)
    print(length)
    reset(cp, hd)
    left(n)
    rec_light(length * percentage)



color("black")


setpos(0, 0)
speed(0)
seth(180)
# ht()
rec_light(start_length)
print(n)
done()