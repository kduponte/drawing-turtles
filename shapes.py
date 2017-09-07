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

    bubbles = turtle.Turtle()
    bubbles.shape("turtle")
    bubbles.color("blue")
    bubbles.speed(1)

    bubbles.circle(50)
    bubbles.right(45)

    squirts = turtle.Turtle()
    squirts.shape("turtle")
    squirts.color("yellow")
    squirts.speed(1)

    for x in range(0,3):
        squirts.backward(120)
        squirts.right(-120)

    window.exitonclick()

draw_shapes()
