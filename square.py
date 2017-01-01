import turtle

def draw_shapes():
    window = turtle.Screen()
    window.bgcolor("black")

    swimmy = turtle.Turtle()
    swimmy.shape("turtle")
    swimmy.color("green")
    swimmy.speed(1)

    for x in range(0,4):
        swimmy.forward(100)
        swimmy.right(90)

    window.exitonclick()

draw_shapes()
