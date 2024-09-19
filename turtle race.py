from turtle import Screen,Turtle
import random

screen=Screen()
screen.setup(width=500,height=400)
bet=screen.textinput(title="Make your bet",prompt="Which turtle will win the race? Enter a color: ")

colors=["red","orange","yellow","green","blue","purple"]
pos=[-70,-40,-10,20,50,80]
all_turtles=[]

for i in range(6):
    turtle=Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.penup()
    turtle.goto(x=-230,y=pos[i])
    all_turtles.append(turtle)

is_race_on=False
if bet:
    is_race_on=True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race_on=False
            win=turtle.pencolor()
            if win==bet:
                print(f"You've won! The {win} turtle is the winner.")
            else:
                print(f"You've lost! The {win} turtle is the winner.")
                
        dist=random.randint(0,10)
        turtle.forward(dist)

screen.exitonclick()