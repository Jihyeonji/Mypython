size = input('집의 크기는 얼마로 할까요?')
size = int(size)
import turtle
t = turtle.Turtle()
t.shape('turtle')

t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)
t.forward(size)
t.right(90)

t.forward(size)
t.left(120)
t.forward(size)
t.left(120)
t.forward(size)

