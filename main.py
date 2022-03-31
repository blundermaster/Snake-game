import time
from turtle import Screen,Turtle
from Snake import snake
from Food import food
from scoreboard import Scoreboard
mysnake=snake()
s=Screen()
f=food()
score=Scoreboard()
s.setup(width=600,height=600)
s.bgcolor("black")
s.title("Saap e Chobol maarey")
s.tracer(0)

w=s.textinput(title="Choose difficulty", prompt="Easy or Hard").lower()
s.listen()
s.onkeypress(mysnake.up,"Up")
s.onkeypress(mysnake.down,"Down")
s.onkeypress(mysnake.right, "Right")
s.onkeypress(mysnake.left,"Left")

game_is_on=True
c=400


# def extend():
#     new_segment = Turtle()
#     new_segment.shape("square")
#     new_segment.color("white")
#     new_segment.penup()
#     new_segment.speed("fast")
#     new_segment.goto(mysnake.d[-1].position())
#     mysnake.d.append(new_segment)


while game_is_on:
    s.update()
    time.sleep(0.1)

    if w=="easy":
        mysnake.move()
        if mysnake.d[0].xcor()>360:
            mysnake.d[0].setx(-c)
            for i in range (1,len(mysnake.d)):
                for j in range(0,i):
                    mysnake.d[j].fd(20)
                mysnake.d[i].setx(-c)

        if mysnake.d[0].xcor()<-360:
            mysnake.d[0].setx(c)
            for i in range(1, len(mysnake.d)):
                for j in range(0, i):
                    mysnake.d[j].fd(20)
                mysnake.d[i].setx(c)
        if mysnake.d[0].ycor() > 360:
            mysnake.d[0].sety(-c)
            for i in range(1, len(mysnake.d)):
                for j in range(0, i):
                    mysnake.d[j].fd(20)
                mysnake.d[i].sety(-c)
        if mysnake.d[0].ycor()<-360:
            mysnake.d[0].sety(c)
            for i in range(1, len(mysnake.d)):
                for j in range(0, i):
                    mysnake.d[j].fd(20)
                mysnake.d[i].sety(c)

        if mysnake.d[0].distance(f)<15:
            f.new_position()
            score.increase_score()
            mysnake.extend()
        for i in range(1, len(mysnake.d)):
            if mysnake.d[0].xcor()<320 and mysnake.d[0].xcor()>-320 and mysnake.d[0].ycor()<320 and mysnake.d[0].ycor()>-320:
                if mysnake.d[0].position() == mysnake.d[i].position():
                    print(f"Game over. Your score is {score.final_score()}")
                    game_is_on = False

    elif w=="hard":
        mysnake.move()
        if mysnake.d[0].distance(f) < 15:
            f.new_position()
            score.increase_score()
            mysnake.extend()
        if mysnake.d[0].xcor() > 280 or mysnake.d[0].xcor() < -280 or mysnake.d[0].ycor() > 280 or mysnake.d[
            0].ycor() < -280:
            print(f"Game over. Your score is {score.final_score()}")
            game_is_on = False
        for i in range(1, len(mysnake.d)):
            if mysnake.d[0].position() == mysnake.d[i].position():
                print(f"Game over. Your score is {score.final_score()}")
                game_is_on = False
    else:
        print("Wrong Choice")
        game_is_on=False

















s.exitonclick()