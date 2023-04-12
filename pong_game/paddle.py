from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor) -> None:
        super().__init__()
        self.x = x_cor
        self.penup()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len = 1 )
        self.pencolor("white")
        self.fillcolor("white")
        self.goto(x = self.x, y = 0)

    def move_up(self):
        if self.ycor() < 240:
            self.goto(x = self.x, y = self.ycor() + 20)

    def move_down(self):
        if self.ycor() > -240:
            self.goto(x = self.x, y = self.ycor() - 20)


        
        
