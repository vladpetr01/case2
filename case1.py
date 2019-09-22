#First case
# Developers:   Zemtseva A. (30%),
#               Petrov V. (60%),
#               Daniel A. (30%)
import turtle
import math


def big_red_triangle(x, y, a) :
    #TODO (Nastya) Big red Triangle
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    b = (a * math.tan(math.radians(45)))
    c = (a / math.cos(math.radians(45)))

    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(c)
    turtle.left(135)
    turtle.forward(b)
    turtle.end_fill()
    pass

def orange_square(x, y, a) :
    # TODO (Alina) Function, drawing orange square.
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('orange')
    turtle.fillcolor('orange')
    turtle.begin_fill()
    turtle.fd(a)
    turtle.right(90)
    turtle.fd(a)
    turtle.right(90)
    turtle.fd(a)
    turtle.right(90)
    turtle.fd(a)
    turtle.right(90)
    turtle.pendown()
    turtle.end_fill()
    pass

def small_purple_triangle(x, y, a):
    #TODO (Vlad) Function, drawing small purple triangle
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('purple')
    turtle.fillcolor('purple')
    turtle.begin_fill()
    b = (2 ** 0.5) * a
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.pendown()
    turtle.end_fill()
pass


def big_yellow_triangle(x, y, a):
    #TODO (Nastya) Big yellow Triangle
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()

    b = (a * math.tan(math.radians(45)))
    c = (a / math.cos(math.radians(45)))

    turtle.begin_fill()
    turtle.forward(a)
    turtle.left(135)
    turtle.forward(c)
    turtle.left(135)
    turtle.forward(b)
    turtle.end_fill()
pass


def blue_triangle(x, y, a) :
    #TODO (Alina) Function, drawing blue triangle.
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('light blue')
    turtle.fillcolor('light blue')
    turtle.begin_fill()
    b = (2 ** 0.5) * a
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(2 * a)
    turtle.right(135)
    turtle.forward(b)
    turtle.pendown()
    turtle.end_fill()
pass


def green_parallelogram(x, y, a):
    #TODO (Vlad) Function, drawing Green Parallelogram
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('green')
    turtle.fillcolor('green')

    b = (2 ** 0.5) * a

    turtle.begin_fill()
    turtle.fd(b)
    turtle.right(30)
    turtle.fd(a)
    turtle.right(60)
    turtle.fd(b)
    turtle.right(150)
    turtle.fd(a)
    turtle.pendown()
    turtle.end_fill()

pass


def small_pink_triangle(x, y, a):
    #TODO (Vlad) Function, drawing small pink Triangle
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.color('pink')
    turtle.fillcolor('pink')
    turtle.begin_fill()
    b = (2 ** 0.5) * a
    turtle.forward(a)
    turtle.right(135)
    turtle.forward(b)
    turtle.right(135)
    turtle.forward(a)
    turtle.pendown()
    turtle.end_fill()

def main():
        turtle.color("red")
        big_red_triangle(-200, 100, 180)
        orange_square(0, 0, 180)
        blue_triangle(100, 0, 180)
        small_pink_triangle(300, 0, 180)
        green_parallelogram(0, -100, 180)
        small_purple_triangle(200, -100, 180)
        turtle.color("yellow")
        big_yellow_triangle(-100, 50, 180)
        turtle.done()

main()


