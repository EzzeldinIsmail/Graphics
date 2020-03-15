from turtle import *
from random import choice
mode("logo")
tree_length = 200   # 200
start_angle = 90 # 30, 4780, 90, 13**11
recursive_depth = 30    # 30
curviness = 1.1       # 1.1
smallness = 30      # 30
n = 0
invert = 1
# colours = ["Red", "Yellow", "Green", "Blue", "Purple"]
colours = ['Black']
screensize(canvwidth=5000, canvheight=5000, bg=None)
def rec_tree(length, angle):
    global n
    if length < 30:
        return
    n +=1
    depth = length/30
    colour = choice(colours)
    color(choice(colours))
    width(depth)
    cp = pos()
    hd = heading()
    setheading(hd)
    left(angle)
    forward(invert*length)
    # rec_tree(length-(length*(30/100)), angle-(angle*(30/100)), depth*60/100)
    rec_tree(length - (length * (recursive_depth / 100)), angle * curviness)
    penup()
    setpos(*cp)
    setheading(hd)
    color(choice(colours))
    pendown()
    width(depth)
    right(angle)
    forward(invert*length)
    rec_tree(length - (length * (recursive_depth / 100)), angle * curviness)


color("black")


setpos(0, 0)
speed(0)
width(12)
forward(invert*200)
rec_tree(tree_length, start_angle)
ht()
print(n)
done()

#
# def lsystem(string, depths, rules: list):
#     if depths != 0:
#         s = ''
#         for c in string:
#             for rule, change in rules:
#                 if rule(c):
#                     s += change
#                     break
#             else:
#                 s += c
#         yield s
#         yield from lsystem(s, depths-1, rules)
#
#
# rules = [(lambda x: 'A' in x, 'AB'), (lambda x: 'B' in x, 'A')]
# axiom = 'A'
# before = len(axiom)
# # print(before)
# for i in lsystem(axiom, 15, rules):
#     print(i, len(i)/before)
#     before = len(i)
#

