import turtle

def triangle_draw(side_length):
    turtle.speed(5)
    for i in range(3):
        turtle.forward(side_length)
        turtle.left(120)


triangle_draw(100)

turtle.exitonclick()