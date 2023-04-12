from turtle import Turtle, Screen
import random

def random_walk():
    degree = random.choice([0,90,180,270])
    jimmy.setheading(degree)
    jimmy.forward(25)

def draw_shape(no_of_sides):
    angle = 360 / no_of_sides
    for _ in range(no_of_sides):
        jimmy.forward(100)
        jimmy.right(angle)

def draw_spirograph(no_circles):
    degree = 360 / no_circles
    for i in range(no_circles):
        jimmy.pencolor(random_colour())
        jimmy.setheading(i * degree)
        jimmy.circle(100, steps=50)

def random_colour():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def move_forward():
    jimmy.forward(10)

def move_backward():
    jimmy.back(10)

def turn_clockwise():
    jimmy.right(15)

def turn_anticlockwise():
    jimmy.left(15)

def clear_drawing():
    jimmy.clear()
    jimmy.penup()
    jimmy.home()
    jimmy.pendown()

screen = Screen()
screen.colormode(255)
jimmy = Turtle()

# draw different shape
for i in range(3,11):
    jimmy.pencolor(random_colour())
    draw_shape(i)

## random walk
# jimmy.pensize(10)
# jimmy.speed(6)
# for _ in range(100):
#     jimmy.pencolor(random_colour())
#     random_walk()

# draw spirograph
# jimmy.speed(0)
# draw_spirograph(60)

# make an etch-a-sketch app
# screen.listen()
# screen.onkey(fun = move_forward, key = 'w')
# screen.onkey(fun = move_backward, key = 's')
# screen.onkey(fun = turn_clockwise, key = 'd')
# screen.onkey(fun = turn_anticlockwise, key = 'a')
# screen.onkey(fun = clear_drawing, key = 'c')

screen.exitonclick()
        


