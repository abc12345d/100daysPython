from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(500,400)
is_race_on = False
colour_list = ["red", "orange", 'yellow', 'green', 'blue', 'purple']

# get user's guess through message dialog
user_guess = screen.textinput(title= "Make your bet", prompt= "Who will win the race? Enter a colour: ")
if user_guess:
    is_race_on = True

start_y = 125
turtle_list = []
for i in range(len(colour_list)):
    turtle_instance = Turtle(shape="turtle")
    turtle_instance.color(colour_list[i])
    turtle_instance.penup()
    turtle_instance.setposition(x=-240, y=start_y)
    turtle_list.append(turtle_instance)
    start_y -= 50

while is_race_on:
    for turtle in turtle_list:
        if turtle.xcor() > 220:
            is_race_on = False

            if turtle.pencolor() == user_guess:
                print(f"You've won! The {turtle.pencolor()} turtle is the winner!")
            else:
                print(f"You've lost! The {turtle.pencolor()} turtle is the winner!")
            break

        turtle.forward(random.randint(1,10))


screen.exitonclick()
