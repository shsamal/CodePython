from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.hideturtle()
tim.width(7)
tim.speed(10)

colors = ["SteelBlue", "yellow", "wheat3", "tomato", "purple", "red", "navy", "magenta"]
directions = [0, 90, 180, 270]


for i in range(300):
    tim.color(random.choice(colors))
    tim.forward(15)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()