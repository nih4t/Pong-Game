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
        x_pos = self.xcor()
        y_pos = self.ycor()


        self.goto(x_pos + self.x_move, y_pos + self.y_move)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x_l(self):
        self.x_move = (abs(self.x_move))
        self.move_speed *= 0.9

    def bounce_x_r(self):
        self.x_move = -(abs(self.x_move))
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0,0)
        self.x_move *= -1
        self.move_speed = 0.1
