from turtle import Turtle


X_POSITION = [0, -20, -40]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.snake_segments = []
        self.creating_snake()
        self.head = self.snake_segments[0]


    def creating_snake(self):
        for snake_parts in range(0, 3):
            snake_segment = Turtle(shape='square')
            snake_segment.color('white')
            snake_segment.penup()
            snake_segment.goto(x=X_POSITION[snake_parts], y=0)
            self.snake_segments.append(snake_segment)

    def move(self):
        for segment_number in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[segment_number - 1].xcor()
            new_y = self.snake_segments[segment_number - 1].ycor()
            self.snake_segments[segment_number].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)