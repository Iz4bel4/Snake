from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Courier', 18, 'normal')


class Scores(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 270)
        self.points_scored = -1
        self.scores_update()

    def scores_update(self):
        self.points_scored += 1
        self.clear()
        self.write(f'Scores: {self.points_scored}', move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('Game Over', move=False, align=ALIGNMENT, font=FONT)



