from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        # self.shapesize(0.3, 0.3, 0.3)
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align="center", font=('Courier', 18, 'normal'))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, align="center", font=('Courier', 18, 'normal'))
