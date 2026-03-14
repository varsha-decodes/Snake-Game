
from turtle import Turtle
INITIAL_COORDINATES = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.my_snake = []
        self.head = None

    def create_snake(self):
        for i in range(3):
            self.my_snake.append(Turtle("square"))
            self.my_snake[i].pu()
            self.my_snake[i].speed(9)
            self.my_snake[i].color("white")
            self.my_snake[i].goto(INITIAL_COORDINATES[i])
        self.head = self.my_snake[0]

    def extend(self):
        new_segment = Turtle("square")
        new_segment.pu()
        new_segment.speed(9)
        new_segment.color("white")
        xcor = self.my_snake[-1].xcor()
        ycor = self.my_snake[-1].ycor()
        new_segment.goto(xcor,ycor)
        self.my_snake.append(new_segment)

    def reset_my_snake(self):
        for segment in self.my_snake:
            segment.goto(2000,2000)
        self.my_snake.clear()
        self.create_snake()

    def move(self):
        # for every part of snake other than the first
        for index in range(len(self.my_snake) - 1, 0, -1):
            prev_x = self.my_snake[index - 1].xcor()
            prev_y = self.my_snake[index - 1].ycor()
            self.my_snake[index].goto(prev_x, prev_y)
        # command for what happens to the head?
        self.head.forward(MOVE_DISTANCE)
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading()!=RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
