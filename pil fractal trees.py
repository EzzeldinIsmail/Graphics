from PIL.Image import *
from PIL.ImageDraw import *
from PIL import *
from math import sin, cos, radians
height, width = 2000, 2000
im = new("L", (height, width), color=255)
d = Draw(im)
tree_length = 500   # 200
start_angle = 25  # 30
recursive_depth = 25    # 30
curviness = 1.1       # 1.1
n = 0
colours = ["Red", "Yellow", "Green", "Blue", "Purple"]
def rec_tree(x, y, length, angle):
    global n, d
    if length < 30:
        return
    n +=1
    x1 = x + int(length*sin(radians(angle)))
    y1 = y - int(length*cos(radians(angle)))
    d.line([(x, y),(x1, y1)], width=int(length/30), fill=0)
    print(angle, x, y, "->", x1, y1)
    # rec_tree(length-(length*(30/100)), angle-(angle*(30/100)), depth*60/100)
    rec_tree(x1, y1, length * (1 - (recursive_depth / 100)), abs(angle * curviness))
    rec_tree(x1, y1, length * (1 - (recursive_depth / 100)), -abs(angle * curviness))


d.line([(width/2, height), (width/2, height-200)], width=int((tree_length+30)/30))
rec_tree(width/2, height-200, tree_length, start_angle)
rec_tree(width/2, height-200, tree_length, -start_angle)
im.show()
