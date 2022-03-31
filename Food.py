
from turtle import Turtle
import random
class food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
    def new_position(self):
        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        self.goto(x,y)
