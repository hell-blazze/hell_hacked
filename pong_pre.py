try:
    import turtle

    wn = turtle.Screen()
    wn.title("1 player pong by shashank")
    wn.bgcolor("black")
    wn.setup(width=800, height=600)
    wn.tracer(0)

    # Score
    score_a = 0

    # Paddle A
    paddle_a = turtle.Turtle()
    paddle_a.speed(0)
    paddle_a.shape("square")
    paddle_a.color("white")
    paddle_a.shapesize(stretch_wid=5, stretch_len=1)
    paddle_a.penup()
    paddle_a.goto(-350, 0)

    # Ball
    ball = turtle.Turtle()
    ball.speed(0)
    ball.shape("square")
    ball.color("white")
    ball.penup()
    ball.goto(0, 0)
    ball.dx = 1
    ball.dy = -1

    # Pen
    pen = turtle.Turtle()
    pen.speed(0)
    pen.color("white")
    pen.penup()
    pen.hideturtle()
    pen.goto(0, 260)
    pen.write("miss :0", align="center", font=("Courier", 24, "normal"))
    pen2 = turtle.Turtle()
    pen2.speed(0)
    pen2.color("white")
    pen2.penup()
    pen2.hideturtle()
    pen2.goto(290, 0)
    pen2.pendown()
    pen2.goto(290, 290)
    pen2.goto(290, -290)

    # Function
    def paddle_a_up():
        y = paddle_a.ycor()
        y += 30
        paddle_a.sety(y)


    def paddle_a_down():
        y = paddle_a.ycor()
        y -= 30
        paddle_a.sety(y)


    # Keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up, "Up")
    wn.onkeypress(paddle_a_down, "Down")

    # Main game loop
    while True:
        wn.update()

        # Move the ball
        ball.goto(ball.xcor() + ball.dx, ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1

        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        if ball.xcor() > 290:
            ball.dx *= -1

        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1
            pen.clear()
            score_a += 1
            pen.write("miss: {}  ".format(score_a), align="center", font=("Courier", 24, "normal"))

        # Paddle and ball collisions

        if (-340 > ball.xcor() > -350) and (
                paddle_a.ycor() + 60 > ball.ycor() > paddle_a.ycor() - 60):
            ball.setx(-340)
            ball.dx *= -1
except:
    print('tanks for playing')
