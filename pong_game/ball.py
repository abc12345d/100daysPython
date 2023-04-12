from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.pencolor("orange")
        self.fillcolor("orange")
        self.x_move = random.choice([1,-1])
        self.y_move = random.choice([1,-1])
        self.speed(0)
        self.move_speed = 0.005

    def move(self):
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move

        self.goto(x = x,y = y)

    def bounce_y(self):
        '''trigger when the ball hit the top wall or bottom wall'''
        self.y_move *= -1

    def bounce_x(self):
        '''trigger when the ball hit the left wall or right wall'''
        self.x_move *= -1
        # increase the moving speed of ball
        self.move_speed *= 0.6

    def reset_ball(self):
        self.goto(x=0, y=0)
        self.move_speed = 0.005
        self.x_move *= -1

        





