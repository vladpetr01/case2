import turtle



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
    turtle.right(45)
    turtle.fd(a)
    turtle.right(135)
    turtle.fd(b)
    turtle.right(45)
    turtle.fd(a)
    turtle.pendown()
    turtle.end_fill()

pass


def main():
    turtle.color("red")
    green_parallelogram(-200, 100, 180)



main()