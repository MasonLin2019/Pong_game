from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 80, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.l_score = 0
        self.r_score = 0

        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.l_score, False, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, False, align=ALIGNMENT, font=FONT)

    def increase_lscore(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def increase_rscore(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
