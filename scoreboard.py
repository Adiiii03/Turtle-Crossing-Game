from turtle import Turtle
FONT = ("Courier", 24, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.level = 1
        self.display_levels()

    def update_level(self):
        self.clear()
        self.level += 1
        self.display_levels()

    def display_levels(self):
        self.color("black")
        self.goto(-220, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.color("black")
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=FONT)
