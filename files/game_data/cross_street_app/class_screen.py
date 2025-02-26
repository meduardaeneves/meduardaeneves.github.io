from turtle import Screen
from variables import TITLE_GAME, width_screen_value, height_screen_value, max_width_turtle,  max_height_turtle

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
