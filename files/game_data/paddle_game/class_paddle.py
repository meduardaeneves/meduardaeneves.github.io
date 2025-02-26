from turtle import Turtle
from variables import PADDLE_WID_STRETCH, PADDLE_LEN_STRETCH, NORTH, max_height_turtle

class Paddle(Turtle):
    def __init__(self,x_position,y_position,paddle_name):
        super().__init__()
        self.penup()
        self.goto(x_position,y_position)
        self.color('white')
        self.shape('square')
        self.speed('fast')
        self.shapesize(stretch_wid=PADDLE_WID_STRETCH,stretch_len=PADDLE_LEN_STRETCH)
        self.setheading(NORTH)
        self.paddle_name = paddle_name

    def _validate_top_movement(self):
        top_coord = self.ycor() + 20*PADDLE_LEN_STRETCH/2
        if top_coord >= max_height_turtle:
            return False
        return True
    
    def _validate_bottom_movement(self):
        bottom_coord = self.ycor() - 20*PADDLE_LEN_STRETCH/2
        if bottom_coord <= (-1 * max_height_turtle):
            return False
        return True   
     
    def move_up_paddle(self):
        if self._validate_top_movement():
            self.forward(25)
    
    def move_down_paddle(self):
        if self._validate_bottom_movement():
            self.backward(25)