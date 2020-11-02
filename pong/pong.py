import turtle

wn = turtle.Screen()
wn.title("Pong by Robin")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


# paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.1
ball.dy = -0.1


# functions
def peddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def peddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def peddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def peddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# keyboard binding
wn.listen()
wn.onkeypress(peddle_a_up, "z")
wn.onkeypress(peddle_a_down, "s")
wn.onkeypress(peddle_b_up, "Up")
wn.onkeypress(peddle_b_down, "Down")

# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1


    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx += -1


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx += -1
