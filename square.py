#!/usr/bin/env python

import turtle


def quit():
    turtle.bye()

def square(t, x : float , y : float):

    t.penup()
    t.goto(x,y)
    t.pendown()

    for i in range(4):
        t.left(90)
        t.forward(100)




# create my main turtle
my_turtle =turtle.Turtle()
# tell the screen to listen for key events
turtle.Screen().listen()
# if the escape key is pressed exit
turtle.onkeypress(quit, key="Escape")
# enter main loop so window stays in view
square(my_turtle,-100,-100)
turtle.mainloop()
