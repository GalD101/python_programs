from turtle import *

from turtle import *
from math import pi
width(2)


def eye():
    # white of the eye
    color('black', 'white')
    begin_fill()
    circle(50)
    end_fill()
    forward(25)
    # pupil
    color('black', 'black')
    begin_fill()
    circle(25)
    end_fill()
    back(25)


def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    begin_fill()
    for i in range(60):
        forward(pi * radius / 30)
        left(6)
    end_fill()
    right(90)
    penup()
    back(radius)

speed(20)
# your code here
left(90)
color('Pale Green', 'purple')
circle(250)
forward(75)
left(270)
forward(100)
eye()
back(50)
eye()
right(90)
forward(150)
left(90)
forward(220)

pendown()

# GAL signature
color('Purple')
width(5)
forward(33)
right(90)
forward(50)
right(90)
forward(33)
right(45)
forward(47)
right(45)
forward(33)
right(45)
forward(47)
right(45)
forward(33)

penup()
right(90)
forward(100)
left(90)
forward(30)
pendown()

left(60)
forward(115)
right(120)
forward(115)
left(180)
forward(40)
left(60)
forward(73)
left(180)
forward(73)
right(60)
forward(40)

left(60)
penup()
forward(30)
pendown()
left(90)
forward(100)
back(100)
right(90)
forward(50)

back(300)
penup()
back(600)
pendown()

hideturtle()
color('black', 'magenta')


def left_turn():
    for i in range(10):
        forward(15)
        left(9)


def petal():
    color('black', 'Pale Turquoise')
    begin_fill()
    left_turn()
    left(90)
    left_turn()
    left(90)
    end_fill()

speed(30)
penup()
forward(200)
for i in range(5):
    forward(i*10)
    right(i*45)

penup()
left(180)
forward(160)
pendown()
for i in range(5):
    petal()
    right(360/5)

getscreen().getcanvas().postscript(file='outputname.ps')
bye()
width(3)
speed(10)

# how to draw a centered circle


def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    for i in range(60):
        forward(3.14*radius/30)
        left(6)
    right(90)
    penup()
    back(radius)

# how to draw an eye


def eye():
    color('orange', 'white')
    begin_fill()
    circle(50)
    end_fill()
    forward(25)
    # pupil
    color('black', 'black')
    begin_fill()
    circle(25)
    end_fill()
    back(25)


def right_arc(radius, angle):
    for i in range(angle):
        forward(2*3.14*radius/360)
        right(1)


def centered_arc(radius, angle):
    penup()
    left(angle/2)
    forward(radius)
    right(90)
    pendown()
    right_arc(radius, angle)
    penup()
    left(90)
    back(radius)
    left(angle/2)


# drawing the head
color('orange', 'yellow')
begin_fill()
circle(300)
end_fill()

# drawing the left eye
left(90)
forward(150)
left(90)
forward(100)
right(270)
eye()

# drawing the right eye
left(90)
forward(200)
right(90)
eye()

# move back into the middle
right(90)
forward(100)
left(90)

# drawing the mouth
width(15)
forward(200)
#left(180)
color('red')
centered_arc(100, 72)

hideturtle()
bye()


