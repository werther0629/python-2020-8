import turtle
import time

alex = turtle.Turtle()
alex.color('red')
alex.pensize(5)

bill = turtle.Turtle()
bill.color('green')
bill.pensize(10)

time.sleep(1)
alex.forward(100)
alex.left(90)

bill.left(180)
bill.forward(100)
bill.right(90)

alex.forward(100)
alex.left(90)

bill.forward(100)
bill.right(90)

alex.forward(100)
alex.left(90)

bill.forward(100)
bill.right(90)

alex.forward(100)
alex.left(90)

bill.forward(100)
bill.right(90)

turtle.done()