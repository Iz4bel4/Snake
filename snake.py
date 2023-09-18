from turtle import Turtle

STARTING_SEGMENT_X_POSITIONS = [0, -20, -40]
STARTING_SEGMENT_Y_POSITION = 0
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for segment_id in range(0, 3):
            self.add_segment(STARTING_SEGMENT_X_POSITIONS[segment_id], STARTING_SEGMENT_Y_POSITION)

    def add_segment(self, pos_x, pos_y):
        snake_segment = Turtle(shape='square')
        snake_segment.color('white')
        snake_segment.penup()
        snake_segment.goto(x=pos_x, y=pos_y)
        self.snake_segments.append(snake_segment)

    def extend(self):
        # add a new segment to the snake
        last_segment_position = self.snake_segments[-1].position()
        pos_x = last_segment_position[0]
        pos_y = last_segment_position[1]
        self.add_segment(pos_x, pos_y)

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
