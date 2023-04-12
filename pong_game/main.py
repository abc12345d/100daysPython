from turtle import Screen, Turtle
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball
import time

SCREEN_HEIGHT = 600
SCREEN_WIDTH = 800
ALIGNMENT = 'center'
FONT = ('Baskerville Old Face', 25, 'normal')
WINNER_SCORE = 3

def collide_horizontal_wall(ball, y_boundary):
    return ball.ycor() > y_boundary or ball.ycor() < -y_boundary

def collide_paddle(ball, paddle_left, paddle_right):
    return ball.distance(paddle_left) < 50 and ball.xcor() <= (paddle_left.xcor()+ 20) or ball.distance(paddle_right) < 50 and ball.xcor() >= (paddle_right.xcor()- 20)

# setup screen
screen = Screen()
screen.setup(width= SCREEN_WIDTH, height=SCREEN_HEIGHT)
screen.title("Ping Ping Pong")
screen.colormode(255)
screen.bgcolor("black")
screen.tracer(0)

# setup turtle for drawing separation line
turtle = Turtle()
turtle.speed(0)
turtle.hideturtle()
turtle.pensize(6)
turtle.pencolor("white")
turtle.penup()
start_y = SCREEN_HEIGHT // 2
turtle.goto(x = 0, y = start_y)

# draw separation line
while start_y > -(SCREEN_HEIGHT // 2):
    if turtle.isdown():
        turtle.penup()
    else:
        turtle.pendown()

    start_y -= 20
    turtle.goto(0, start_y)

# setup scoreboard
y_cor = (SCREEN_HEIGHT // 2) - 70
scoreboard_left = Scoreboard(x= -50, y = y_cor)
scoreboard_right = Scoreboard(x= 50, y= y_cor)

# setup paddle
x_cor = (SCREEN_WIDTH // 2) - 20
paddle_left = Paddle(x_cor = -x_cor)
paddle_right = Paddle(x_cor = x_cor - 10)

# setup ball
ball = Ball()

screen.listen()
is_game_on = True
y_boundary = (SCREEN_HEIGHT // 2) - 20
x_boundary = (SCREEN_WIDTH // 2) - 20

while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)

    screen.onkey(fun= paddle_left.move_up, key = "a")
    screen.onkey(fun= paddle_left.move_down, key = "s")
    screen.onkey(fun= paddle_right.move_up, key = "k")
    screen.onkey(fun= paddle_right.move_down, key = "l")

    if collide_horizontal_wall(ball, y_boundary):
        ball.bounce_y()

    if collide_paddle(ball,paddle_left,paddle_right):
        ball.bounce_x()

    ball.move()

    # detect collision with right wall
    if ball.xcor() > x_boundary:
        ball.reset_ball()
        screen.update()
        time.sleep(1)
        scoreboard_left.increase_score()

    # detect collision with left wall 
    elif ball.xcor() < -(x_boundary + 10):
        ball.reset_ball()
        screen.update()
        time.sleep(1)
        scoreboard_right.increase_score()

    if scoreboard_left.score >= WINNER_SCORE:
        is_game_on = False
        turtle.penup()
        turtle.goto(x = 0, y = 100)
        turtle.pencolor("blue")
        turtle.write(f"Player Left got {scoreboard_left.score} points first  ! The winner is Player Left!  ", align= ALIGNMENT, font= FONT)
    elif scoreboard_right.score >= WINNER_SCORE:
        is_game_on = False
        turtle.penup()
        turtle.goto(x = 0, y = 100)
        turtle.pencolor("blue")
        turtle.write(f"Player Right got {scoreboard_right.score} points first  ! The winner is Player Right!  ", align= ALIGNMENT, font= FONT)

screen.exitonclick()