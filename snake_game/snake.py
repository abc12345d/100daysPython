from turtle import Turtle

DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        self.last_position = None

    def create_snake(self):
        start_x = 0
        for i in range(3):
            segment = Turtle(shape= "square")
            segment.penup()
            segment.color("white")
            segment.setposition(x = start_x, y = 0)
            start_x -= 20
            self.snake.append(segment)

    def append_segment(self):
        segment = Turtle(shape= "square")
        segment.penup()
        segment.color("white")
        segment.setposition(x = self.last_position[0], y = self.last_position[1])

        self.snake.append(segment)
    
    def reset(self):
        for segment in self.snake:
            segment.goto(1000,1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]
        self.last_position = None

    def is_collision_tail(self):
        for segment in self.snake[1:]:
            if self.head.distance(segment) <= 10:
                return True
        return False

    def move(self):
        self.last_position = self.snake[-1].pos()
        for i in range(len(self.snake) - 1, 0, -1):
            # set the position of i-th segment to the position of its previous segment
            new_pos = self.snake[i-1].position()
            self.snake[i].setposition(new_pos)

        self.head.forward(DISTANCE)

    def left(self):
        if self.head.heading() != RIGHT:
            # snake is not allowed to move in opposite direction
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            # snake is not allowed to move in opposite direction
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            # snake is not allowed to move in opposite direction
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            # snake is not allowed to move in opposite direction
            self.head.setheading(DOWN)


    

