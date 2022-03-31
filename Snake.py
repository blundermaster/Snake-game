import turtle
from turtle import Turtle,Screen
s=Screen()
class snake:
    def __init__(self):
        self.d=[]
        self.create_snake()

    def create_snake(self):
        global d
        t = [Turtle() for i in range(6)]
        for i in range(6):
            t[i].shape("square")
            t[i].color("white")
            t[i].speed("fast")
            t[i].home()
            t[i].penup()
            self.d.append(t[i])
        c=0
        for f in self.d:
            a=f.xcor()
            self.d[self.d.index(f)+1].goto(a-10,0)
            c+=1
            if c==5:
                break
    def move(self):
        position= []
        for i in range(0,len(self.d)):
            position.append(self.d[i].pos())
        for j in range(len(self.d)):

            if j==0:
                self.d[0].fd(10)
            else:
                self.d[j].setposition(position[j-1])
    def up(self):
        if self.d[0].heading()!=270:
            self.d[0].setheading(90)
    def down(self):
        if self.d[0].heading()!=90:
            self.d[0].setheading(270)
    def right(self):
        if self.d[0].heading()!=180:
            self.d[0].setheading(0)
    def left(self):
        if self.d[0].heading()!=0:
            self.d[0].setheading(180)

    def extend(self):
        new_segment = Turtle()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.speed("fast")
        new_segment.goto(self.d[-1].position())
        self.d.append(new_segment)

