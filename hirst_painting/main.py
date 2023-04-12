from turtle import Turtle, Screen
import colorgram
import random

### extracts colours from image and 
### save a list of (r,g,b) tuples
extracted_colors = colorgram.extract("./images/Damien_hirst_dequalinium_painting.jpg", 30)

extracted_rgb = []
for color in extracted_colors:
    extracted_rgb.append(tuple(color.rgb))

# first four colours are too light
extracted_colors = extracted_colors[4:]

### modify the setting of screen
screen = Screen()
screen.colormode(255)
screen.screensize(400, 400)


### use turtle to create spot painting
jimmy = Turtle()
jimmy.penup()
start_y = -225
start_x = -225
jimmy.setposition(start_x, start_y)
jimmy.shape("circle")
jimmy.shapesize(outline=20)

for i in range(10):
    for _ in range(10):
        jimmy.pendown()
        jimmy.pencolor(random.choice(extracted_rgb))
        jimmy.stamp()
        jimmy.penup()
        if i % 2 == 0:
            jimmy.forward(50)
        else:
            jimmy.back(50)
        

    if i % 2 == 0:
        start_x = +225
    else:
        start_x = -225

    start_y += 50
    jimmy.setposition(start_x, start_y)
jimmy.hideturtle()
 

screen.exitonclick()
