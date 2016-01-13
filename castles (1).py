'''
Author: Spencer Klinge
Date: 9/18/2015
Class: ISTA 130
Section Leader: Will Zandler

Description:
replaces the castles.py functions shape functions with a generic polygon one. it makes
the appropriate call adjustments in main. it then draws the example figure in the 
homework 2 outline.

'''

import turtle

def polygon(buddy, sides_number, side_length):
    for i in range(sides_number):
        buddy.forward(side_length)
        buddy.left(360/sides_number)



def house(a_turtle, size):
    '''Draw a simple house of the given size.'''
    polygon(a_turtle, 4, size)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    polygon(a_turtle, 3, size)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    return None

def castle(a_turtle, size):
    '''Draw a simple castle of the given size.'''
    polygon(a_turtle, 4, size)
    a_turtle.penup()
    a_turtle.backward(size * 0.25)
    a_turtle.left(90)
    a_turtle.forward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.forward(size * 0.5)
    house(a_turtle, size * 0.5)
    a_turtle.penup()
    a_turtle.backward(size * 0.75)
    a_turtle.left(90)
    a_turtle.backward(size)
    a_turtle.right(90)
    a_turtle.pendown()
    return None

#==============================================
def main():
    '''Draw the outlined castle.'''
    yertle = turtle.Turtle()
    yertle.speed(0)
    yertle.penup()
    yertle.backward(100)
    yertle.pendown()
    yertle.pencolor('dark slate grey')
    yertle.pensize(5)
    castle(yertle, 100)
    yertle.forward(100)
    yertle.right(180)
    castle(yertle, 100)
    yertle.right(180)
    castle(yertle, 100)
    yertle.forward(100)
    yertle.right(180)
    castle(yertle, 100)
    yertle.right(180)
    castle(yertle, 100)
    yertle.forward(100)
    yertle.right(180)
    castle(yertle, 100)
    yertle.right(180)
    castle(yertle, 100)
    yertle.forward(100)
    yertle.right(180)
    castle(yertle, 100)
    
    input('Enter to end')

if __name__ == '__main__':
    main()
