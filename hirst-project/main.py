import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
colour_list = [(231, 233, 238), (207, 160, 81), (56, 88, 130), (144, 91, 41), (139, 27, 48), (221, 207, 108), (134, 177, 201), (157, 47, 85), (43, 54, 105), (170, 159, 41), (130, 189, 144), (83, 20, 43), (39, 43, 64), (185, 95, 108), (189, 140, 166), (86, 122, 180), (59, 40, 31), (89, 157, 93), (80, 153, 165), (194, 80, 73), (45, 75, 77), (160, 201, 219), (54, 129, 127), (80, 75, 44), (218, 176, 186), (46, 74, 73), (170, 206, 167)]

tim.setheading(200)
tim.forward(300)
tim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colour_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
