from math import sin, cos, sqrt, pi, e
from random import randint
phi = ( 1 + sqrt(5) ) / 2
irrational = phi
angle = irrational
s = 10
def setup():
    global canvas
    size(1000, 1000)
    canvas = createGraphics(1000, 1000)
    frameRate(1000)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    
def draw():
    global angle, s
    y = s * sin(angle) + 500
    x = s * cos(angle) + 500
    canvas.beginDraw()
    canvas.stroke(255)
    canvas.strokeWeight(4)
    canvas.point(x, y)
    canvas.endDraw()
    image(canvas, 0, 0)
    angle += irrational
    s += 3
    # if(s>450):
    #     if randint(1, 100) < 100:
    #         # print("Here")
    #         canvas.beginDraw()
    #         canvas.strokeWeight(2)
    #         canvas.line(500, 500 , x, y)
    #         canvas.endDraw()
    if(s>750):
        # print("done")
        noLoop()
    # noLoop()
