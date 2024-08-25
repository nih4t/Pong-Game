from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        """Initialize the paddle with a given position."""
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.position = position
        self.goto(position)

    def up(self):
        """Move the paddle up by 50 units."""
        if self.ycor() < 245:
            self.goto(self.xcor(), self.ycor() + 50)

    def down(self):
        """Move the paddle down by 50 units."""
        if self.ycor() > -245:
            self.goto(self.xcor(), self.ycor() - 50)
