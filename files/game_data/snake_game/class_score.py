from turtle import Turtle
from class_screen import SetUpScreen,INITIAL_LEN_STRETCH

FONT_STYLE = ('Arial',12,'bold')
ALIGN = 'center'

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        # self.goto(x=0,y=0)
        self.goto(x=0,y=(SetUpScreen().height_screen/2 - (INITIAL_LEN_STRETCH/2 + 25)))
        self.color('white')
        self.hideturtle()
        self.score = 0
        self.write(f'SCORE: {self.score}',move=False,font=FONT_STYLE,align=ALIGN)
    
    def add_score(self):
        self.clear()
        self.score += 1
        self.write(f'SCORE: {self.score}',move=False,font=FONT_STYLE,align=ALIGN)
    
    def game_over(self):
        self.goto(x=0,y=0)
        self.write('GAME OVER',font=FONT_STYLE,align=ALIGN)
        
        