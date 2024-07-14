from turtle import Turtle, Screen
import random

is_race_on = True
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "violet"]

tim = Turtle(shape="turtle")
terry = Turtle(shape="turtle")
alex = Turtle(shape="turtle")
jack = Turtle(shape="turtle")
teddy = Turtle(shape="turtle")
mike = Turtle(shape="turtle")

turtles = [tim, terry, alex, jack, teddy, mike]

color_counter = 0
turtle_x_pos = -240
turtle_y_pos = -150
for turtle in turtles:
    turtle.color(colors[color_counter])
    turtle.penup()
    turtle.goto(turtle_x_pos, turtle_y_pos)
    turtle_y_pos += 60
    color_counter += 1

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()
