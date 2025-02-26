from turtle import Turtle
from variables import max_height_turtle,max_width_turtle,EAST,WEST, NORTH, SOUTH
import random
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from class_paddle import Paddle

max_ball_positive_height = max_height_turtle - 15
HEADING_VARIATION_ANGLES = [-45,45]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('circle')
        self.speed('slowest')
        self.shapesize(stretch_len=1,stretch_wid=1)
        self.x_initial_position = 0
        self.y_initial_position = 0
        self.goto(self.x_initial_position,self.y_initial_position)
        self._chose_side_to_leave()
        self.initial_forward_step = 15
    
    def _chose_y_start_value(self):
        y_position = random.randrange(-max_ball_positive_height,max_ball_positive_height)
        self.goto(self.x_initial_position,y_position) 
        
    def _chose_side_to_leave(self):
        if self.xcor() == 0:
            side = random.choice([EAST,WEST])
        elif self.xcor() > 0:
            side = WEST
        elif self.xcor() < 0:
            side = EAST
          
        heading = side + random.randrange(HEADING_VARIATION_ANGLES[0],HEADING_VARIATION_ANGLES[1]) 
        self.setheading(heading)
    
    def _verify_ball_y_position(self):
        if self.ycor() > 0 and self.ycor() >= max_ball_positive_height:
            dif_angle = self.heading() - NORTH
            new_heading = SOUTH + -1*dif_angle 
            self.setheading(new_heading)    
        elif self.ycor() < 0 and self.ycor() <= -max_ball_positive_height:
            dif_angle = SOUTH - self.heading()
            new_heading = NORTH + dif_angle
            self.setheading(new_heading)       
    
    def _verify_y_collision(self,y_element_comparison):
        y_range = [(y_element_comparison-50),(y_element_comparison+50)]
        if self.ycor() >= y_range[0] and self.ycor() <= y_range[1]:
            return True
    
    def verify_collision(self,paddle: 'Paddle'):
        if paddle.xcor() > 0:
            if self.xcor() >= (paddle.xcor()-20):
                # print('oi direita')
                if self._verify_y_collision(paddle.ycor()):
                    # print('encontrei direita')
                    return True
        elif paddle.xcor() < 0:
            if self.xcor() <= (paddle.xcor()+20):
                # print('oi esquerda')
                if self._verify_y_collision(paddle.ycor()):
                    # print('encontrei esquerda')  
                    return True 
    
    def rebounce(self):
        self._chose_side_to_leave()
        self.initial_forward_step *= 1.1
    
    def reset_game(self):
        self.initial_forward_step = 15
        self._chose_side_to_leave()
        self._chose_y_start_value()
                
    def move_ball(self):
        self._verify_ball_y_position()
        self.forward(self.initial_forward_step)
