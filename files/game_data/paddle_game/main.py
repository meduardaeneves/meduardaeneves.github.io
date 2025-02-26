from class_screen import SetUpScreen
from class_paddle import Paddle
from class_scoreboard import Scoreboard
from class_ball import Ball
from variables import r_paddle_x_initial_position, l_paddle_x_initial_position, paddle_y_initial_position

import time

set_up_screen = SetUpScreen()
screen = set_up_screen.screen
screen.tracer(0)

set_up_screen.draw_middle_line()
ball = Ball()
r_paddle = Paddle(x_position=r_paddle_x_initial_position,y_position=paddle_y_initial_position,paddle_name='Right Paddle')
l_paddle = Paddle(x_position=l_paddle_x_initial_position,y_position=paddle_y_initial_position,paddle_name='Left Paddle')
r_scoreboard = Scoreboard(r_paddle)
l_scoreboard = Scoreboard(l_paddle)

screen.listen()
screen.onkey(fun=r_paddle.move_up_paddle,key='Up')
screen.onkey(fun=r_paddle.move_down_paddle,key='Down')
screen.onkey(fun=l_paddle.move_up_paddle,key='w')
screen.onkey(fun=l_paddle.move_down_paddle,key='s')
screen.update()

MAXIMUM_SCORE = 5

def verify_winning(scoreboard: Scoreboard):
    if scoreboard.score == MAXIMUM_SCORE:
        scoreboard.end_game()
        scoreboard.print_winner()
        return True
    return False

game_on = True
while game_on:
    
    time.sleep(.10)    
    screen.update()  
    
    ball.move_ball()
    collision_r = ball.verify_collision(r_paddle)
    collision_l = ball.verify_collision(l_paddle)
    collision = False
    
    if collision_r or collision_l:
        ball.rebounce()
        collision = True
    if not collision:
        if ball.xcor() > 0 and ball.xcor() >= r_paddle.xcor():
            l_scoreboard.update_score()
            if verify_winning(l_scoreboard):
                game_on = False    
            else:
                ball.reset_game()
        elif ball.xcor() < 0 and ball.xcor() <= l_paddle.xcor():
            r_scoreboard.update_score()
            if verify_winning(r_scoreboard):
                game_on = False    
            else:
                ball.reset_game()
screen.exitonclick()