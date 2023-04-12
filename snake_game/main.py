from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time 

screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("Greedy snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.1) # to control the speed of animation
    
    screen.onkey(fun= snake.left, key= "Left")
    screen.onkey(fun= snake.right, key= "Right")
    screen.onkey(fun= snake.up, key= "Up")
    screen.onkey(fun= snake.down, key= "Down")

    snake.move()

    # detect collisions with the food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()
        # append a segment to the snake
        snake.append_segment()

    # detect collisions with the wall
    if snake.head.xcor() >= 300 or snake.head.xcor() <= -300 or snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        # is_game_on = False
        scoreboard.reset()
        snake.reset()
    
    # detect collisions with tail
    if snake.is_collision_tail():
        # is_game_on = False
        scoreboard.reset()
        snake.reset()

screen.exitonclick()