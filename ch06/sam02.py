fig=int(input('몇각형을 그릴까여'))

import turtle
t= turtle.Turtle()

for i in range(fig):
    t.forward(10)
    t.left(360/fig)
