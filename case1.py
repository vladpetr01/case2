#First case
# Developers:   Zemtseva A. (20%),
#               Petrov V. (60%),
#               . (30%)
import turtle




def square(x, y, a,):
    turtle.up()
    turtle.setposition(x, y)
    turtle.down()
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)
    turtle.forward(a)
    turtle.right(90)


def main():
    square(-200, 200,180)
    square(20,200, 180)
    square(20,-20, 180)
    square(-200,-20,180)
    turtle.done()

main()

