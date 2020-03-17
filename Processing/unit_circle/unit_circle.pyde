from math import pi, cos, sin
theta = 0
radius = 100
def setup():
    global canvas
    size(500, 500)
    frameRate(15)
    canvas = createGraphics(500, 500)
    canvas.beginDraw()
    canvas.background(255)
    canvas.endDraw()
    
def draw():
    global theta, radius
    image(canvas, 0, 0)
    x =  (radius * cos(theta) + 250)
    y =  (radius * sin(theta) + 250)
    stroke(0)
    strokeWeight(1)
    theta = (theta + .1) 
    print(x, y)
    line(x, 250, x, y)
    line(250, y, x, y)
    canvas.beginDraw()
    canvas.point(x, y)
    canvas.endDraw()
    
