from turtle import Turtle
ALIGNMENT = align= "center"
FONT = ('Arial', 25, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("aquamarine")
        self.penup()
        self.hideturtle()
        self.setposition(0,270)
        self.score = 0
        self.highest_score = self.get_highest_score()
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}   Highest score: {self.highest_score}", align= ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()

    def get_highest_score(self):
        with open("data.txt") as file:
            highest_score = int(file.read())

        return highest_score
    
    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("data.txt", mode= 'w') as file:
                file.write(f"{self.score}")
            
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.color('red')
    #     self.setposition(x = 0, y = 0)
    #     self.write(f"Game over!", align= ALIGNMENT, font= FONT)