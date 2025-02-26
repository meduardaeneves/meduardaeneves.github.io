from turtle import Turtle
from variables import border_center_offset_position, NORTH,max_width_turtle
from typing import TYPE_CHECKING

TURTLE_PACE = 20
if TYPE_CHECKING:
    from class_car import Car

class MyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('white')
        self.penup()
        self.start_x = 0
        self.start_y = border_center_offset_position['bottom']
        self.setheading(NORTH)
        self.goto(x=self.start_x,y=self.start_y)
        self.positive_max_x_position = max_width_turtle - 20
        self.turtle_space_occupation()
           
    def move_up(self):
        if self.ycor() < -(self.start_y):
            self.forward(TURTLE_PACE)
            self.turtle_space_occupation()
            
    def move_down(self):
        if self.ycor() > self.start_y:
            self.backward(TURTLE_PACE)
            self.turtle_space_occupation()
    
    def move_right(self):
        if self.xcor() < self.positive_max_x_position:
            new_x = self.xcor() + TURTLE_PACE
            self.goto(x=new_x,y=self.ycor())
            self.turtle_space_occupation()
    
    def move_left(self):
        if self.xcor() > - (self.positive_max_x_position):
            new_x = self.xcor() - TURTLE_PACE
            self.goto(x=new_x,y=self.ycor())
            self.turtle_space_occupation()
    
    def verify_toutch_with_car(self,car: 'Car'):
        verify_y = self.turtle_ycor_range[1] >= car.car_ycor_range[0] and self.turtle_ycor_range[0] < car.car_ycor_range[1]
        verify_x = self.turtle_xcor_range[1] >= car.car_xcor_range[0] and self.turtle_xcor_range[0] <= car.car_xcor_range[1]
        if verify_y and verify_x:
            # print('Encontrei o carro')
            return True

    def turtle_space_occupation(self):
        self.turtle_ycor_range = [self.ycor()-10,self.ycor()+10]
        self.turtle_xcor_range = [self.xcor()-10,self.xcor()+10]
        # print(f'turtle {self.xcor()=}; range in x: {self.turtle_xcor_range}')
        # print(f'turtle {self.ycor()=}; range in y: {self.turtle_ycor_range}')
    
    def restart_game(self):
        self.goto(self.start_x,self.start_y)
        self.turtle_space_occupation()