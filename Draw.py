import turtle

def draw_square():
    t = turtle.Turtle(shape="turtle")
    t.color("dodger blue")
    t.pensize(2)
    for i in range(4):
        t.forward(200)
        t.right(90)

def draw_circle():
    t = turtle.Turtle()
    t.color("lime green")
    t.pensize(3)
    t.circle(100)

def draw_triangle():
    t = turtle.Turtle()
    t.color("magenta")
    t.pensize(4)
    for i in range(3):
        t.backward(175)
        t.left(120)

def picasso():
    draw_board = turtle.Screen()
    draw_board.bgcolor("peach puff")

    draw_square()
    draw_circle()
    draw_triangle()

    draw_board.exitonclick()

picasso()
