from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x = -275, y = 265)
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.write(f"Level {self.level}", font= FONT)

    def increase_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(x = 0, y = 0)
        self.write("GAME OVER!", font= FONT, align= "center")

    def congratulation(self):
        self.goto(x = 0, y = 0)
        self.write("YOU WIN!", font= FONT, align= "center")