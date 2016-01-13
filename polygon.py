'''
Author: Spencer Klinge
Date: 9/18/2015
Class: ISTA 130
Section Leader: Will Zandler

Description:

polygon(turtle, int, int):

draws any polygon with any number of sides at any length, a great amount of code 
reduction compared to writing induvidual square and triangle functions.

main():
draws the figure with the dimensions(100), the offset(20), and 
the orientation outlined in homework 2.

'''

#==========================================================
import turtle

def polygon(buddy, sides_number, side_length):
    for i in range(sides_number):
        buddy.forward(side_length)
        buddy.left(360/sides_number)

def main():
    length=100
    'draw pentagram'
    penta= turtle.Turtle()
    penta.setheading(180)
    for i in range(3):
        penta.pendown()
        polygon(penta, 5, length)
        penta.penup()
        penta.sety(penta.ycor()-20)
    penta.hideturtle()
    'draw triangle'
    tri= turtle.Turtle()
    tri.setheading(180)
    tri.forward(length)
    tri.setheading(60)
    for i in range(3):
        polygon(tri,3,length)
        tri.left(90)
        tri.penup()
        tri.forward(20)
        tri.right(90)
        tri.pendown()
    tri.hideturtle()
    'draw square'
    square= turtle.Turtle()
    square.setheading(30)
    for i in range(3):
        polygon(square,4,length)
        square.forward(20)
    square.hideturtle()

    input('Press enter to end.')  # keeps the Sturtle graphics window open

if __name__ == '__main__':
    main()
