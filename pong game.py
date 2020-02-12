try:
            import turtle

            sc = turtle.Screen()
            sc.title('game of pong by shashank')
            sc.bgcolor('black')
            sc.setup(width=1000, height=600)
            sc.tracer()
            score_a = 0
            score_b = 0

            # hitter 1
            hi = turtle.Turtle()
            hi.speed(0)
            hi.shape("square")
            hi.color('lightblue')
            hi.shapesize(stretch_wid=5, stretch_len=1)
            hi.penup()
            hi.goto(-450, 0)




            # hitter 2
            hii = turtle.Turtle()
            hii.speed(0)
            hii.shape("square")
            hii.color('cyan')
            hii.shapesize(stretch_wid=5, stretch_len=1)
            hii.penup()
            hii.goto(450, 0)



            #ball
            ball = turtle.Turtle()
            ball.speed(0)
            ball.shape("square")
            ball.color('cyan')
            ball.penup()
            x=4
            y=4





            # Pen
            pen = turtle.Turtle()
            pen.speed(0)
            pen.color("white")
            pen.penup()
            pen.hideturtle()
            pen.goto(0, 260)
            pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))
            pen2 = turtle.Turtle()
            pen2.speed(0)
            pen2.color("white")
            pen2.penup()
            pen2.hideturtle()
            penz=turtle.Turtle()
            penz.hideturtle()
            penz.color('white')
            penz.goto(0,300)
            penz.goto(0,-300)


            #functions
            def hi_up():
                y=hi.ycor()
                y+=20
                hi.sety(y)
            def hi_down():
                y=hi.ycor()
                y-=20
                hi.sety(y)
            def hii_up():
                y=hii.ycor()
                y+=20
                hii.sety(y)
            def hii_down():
                y=hii.ycor()
                y-=20
                hii.sety(y)
            def eeg():

                pen2.goto(0, 160)
                pen2.write(" THIS GAME IS CREATED BY SHASHANK HOPE YOU LIKE IT . ",
                          align="center", font=("bleeding cowboys", 12, "normal"))
            def egg():
                pen2.goto(0,-160)
                pen2.write("EMBRACE!!!! NO GAME NO LIFE ",align="center", font=("Blowbrush", 13, "normal"))



            #key board
            sc.listen()
            sc.onkeypress(hi_up,'w')
            sc.onkeypress(hi_down,'s')
            sc.onkeypress(hii_up,'Up')
            sc.onkeypress(hii_down,'Down')
            sc.onkeypress(turtle.done,'q')



            #main code
            while True:
                sc.update()

                ball.goto(ball.xcor()+x,ball.ycor()+y)
                # background restriction
                if  ball.ycor() >290 or ball.ycor()<-290:
                    y*=-1
                if ball.xcor()>480 :
                    ball.goto(0,0)
                    pen.clear()
                    score_a += 1
                    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

                if ball.xcor()<-480:
                    ball.goto(0,0)
                    pen.clear()
                    score_b += 1
                    pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
                # hitter restriction
                if (420<ball.xcor()  <440) and (hii.ycor() + 60 > ball.ycor() > hii.ycor() - 60):
                    ball.setx(340)
                    x *= -1


                if (-440<ball.xcor() <-420) and (hi.ycor() + 60 > ball.ycor() > hi.ycor() - 60):
                    ball.setx(-340)
                    x *= -1
                sc.onkeypress(eeg, 'e')
                sc.onkeypress(egg,'Tab')
except:
    print("Glad you like it !!!!!!!")
