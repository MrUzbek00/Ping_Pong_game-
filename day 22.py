# Pong Game


from turtle import Turtle, Screen
from controller import Paddle
from ball import Ball
import time
from score import ScoreBoard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

l_paddle= Paddle(position=(-350, 0))
r_paddle= Paddle(position=(350, 0))
pong = Ball()
scoreboard = ScoreBoard() 


screen.listen()

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

game_is_on= True
while game_is_on:
    time.sleep(pong.move_speed)
    screen.update()
    pong.move()
    # Detect collision with the cieling, bottom
    
    if pong.ycor() > 280 or pong.ycor() < -280:
        print("collision")
       
        pong.bounce_y()
    
        # Detect collision with the paddle
        
    if pong.distance(r_paddle) < 50 and pong.xcor() > 320 or pong.distance(l_paddle) < 50 and pong.xcor()< -320:
        pong.bounce_x()
        # print("collied with the paddle")
        
          
    # Detecting if the right paddle  missed the ball
    if pong.xcor() > 380:
        pong.reset_position()
        scoreboard.l_point()
    # Detecting if the left paddle  missed the ball
    if pong.xcor() < -380:
        pong.reset_position()
        scoreboard.r_point()

        
        
        


        
       








screen.exitonclick()





