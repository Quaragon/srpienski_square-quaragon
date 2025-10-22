import turtle

def srpienski_square(size, n):
    # Implement the Srpienski square
    #owkie
    if n == 0:
        turtle.begin_fill()
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.end_fill()
        return

    srpienski_square(size/3, n-1)
    turtle.forward(size/3)
    srpienski_square(size / 3, n - 1)
    turtle.forward(size / 3)
    srpienski_square(size / 3, n - 1)
    turtle.forward(size / 3)
    turtle.left(90)
    turtle.forward(size / 3)
    srpienski_square(size / 3, n - 1)
    turtle.forward(size / 3)
    srpienski_square(size / 3, n - 1)
    turtle.forward(size / 3)
    turtle.left(90)
    turtle.forward(size / 3)
    srpienski_square(size / 3, n - 1)
    turtle.forward(size / 3)
    srpienski_square(size / 3, n - 1)
    turtle.forward(size / 3)
    turtle.left(90)
    turtle.forward(size / 3)
    srpienski_square(size / 3, n - 1)
    turtle.forward(size / 1.5)
    turtle.left(90)










    pass

