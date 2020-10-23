# When you don't know when to end the loop

import turtle

test_turtle = turtle.Turtle()

while test_turtle.distance(0,0) < 100:
    test_turtle.forward(10)

#To stop tkinter window from ending itself on its own
turtle.exitonclick()