#import colorgram as co
# colors = co.extract("hirst.jpg", 30)
# c_list = []
#
# for i in range(len(colors)):
#
#     r = colors[i].rgb.r
#     g = colors[i].rgb.g
#     b = colors[i].rgb.b
#     c_tup = (r, g, b)
#     c_list.append(c_tup)
# print(c_list)
import turtle as t
import random as r
t.colormode(255)
hirst_colors = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216), (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179)]
timmy = t.Turtle()
timmy.penup()
timmy.speed("fastest")
timmy.setpos(-300, -200)
timmy.hideturtle()
for i in range(10):

    timmy.setpos(-300, timmy.ycor()+40)
    for _ in range(10):
        timmy.fd(50)
        timmy.pd()
        timmy.dot(20, r.choice(hirst_colors))
        timmy.pu()









screen = t.Screen()
screen.exitonclick()
