import turtle
import random

wn=turtle.Screen()
wn.tracer(False)
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.title("pong")
wn.tracer(0)

#peddle_a
paddle_a=turtle.Turtle()
paddle_a.color("white")
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.goto(350,0)


#paddle b
paddle_b=turtle.Turtle()
paddle_b.penup()
paddle_b.color("white")
paddle_b.shape("square")
paddle_b.goto(-350,0)
paddle_b.speed(0)
paddle_b.shapesize(stretch_wid=5,stretch_len=1)

#ball
ball=turtle.Turtle()
ball.color("white")
ball.shape("square")
ball.goto(0,0)
ball.speed(0)
ball.penup()
ball.dx=0.1
ball.dy=0.1

def paddles_moving():

    def paddle_a_up():
        y=paddle_a.ycor()
        y +=20
        paddle_a.sety(y)

    #keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_up,"Up")


    #function                               1

    def paddle_a_down():
        y=paddle_a.ycor()
        y -=20
        paddle_a.sety(y)

    #keyboard binding
    wn.listen()
    wn.onkeypress(paddle_a_down,"Down")



    #function                             2

    def paddle_b_up():
        y=paddle_b.ycor()
        y +=20
        paddle_b.sety(y)

    #keyboard binding
    wn.listen()
    wn.onkeypress(paddle_b_up,"w")


    #function                             3

    def paddle_b_down():
        y=paddle_b.ycor()
        y -=20
        paddle_b.sety(y)

    #keyboard binding
    wn.listen()
    wn.onkeypress(paddle_b_down,"s")
paddles_moving()

while True:
    wn.update()
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor()+ball.dx)
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor()>390:
        ball.sety(390)
        ball.goto(0,0)
        ball.dx *= -1
    if ball.xcor()<-390:
        ball.sety(390)
        ball.goto(0,0)    
        ball.dx *= -1  
    if 350>ball.xcor()> 340 and (paddle_a.ycor()+50>ball.ycor()>paddle_a.ycor()-50) :
        ball.dx *= -1

    if -350<ball.xcor() < -340 and (paddle_b.ycor()+50>ball.ycor()>paddle_b.ycor()-50) :
        ball.dx *= -1
