from turtle import Turtle,Screen
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.create()


    def create(self):
        self.penup()
        xcor = random.randint(-220, 220)
        ycor = random.randint(-220, 220)
        self.goto(xcor, ycor)
