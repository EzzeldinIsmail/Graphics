from turtle import *
from math import cos, sin, pi
mode("logo")
screensize(canvwidth=5000, canvheight=5000, bg=None)

timetable = 11
modulo = 200
coord = lambda theta: (cos(theta* 2*pi)*300 , sin(theta* 2*pi)*300 )
color("black")
# penup()
setpos(-300, 0)
speed(0)

# setpos(0, -300)
# for timetable in range(200):
if True:
    # timetable = 91
    for i in range(modulo):
        x, y = coord(i/modulo % modulo)
        setpos(x, y)
        ans = timetable*i
        x, y = coord(ans/modulo % modulo)
        print(x, y)
        pendown()
        setpos(x, y)
        penup()
        # setpos(-300, 0)
    clear()

print("done")
done()