import random
from turtle import Turtle
from class_screen import SetUpScreen, INITIAL_LEN_STRETCH, INITIAL_WID_STRETCH

class Fruit(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.shapesize(stretch_wid=INITIAL_WID_STRETCH,stretch_len=INITIAL_LEN_STRETCH)
        
    def move_fruit(self):
        x_fruit = random.choice(SetUpScreen().max_turtles_x_coordinates)
        y_fruit = random.choice(SetUpScreen().max_turtles_y_coordinates)
        self.speed(0)
        # self.teleport(x=x_fruit,y=y_fruit)    
        self.goto(x_fruit,y_fruit)
       
    