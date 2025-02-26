from turtle import Screen, Turtle
from variables import TITLE_GAME, width_screen_value, height_screen_value, max_width_turtle,  max_height_turtle, SOUTH, PACE_MOVEMENT

class SetUpScreen():    
    def __init__(self):
        self.title = TITLE_GAME
        self.width_screen = width_screen_value
        self.height_screen = height_screen_value
        
        self.max_width_turtle = max_width_turtle
        self.max_height_turtle = max_height_turtle 
               
        self.screen = Screen()
        self.screen.setup(width=self.width_screen,height=self.height_screen)
        self.screen.title(self.title)
        self.screen.bgcolor('black')
    
    def draw_middle_line(self):
        middle_line = Turtle()
        middle_line.hideturtle()
        middle_line.speed('fastest')
        middle_line.penup()
        middle_line.goto(x=0,y=self.max_height_turtle)
        middle_line.setheading(SOUTH)
        middle_line.color('white')
        movement = 0
        while movement < self.height_screen:
            middle_line.forward(PACE_MOVEMENT)
            movement += PACE_MOVEMENT
            middle_line.pendown()
            middle_line.forward(PACE_MOVEMENT)
            movement += PACE_MOVEMENT
            middle_line.penup() 