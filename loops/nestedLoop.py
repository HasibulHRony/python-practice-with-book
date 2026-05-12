# nested loop and turtle
import turtle
turtle.shape("turtle")
turtle.speed(0)

for sidelength in range(50, 100, 10):
    print(sidelength)
    for i in range(4):
        turtle.forward(sidelength)
        turtle.left(90)

turtle.exitonclick()