import turtle as t
import os

# =======================================
#        Pong Game by Muskan Shaikh
#         A classic arcade game built
#         with Python and Turtle graphics
# =======================================

# Initialize scores
playerAscore = 0
playerBscore = 0

# Create a window
window = t.Screen()
window.title("The Pong Game")
window.bgcolor("black")  # Change the background color
window.setup(width=800, height=600)
window.tracer(0)

# Creating the left paddle
leftpaddle = t.Turtle()
leftpaddle.speed(0)
leftpaddle.shape("square")
leftpaddle.color("cyan")  # Change paddle color
leftpaddle.shapesize(stretch_wid=6, stretch_len=1)  # Increase paddle height
leftpaddle.penup()
leftpaddle.goto(-350, 0)

# Creating the right paddle
rightpaddle = t.Turtle()
rightpaddle.speed(0)
rightpaddle.shape("square")
rightpaddle.color("magenta")  # Change paddle color
rightpaddle.shapesize(stretch_wid=6, stretch_len=1)  # Increase paddle height
rightpaddle.penup()
rightpaddle.goto(350, 0)  # Fix the paddle position

# Code for creating the ball
ball = t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("yellow")  # Change ball color
ball.shapesize(stretch_wid=1.5, stretch_len=1.5)  # Increase ball size
ball.penup()
ball.goto(0, 0)  # Center the ball
ballxdirection = 0.4  # Increased speed
ballydirection = 0.4

# Code for creating pen for scorecard update
pen = t.Turtle()
pen.speed(0)
pen.color("white")  # Change pen color
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0    Player B: 0", align="center", font=('Arial', 24, 'normal'))

# Code for moving the left paddle
def leftpaddleup():
    y = leftpaddle.ycor()
    if y < 250:  # Prevent going out of bounds
        leftpaddle.sety(y + 20)  # Adjust paddle speed

def leftpaddledown():
    y = leftpaddle.ycor()
    if y > -240:  # Prevent going out of bounds
        leftpaddle.sety(y - 20)  # Adjust paddle speed

# Code for moving the right paddle
def rightpaddleup():
    y = rightpaddle.ycor()
    if y < 250:  # Prevent going out of bounds
        rightpaddle.sety(y + 20)  # Adjust paddle speed

def rightpaddledown():
    y = rightpaddle.ycor()
    if y > -240:  # Prevent going out of bounds
        rightpaddle.sety(y - 20)  # Adjust paddle speed

# Assign keys to play
window.listen()
window.onkeypress(leftpaddleup, 'w')
window.onkeypress(leftpaddledown, 's')
window.onkeypress(rightpaddleup, 'Up')
window.onkeypress(rightpaddledown, 'Down')

while True:
    window.update()

    # Moving the ball
    ball.setx(ball.xcor() + ballxdirection)
    ball.sety(ball.ycor() + ballydirection)

    # Border setup
    if ball.ycor() > 290:
        ball.sety(290)
        ballydirection *= -1
    if ball.ycor() < -290:
        ball.sety(-290)
        ballydirection *= -1

    if ball.xcor() > 390:  # Right wall
        ball.goto(0, 0)
        ballxdirection *= -1
        playerAscore += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(playerAscore, playerBscore), align="center", font=('Arial', 24, 'normal'))

    if ball.xcor() < -390:  # Left wall
        ball.goto(0, 0)
        ballxdirection *= -1
        playerBscore += 1
        pen.clear()
        pen.write("Player A: {}    Player B: {}".format(playerAscore, playerBscore), align="center", font=('Arial', 24, 'normal'))

    # Handling collisions with paddles
    if (340 < ball.xcor() < 350) and (rightpaddle.ycor() - 50 < ball.ycor() < rightpaddle.ycor() + 50):
        ball.setx(340)
        ballxdirection *= -1
        os.system("afplay paddle.wav&")

    if (-350 < ball.xcor() < -340) and (leftpaddle.ycor() - 50 < ball.ycor() < leftpaddle.ycor() + 50):
        ball.setx(-340)
        ballxdirection *= -1
        os.system("afplay paddle.wav&")
