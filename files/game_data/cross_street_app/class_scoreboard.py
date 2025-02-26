from turtle import Turtle
from class_border import Border
from variables import max_height_turtle,max_width_turtle, BORDER_CENTER_OFFSET

OFFSET_HEIGHT = 45
OFFSET_WIDTH_SCORE = 60
ALIGN = 'center'
FONT = ('Arial',15,'bold')
FONT_END_GAME = ('Arial',25,'bold')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score = 0
        self._write_score()
        
    def _write_score(self):
        self.clear()
        self.goto((-max_width_turtle)+OFFSET_WIDTH_SCORE,(max_height_turtle-OFFSET_HEIGHT))
        self.write(arg=f'Score: {self.score}',move=False,align=ALIGN,font=FONT)
        self.forward(0)
    
    def add_score(self):
        self.score += 1
        self._write_score()
    
    def end_game(self):
        self.goto(0,max_height_turtle-55)
        self.write(arg=f'GAME OVER',move=False,align=ALIGN,font=FONT_END_GAME)
    