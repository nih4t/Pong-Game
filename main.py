from turtle import Screen
from paddle import Paddle
from ball   import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")

screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

ball = Ball()
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x_r()

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x_l()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()







screen.exitonclick()