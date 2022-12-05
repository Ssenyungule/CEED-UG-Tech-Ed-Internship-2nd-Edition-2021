"""This is a classic game known as Ping-Pong or commonly referred
to as Pong. We used basic functions and no classes or OOP.
It was envisioned and created by 
CEED coding interns cohort sept-Nov 2021
Credit to @TokyoEdTech(twitter) at freeCodeCamp.org
"""
# we start by importing our turtle module and set up our game window

import turtle

win = turtle.Screen()
win.title("Ping-Pong by Ssenyungule, Akena,and Sovra")
win.bgcolor("green")
win.setup(width=800, height=600)
win.tracer(0)

#Let's set up our game objects
    #Bar A
bar_a = turtle.Turtle()
bar_a.speed(0)
bar_a.shape("square")
bar_a.color("white")
bar_a.shapesize(stretch_wid=5, stretch_len=1)
bar_a.penup()
bar_a.goto(-350,0)

    #Bar B
bar_b = turtle.Turtle()
bar_b.speed(0)
bar_b.shape("square")
bar_b.color("white")
bar_b.shapesize(stretch_wid=5, stretch_len=1)
bar_b.penup()
bar_b.goto(350,0)

    #Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("black")
ball.penup()
ball.goto(0,0)
#below here we're setting delta-value to aid ball move in x & y planes
ball.dx = 0.2
ball.dy = -0.2

#Setting up the Score board
    #Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align="center", font=("courier",24,"normal"))

# Score
score_a = 0
score_b = 0

#Let's get our Bars moving
    #we are going to define functions
def bar_a_up():
    y = bar_a.ycor()
    y += 20
    bar_a.sety(y)

def bar_a_down():
    y = bar_a.ycor()
    y -= 20
    bar_a.sety(y)

def bar_b_up():
    y = bar_b.ycor()
    y += 20
    bar_b.sety(y)

def bar_b_down():
    y = bar_b.ycor()
    y -= 20
    bar_b.sety(y)

    #keyboard binding
win.listen()
win.onkeypress(bar_a_up,"a")
win.onkeypress(bar_a_down,"z")
win.onkeypress(bar_b_up,"Up")
win.onkeypress(bar_b_down,"Down")

# main game loop; where all our needs go be put
while True:
    win.update()
    #Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #Border checking
    if ball.ycor() > 290:
        ball.sety(290)           #here we're setting up top and bottom borders
        ball.dy *= -1
    
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)           #here we're setting up right and left borders
        ball.dx *= -1
        score_a += 1   #this is to award score to Player A if ball falls offscreen at RHS
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier",24,"normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1   #this is to award score to Player B if ball falls offscreen at LHS
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("courier",24,"normal"))

    #Bar and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < bar_b.ycor() + 40 and ball.ycor() > bar_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
    
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < bar_a.ycor() + 40 and ball.ycor() > bar_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1