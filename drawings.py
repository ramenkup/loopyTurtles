'''
Author: Spencer Klinge
Date:
Class: ISTA 130
Section Leader: Will Zandler

Description:
Rotating Star Chain

def shape(turtle, int)
This function uses a set of nested for loops to draw a chain of stars.

def rotated_shapes(turtle, int, int, int)
This function rotates the star chain

main():
sets the speed, constructs, and calls the methods.
'''
#==========================================================
import turtle
'star chain'
def shape(buddy, size):
    'chainloop'
    for i in range(8):
        buddy.penup()
        buddy.setx(buddy.xcor()+size)
        'star loop'
        for i in range (5):
            buddy.pendown()
            buddy.forward(size)
            buddy.left(144)
    buddy.setheading(0)

'starchain rotator'
def rotated_shapes(turt, size, number, angle):
    accu_angle=0
    'rotation loop'
    for i in range(number):
        accu_angle+=angle
        shape(turt, size)
        turt.setheading(accu_angle)

def main():
    don= turtle.Turtle()
    don.setx(-20)
    don.speed(0)
    rotated_shapes(don, 10, 85, 10)

    input('Press enter to end.')  # keeps the turtle graphics window open

if __name__ == '__main__':
    main()
