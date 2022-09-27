from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")

        self.food_x = randint(-260, 260)
        self.food_y = randint(-260, 260)
        self.goto(self.food_x, self.food_y)

    def refresh(self):
        self.food_x = randint(-280, 280)
        self.food_y = randint(-260, 260)
        self.goto(self.food_x, self.food_y)
