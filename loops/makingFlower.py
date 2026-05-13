import turtle
turtle.speed(0)

# turtle.shape("turtle")

for i in range(1, 37):
    for j in range(1, 5):
        turtle.forward(100)
        turtle.left(90)
    turtle.left(10)

turtle.exitonclick()