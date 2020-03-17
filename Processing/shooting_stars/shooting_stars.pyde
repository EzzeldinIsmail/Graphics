from random import randint
def resetcoord():
    global x, y, inc
    x = randint(0, 400)
    y =  randint(0, 50)
    inc = 0

def setup():
    size(500, 500)
    resetcoord()
    frameRate(80)
    
def draw():
    global x, y , inc
    background(0)
    stroke(255)
    
    if inc+x < 500 and 2*inc+y < 500:
        print(x+inc/5, y + (2*inc)/5)
        line(x+inc/3, y + (2*inc)/3, inc+x, 2*inc+y)
        inc = inc *2 + .1
    else:
        resetcoord()

    # noLoop()
    
    
