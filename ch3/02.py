import turtle
t=turtle.Turtle()
t.shape('turtle')
side=100
n=int(input('몇각형을 그리시겠습니까'))
angle=360//n

for i in range(n):
    t.forward(side)
    t.left(angle)
