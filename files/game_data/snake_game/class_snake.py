from turtle import Turtle
import time
from class_screen import INITIAL_LEN_STRETCH, INITIAL_WID_STRETCH

NORTH = 90
SOUTH = 270
EAST = 0
WEST = 180

class Snake(Turtle):
    def __init__(self):
        super().__init__()
        self.complete_snake = []
        self.first_x_coord = 0
        self.first_y_coord = 0
        self.add_snake()
        self.head = self.complete_snake[0]
        self.continue_game = True
    
    def add_snake(self):
        turtle = Turtle('square')
        if len(self.complete_snake) != 0:
            self.first_x_coord = self.complete_snake[-1].xcor()
            self.first_y_coord = self.complete_snake[-1].ycor()
            turtle.color('lightgreen')               
        else:
            turtle.color('green')
        turtle.penup()
        turtle.shapesize(stretch_wid=INITIAL_WID_STRETCH,stretch_len=INITIAL_LEN_STRETCH)
        turtle.pencolor('darkgreen')
        turtle.speed(10)
        self.complete_snake.append(turtle)
        self.complete_snake[-1].goto(self.first_x_coord,self.first_y_coord)
    
    def move_snake(self):
        self.previous_x_coord = self.head.xcor()
        self.previous_y_coord = self.head.ycor()
        self.head.forward(20)  
        if len(self.complete_snake) > 1:
            for i in range(1,len(self.complete_snake)):     
                new_x_coord = self.previous_x_coord
                new_y_coord = self.previous_y_coord
                self.previous_x_coord = self.complete_snake[i].xcor()
                self.previous_y_coord = self.complete_snake[i].ycor() 
                self.complete_snake[i].goto(new_x_coord,new_y_coord) 
    
    def head_north(self):
        if self.head.heading() == SOUTH:
            self.continue_game = False
        else:
            self.head.setheading(NORTH)

    def head_south(self):
        if self.head.heading() == NORTH:
            self.continue_game = False
        else:
            self.head.setheading(SOUTH)
        
    def head_east(self):
        if self.head.heading() == WEST:
            self.continue_game = False
        else:
            self.head.setheading(EAST)
        
    def head_west(self):
        if self.head.heading() == EAST:
            self.continue_game = False
        else:
            self.head.setheading(WEST)
        

        