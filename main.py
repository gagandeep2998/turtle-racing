import random
from turtle import Turtle, Screen

is_race_on = False
screen = Screen()
screen.title("Turtle Racing")
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter the color:")

colours = ["red", "green", "orange", "yellow", "blue", "purple"]
turtles = []
x = -230
y = -100
for i in range(6):
    tim = Turtle(shape="turtle")
    tim.color(colours[i])
    tim.penup()
    tim.goto(x, y)
    y += 30
    turtles.append(tim)

if user_bet:
    is_race_on = True


while is_race_on:
    for turtle in turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

        if turtle.xcor() > 230:
            is_race_on = False
            winner_color = turtle.pencolor()
            if user_bet == winner_color:
                print(f"You got it right, {winner_color} turtle is the winner")
            else:
                print(f"You loose, {winner_color} turtle is winner.")






screen.exitonclick()
