"""
Hello
My name is Bailey Nichols and this is a fibonacci flower
1/10/2021
"""
x, y = 1, 1
from turtle import *

a=Turtle()
b=Turtle()
c=Turtle()

a.hideturtle()
b.hideturtle()
c.hideturtle()

a.speed(50)
b.speed(50)
c.speed(100)

a.color('red')
b.color('orange')
c.color('magenta')

a.width(2)
b.width(2)
c.width(3)

b.penup()
b.goto(0,29)
b.pendown()

c.penup()
c.goto(159,202)
c.pendown()

while True:
    a.left(x)
    a.forward(x)

    b.right(x)
    b.forward(x)

    #print(x)

    x=x+x

    c.left(x)
    c.forward(x)

    if x >= 378:
        x=1
    if y == 100:
        break
