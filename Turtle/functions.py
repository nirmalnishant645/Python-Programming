import turtle

test_turtle = turtle.Turtle()

def square():
    test_turtle.forward(100)
    test_turtle.right(90)
    test_turtle.forward(100)
    test_turtle.right(90)
    test_turtle.forward(100)
    test_turtle.right(90)
    test_turtle.forward(100)

square()
test_turtle.forward(100)
square()

turtle.exitonclick()