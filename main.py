from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()
screen.title("PONG GAME")
screen.setup(width=800, height= 600)
screen.bgcolor("black")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(fun = r_paddle.go_up, key= "Up")
screen.onkey(fun = r_paddle.go_down, key= "Down")
screen.onkey(fun = l_paddle.go_up, key= "w")
screen.onkey(fun = l_paddle.go_down, key= "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320 :
        ball.bounce_x()
        
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()   
    
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()






screen.exitonclick()