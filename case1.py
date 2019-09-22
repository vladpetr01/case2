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
    turtle.fd(a)
    turtle.right(45)
    turtle.fd(b)
    turtle.right(135)
    turtle.fd(a)
    turtle.right(45)
    turtle.fd(b)
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


def cock() :
    # TODO (Alina) Print a cock.
    turtle.right(45)
    blue_triangle(-100, 200, 90)
    turtle.left(135)
    turtle.color("red")
    big_red_triangle(-10, 100, 180)
    orange_square(90, 10, 90)
    turtle.right(180)
    turtle.color("yellow")
    big_yellow_triangle(0, 0, 180)
    turtle.left(135)
    b = (2 ** 0.5) * 90
    c = b / 2
    small_pink_triangle((90 + c), (110 + c), 90)
    small_purple_triangle((20 + c), (-170 + c), 90)
    turtle.right(180)
    green_parallelogram(-190, 90, 90)

def happy_human() :
    # TODO (Alina) Print a happy human.
    turtle.right(45)
    orange_square(0, 280, 90)
    turtle.right(135)
    turtle.color("red")
    b = (2 ** 0.5) * 90
    big_red_triangle(-5, (270 - b), 180)
    turtle.left(180)
    turtle.color("yellow")
    big_yellow_triangle(5, (270 - b), 180)
    turtle.right(90)
    blue_triangle(5, (80 - 2 * b), 90)
    turtle.left(90)
    green_parallelogram(-5, (80 - b), 90)
    turtle.left(135)
    small_pink_triangle(-65, (-45 - 2 * b), 90)
    d = b * 2 / 3
    small_purple_triangle((95 + d), (70 - 2 * b), 90)


def spaceship() :
    #TODO (Alina) Print a spaceship.
    turtle.right(45)
    small_pink_triangle(0, 280, 90)
    turtle.left(225)
    b = (2 ** 0.5) * 90
    c = b / 2
    blue_triangle(c, (270 - c), 90)
    turtle.color("yellow")
    turtle.right(225)
    big_yellow_triangle((c - 5), (260 - c - b), 180)
    turtle.right(90)
    turtle.color("red")
    big_red_triangle((c - b), (250 - c - b - b), 180)
    orange_square((c + c - b - 5), (240 - c - c - b - b), 90)
    small_purple_triangle((c - b - 10), (230 - b - c - b - b), 90)
    green_parallelogram((c + 10), (240 - c - b - b), 90)

def main():

main()


