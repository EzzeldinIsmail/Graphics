from random import randint
s = 0
x = []
y = []

def setup():
    size(500, 500)
    frameRate(60)
    
def draw():
    global s, x, y
    background(0)
    print(s)
    if s == 0:
        x = [randint(0, 500) for i in range(10)]
        y = [randint(0, 500) for i in range(10)]
        s = 0
        
    for i in range (10):
        circle(x[i], y[i], s)
    s = (s+1) % 10
    stroke(s)
