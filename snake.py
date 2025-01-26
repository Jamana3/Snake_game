import turtle
from turtle import Turtle

class Snake:

    def __init__(self):

        x = 0
        y = 0
        self.object = []
        for i in range(0, 3):
            i = turtle.Turtle()
            i.penup()
            i.color("white")
            i.shape("square")
            i.goto(x, y)
            self.object.append(i)
            x -= 20


    def move(self):
        for i in range(len(self.object) - 1, 0, -1):
            self.object[i].goto(self.object[i - 1].xcor(), self.object[i - 1].ycor())
        self.object[0].forward(20)

    def add_object(self):
        i = Turtle()
        i.penup()
        i.color("white")
        i.shape("square")
        self.object.append(i)


    def right(self):
        if  self.object[0].heading() != 180:
            self.object[0].setheading(0)

    def up(self):
        if self.object[0].heading() != 270:
           self.object[0].setheading(90)

    def down(self):
        if self.object[0].heading() != 90:
           self.object[0].setheading(270)

    def left(self):
        if self.object[0].heading() != 0:
           self.object[0].setheading(180)

