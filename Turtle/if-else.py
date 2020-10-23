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

elephant_weight = 1000
rat_weight = 10

if elephant_weight > rat_weight:
    square()
else:
    test_turtle.forward(100)

turtle.exitonclick()