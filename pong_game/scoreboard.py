from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Baskerville Old Face', 50, 'normal')

class Scoreboard(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(x = x, y = y)
        self.pencolor("blue")
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(str(self.score), align= ALIGNMENT,font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
