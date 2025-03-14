from turtle import *

RADIUS = 300

def draw_board():
    # -- set up
    screensize(800, 800)
    speed("fastest")
    title("Wyznaczanie π metodą Monte Carlo")
    penup()

    # -- square
    color("gray50", "gray80")
    begin_fill()
    goto(-RADIUS, -RADIUS)
    pendown()
    for i in range(4):
        forward(2*RADIUS)
        left(90)
    end_fill()

    # -- circle
    color("gray70", "gray90")
    goto(0, -RADIUS)
    pendown()
    begin_fill()
    circle(RADIUS)
    end_fill()
    penup()


    # -- X-axis
    pencolor("gray50")
    goto(-400, 0)
    pendown()
    goto(400, 0)
    penup()

    # -- Y-axis
    goto(0, -400)
    pendown()
    goto(0, 400)
    penup()

    hideturtle()


def put_dot(x, y, color="black"):
    goto(x*RADIUS, y*RADIUS)
    dot(5, color)
