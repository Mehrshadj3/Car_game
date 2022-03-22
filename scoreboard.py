FONT = ("Courier", 24, "normal")
from turtle import Screen,Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color('black')
        self.update()


    def add_score(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.penup()
        self.goto(-235, 260)
        self.hideturtle()
        self.write(f'LEVEL: {self.level}', align='center', font=FONT)

    def game_is_over(self):
        self.color('black')
        self.hideturtle()
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)


