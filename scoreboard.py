from turtle import Turtle
score=0
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.i=0
        self.ht()
        self.goto(0, 250)
        self.pencolor("white")
        self.write(f"Score = {self.i} ", True, align="center", font=("Arial",18,"bold"))



    def increase_score(self):
        global score
        self.clear()
        self.penup()
        self.goto(0, 250)
        self.pendown()
        self.i=self.i+1
        self.write(f"Score = {self.i-1} ", True, align="center", font=("Arial", 18, "bold"))
        score= score + 1

    def final_score(self):
        self.goto(0,0)
        global score
        self.write("Game Over", True,"center",font=("calibri", 30, "bold"))
        return score-1