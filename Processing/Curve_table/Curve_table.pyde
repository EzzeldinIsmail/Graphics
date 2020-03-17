from math import sin, cos
box = 100
angle = 0
amount  = 10
canvas = PGraphics()

def setup():
    global canvas
    size(1000, 1000)
    canvas = createGraphics(1000, 1000)
    canvas.beginDraw()
    canvas.background(0)
    canvas.endDraw()
    frameRate(10)

def draw():
    global box, angle, amount, canvas
    canvas.beginDraw()
    canvas.noFill()
    canvas.stroke(255)
    image(canvas, 0, 0)
    
    for x in range(box, box*(amount+1), box):
        # Draws the 'header' circles which control the speed
        canvas.strokeWeight(8)
        canvas.circle(x+box/2, box/2, box-10)
        canvas.circle(box/2, x+box/2, box-10)
        
        # Draws the point moving along the header and the speed of the circle
        canvas.stroke(0)
        canvas.textSize(30)
        
        canvas.point((x+box/2) + (box/2 - 5)*cos(angle*(x/box)), 
              box/2 + (box/2 - 5)*sin(angle*(x/box)))
        canvas.point(box/2 + (box/2 - 5)*cos(angle*(x/box)), 
              x+box/2 + (box/2 - 5)*sin(angle*(x/box)))
        
        canvas.text("{:d}x".format(x/box), x +box/2 - 20, box/2 + 10)
        canvas.text("{:d}x".format(x/box), box/2 - 20, x+ box/2 + 10)
        
        # Deletes the previous point drawn on the header circle
        canvas.stroke(255)
        canvas.point((x+box/2) + (box/2 - 5)*cos((angle-.1)*(x/box)), 
              box/2 + (box/2 - 5)*sin((angle-.1)*(x/box)))
        canvas.point(box/2 + (box/2 - 5)*cos((angle-.1)*(x/box)), 
              x+box/2 + (box/2 - 5)*sin((angle-.1)*(x/box)))
    
    # Draws the circle table
    canvas.strokeWeight(2)
    for x in range(box, box*(amount+1), box):
        for y in range(box, box*(amount+1), box):
            canvas.point((x+box/2) + (box/2 - 5)*cos(angle*(x/box)), 
                        y+box/2 + (box/2 - 5)*sin(angle*(y/box)))
    
    canvas.endDraw()
    angle += .1
        
