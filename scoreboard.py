from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.round_number = 1
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.print_round()

    def print_round(self):
        self.clear()
        self.write(f"Round {self.round_number}", align="center", font=FONT)

    def update_round(self):
        self.round_number += 1
        self.print_round()

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"GAME OVER", align="center", font=FONT)
