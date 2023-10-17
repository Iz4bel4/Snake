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
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.scores_update()

    def scores_update(self):
        self.points_scored += 1
        self.clear()
        self.write(f'Scores: {self.points_scored} High Score:{self.high_score} ', align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.points_scored > self.high_score:
            self.high_score = self.points_scored
            with open('data.txt', mode='w') as data:
                data.write(f'{self.high_score}')
        self.points_scored = -1
        self.scores_update()



