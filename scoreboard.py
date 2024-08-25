from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        """Initialize the scoreboard with default settings."""
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        """Update the scoreboard display with the current scores."""
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 60, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 60, "normal"))

    def l_point(self):
        """Increase the left player's score by 1 and update the display."""
        self.l_score += 1
        self.update()

    def r_point(self):
        """Increase the right player's score by 1 and update the display."""
        self.r_score += 1
        self.update()
