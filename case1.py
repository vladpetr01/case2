#First case
# Developers:   Zemtseva A. (35%),
#               Petrov V. (25%),
#               Daniel A. (35%)
import turtle
import math
k = int(input('Введите число от 1 до 9'))

def big_red_triangle(x, y, a) :
    #TODO (Nastya) Function, drawing big red triangle.
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


def small_purple_triangle(x, y, a):
    #TODO (Vlad) Function, drawing small purple triangle.
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



def big_yellow_triangle(x, y, a):
    #TODO (Nastya) Function, drawing big yellow triangle.
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



def green_parallelogram(x, y, a):
    #TODO (Vlad) Function, drawing green parallelogram.
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




def small_pink_triangle(x, y, a):
    #TODO (Vlad) Function, drawing small pink triangle.
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

def fish():
        # TODO (Nastya) Print a fish.
        turtle.left(180)
        turtle.color("red")
        green_parallelogram(-140, 140, 90)

        turtle.left(90)
        orange_square(-130, 135, 90)

        turtle.right(45)
        small_pink_triangle(-230, 130, 90)

        turtle.right(270)
        small_purple_triangle(-240, 40, 90)

        turtle.right(90)
        turtle.color("red")
        big_red_triangle(13, 318, 180)

        turtle.color("yellow")
        big_yellow_triangle(13, -48, 180)

        turtle.right(135)
        blue_triangle(115, 136, 90)

        turtle.done()


def human():
        # TODO (Nastya) Print a human.
        turtle.right(90)
        turtle.left(45)
        orange_square(-10, 270, 90)

        turtle.right(45)
        turtle.color("red")
        big_red_triangle(-50, 130, 180)

        turtle.left(90)
        green_parallelogram(-60, 130, 90)

        turtle.right(-45)
        turtle.color("yellow")
        big_yellow_triangle(28, -170, 180)

        small_pink_triangle(-220, -130, 90)

        turtle.right(225)
        blue_triangle(130, -190, 90)

        turtle.right(-90)
        small_purple_triangle(-35, -290, 90)

        turtle.done()


def rabbit() :
    # TODO (Nastya) Print a rabbit.
    turtle.left(180)
    green_parallelogram(-5, 190, 90)

    turtle.right(90)
    turtle.left(45)
    orange_square(40, 180, 90)

    turtle.right(180)
    turtle.color("red")
    big_red_triangle(-60, -50, 180)

    turtle.right(135)
    small_pink_triangle(15, -30, 90)


    turtle.right(45)
    turtle.color("yellow")
    big_yellow_triangle(-240, -60, 180)

    blue_triangle(-100, -242, 90)

    turtle.right(180)
    small_purple_triangle(-90, -240, 90)

    turtle.done()

def helicopter() :
    # TODO (Vlad) Print a helicopter.
    turtle.left(45)
    green_parallelogram(0, 100, 90)

    turtle.right(225)
    blue_triangle(-100, 190, 90)

    turtle.left(90)
    turtle.color("red")
    big_red_triangle(125, -35, 180)

    turtle.right(90)
    turtle.color("yellow")
    big_yellow_triangle(-138, -35, 180)

    turtle.left(90)
    small_purple_triangle(-85, -100, 90)

    turtle.left(90)
    small_pink_triangle(-155, -160, 90)

    orange_square(-190, -70, 90)


    turtle.done()


def ship() :
    # TODO (Vlad) Print a ship.
    turtle.right(45)
    orange_square(100, 0, 90)

    small_pink_triangle(30, -70, 90)

    turtle.left(90)
    blue_triangle(5, -230, 90)

    turtle.right(45)
    green_parallelogram(-5, -230, 90)

    turtle.right(180)
    turtle.color('red')
    big_red_triangle(95, 5, 180)

    turtle.left(45)
    turtle.color('yellow')
    big_yellow_triangle(-48, -115, 180)

    turtle.left(90)
    small_purple_triangle(-32, 134, 90)

    turtle.done()

def figure() :
    # TODO (Vlad) Print a figure.
    turtle.left(45)
    orange_square(47, -2, 90)

    turtle.right(90)
    small_pink_triangle(45, -6, 90)

    turtle.color('red')
    big_red_triangle(43, 3, 180)

    turtle.right(180)
    turtle.color('yellow')
    big_yellow_triangle(40, -2, 180)

    green_parallelogram(-85, -137, 90)

    turtle.right(135)
    small_purple_triangle(115, 67, 90)

    turtle.left(45)
    blue_triangle(178, -135, 90)

    turtle.done()
if k == 1:
    cock()
if k == 2 :
    happy_human()
if k == 3 :
    spaceship()
if k == 4 :
    human()
if k == 5 :
    rabbit()
if k == 6 :
    fish()
if k == 7 :
    ship()
if k == 8 :
    helicopter()
if k == 9 :
    figure()



