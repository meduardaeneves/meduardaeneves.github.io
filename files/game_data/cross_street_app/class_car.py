from turtle import Turtle
from variables import BORDER_CENTER_OFFSET, border_center_offset_position,WEST, max_width_turtle
import random

CAR_START_OFFSET_FROM_BORDER = 20
CAR_STRECH_WID = 1
CAR_STRECH_LEN = 2
INITIAL_MOVEMENT_STEP = 10

class Car(Turtle):
    def __init__(self,color):
        super().__init__()
        self.penup()
        self.color(color)
        self.minimum_y = (border_center_offset_position['bottom'] + BORDER_CENTER_OFFSET) + CAR_START_OFFSET_FROM_BORDER
        self.maximum_y = (border_center_offset_position['top'] - BORDER_CENTER_OFFSET) - CAR_START_OFFSET_FROM_BORDER
        self.shape('square')
        self.pencolor('white')
        self.setheading(WEST)
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.chose_position()
        self.car_space_occupation()
        self.movement_step = INITIAL_MOVEMENT_STEP
    
    offset_y = CAR_STRECH_WID*20/2
    offset_x = CAR_STRECH_LEN*20/2    
    
    def chose_position(self):
        y_position = random.randrange(self.minimum_y,self.maximum_y,20)
        x_position = random.randrange((-max_width_turtle+20),(max_width_turtle+20),20)
        self.goto(x_position,y_position)
       
    def car_space_occupation(self):
        self.car_ycor_range = [self.ycor()-Car.offset_y,self.ycor()+Car.offset_y]
        self.car_xcor_range = [self.xcor()-Car.offset_x,self.xcor()+Car.offset_x]
    
    def print_car_conf(self):
        print(f'Car {self.xcor()=}; range in x: {self.car_xcor_range}')
        print(f'Car {self.ycor()=}; range in y: {self.car_ycor_range}')
    
    def move_car(self):
        if self.car_xcor_range[1] < (-max_width_turtle):
            self.goto((max_width_turtle+Car.offset_x),self.ycor())            
        else:  
            self.forward(self.movement_step)
        self.car_space_occupation()
    
    def accelerate(self):
        self.movement_step *= 1.2
    
    def reset_acceleration(self):
        self.movement_step = INITIAL_MOVEMENT_STEP