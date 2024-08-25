from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Moves the ball based on its current x and y movement values."""
        x_pos = self.xcor()
        y_pos = self.ycor()
        self.goto(x_pos + self.x_move, y_pos + self.y_move)

    def bounce_y(self):
        """Reverses the ball's y direction."""
        self.y_move *= -1

    def bounce_x_l(self):
        """Reverses the ball's x direction to the left and increases its speed."""
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def bounce_x_r(self):
        """Reverses the ball's x direction to the right and increases its speed."""
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def reset_position(self):
        """Resets the ball to the center and reverses its x direction."""
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1
