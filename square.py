import turtle

def draw_square():
    window = turtle.Screen()
    window.bgcolor("black")

    swimmy = turtle.Turtle()
    swimmy.shape("turtle")
    swimmy.color("green")
    swimmy.speed(1)

    swimmy.forward(100)
    swimmy.right(90)
    swimmy.forward(100)
    swimmy.right(90)
    swimmy.forward(100)
    swimmy.right(90)
    swimmy.forward(100)
    swimmy.right(90)

    window.exitonclick()

draw_square()
