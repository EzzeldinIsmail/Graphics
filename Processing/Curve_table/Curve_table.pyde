from math import sin, cos
box = 100
angle = 0
amount  = 10
canvas = PGraphics()
screen_size = 1000
white = 255
black = 0

diameter = box - 10
radius = diameter/2
half_circle = box/2
draw_lines = True

def setup():
    global canvas
    size(screen_size, screen_size)
    canvas = createGraphics(screen_size, screen_size)
    canvas.beginDraw()
    canvas.background(black)
    canvas.endDraw()
    frameRate(10)

def draw():
    global box, angle, amount, canvas
    linecanvas = createGraphics(screen_size, screen_size)
    linecanvas.beginDraw()
    linecanvas.background(black, black, black, 0)
    linecanvas.stroke(white)
    
    canvas.beginDraw()
    canvas.noFill()
    canvas.stroke(white)
    image(canvas, 0, 0)
    
    for x in range(box, box*(amount+1), box):
        circle_count = x/box
        circle_center = x + half_circle
        # Due to the circle being drawn from the center,
        # it must be moved half a circle to avoid it being drawn off screen
        
        # Draws the 'header' circles which control the speed
        canvas.strokeWeight(8)
        canvas.circle(circle_center, half_circle, diameter) # y is fixed @ 0 + half_circle
        canvas.circle(half_circle, circle_center, diameter) # x is fixed @ 0 + half_circle
        
        # Draws the point moving along the header and the speed of the circle
        canvas.stroke(black)
        canvas.textSize(30)
        
        canvas.point(circle_center + radius * cos(angle * circle_count), 
              half_circle - radius * sin(angle * circle_count))
        canvas.point(half_circle + radius * cos(angle * circle_count), 
              circle_center - radius * sin(angle * circle_count))
        # For the x values, we want it to start on the right and then move left so we
        # have to add it at the beginning ans as the angle increases cos will decrease
        # Similar thinking for the y values
        
        canvas.text("{:d}x".format(circle_count), circle_center - 20, half_circle + 10)
        canvas.text("{:d}x".format(circle_count), half_circle - 20, circle_center + 10)
        
        # Draws the lines
        if draw_lines:
            linecanvas.line(circle_center + radius * cos(angle * circle_count), 0, 
                            circle_center + radius * cos(angle * circle_count), 1000)
            linecanvas.line(0, circle_center - radius * sin(angle * circle_count), 
                            1000, circle_center - radius * sin(angle * circle_count))
        
        # Deletes the previous point drawn on the header circle
        canvas.stroke(white)
        canvas.point(circle_center + radius * cos((angle-.1) * circle_count), 
              half_circle - radius * sin((angle-.1) * circle_count))
        canvas.point(half_circle + radius * cos((angle-.1) * circle_count), 
              circle_center - radius * sin((angle-.1) * circle_count))
    
    # Draws the circle table
    canvas.strokeWeight(2)
    for x in range(box, box*(amount+1), box):
        for y in range(box, box*(amount+1), box):
            canvas.point(x + half_circle + radius * cos(angle * x/box ), 
                        y + half_circle - radius * sin(angle * y/box))
    
    linecanvas.endDraw()
    image(linecanvas, 0, 0)
    canvas.endDraw()
    linecanvas.clear()
    
    angle += .1
        
