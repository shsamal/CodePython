from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")

# for n in range(3, 11):
#     if n == 3:
#         tim.color("SteelBlue")
#     elif n == 4:
#         tim.color("yellow3")
#     elif n == 5:
#         tim.color("wheat3")
#     elif n == 6:
#         tim.color("SkyBlue")
#     elif n == 7:
#         tim.color("RosyBrown")
#     elif n == 8:
#         tim.color("yellow4")
#     elif n == 9:
#         tim.color("tomato")
#     elif n == 10:
#         tim.color("SkyBlue4")
#     for i in range(n):
#         tim.forward(100)
#         tim.right(360/n)


colors = ["SteelBlue", "yellow", "wheat3", "tomato", "purple", "red", "navy", "magenta"]


def sides(num_of_sides):
    for i in range(num_of_sides):
        tim.forward(100)
        tim.right(360/num_of_sides)


for n in range(3, 11):
    tim.color(random.choice(colors))
    sides(n)






screen = Screen()
screen.exitonclick()