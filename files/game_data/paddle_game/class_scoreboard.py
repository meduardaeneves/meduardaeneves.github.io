from turtle import Turtle
from variables import max_width_turtle, max_height_turtle
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from class_paddle import Paddle

FONT_STYLE = ('Arial',50,'bold')
FONT_STYLE_GAME_OVER = ('Arial',25,'bold')
FONT_STYLE_PADDLES_NAMES = ('Arial',15,'bold')

ALIGN = 'center'
SCORE_Y_POSITION_OFFSET = 100
NAME_Y_POSITION_OFFSET = 30

score_y_position = max_height_turtle - SCORE_Y_POSITION_OFFSET
score_positive_x_position = max_width_turtle/2
score_name_y_position = max_height_turtle - NAME_Y_POSITION_OFFSET

END_GAME_X_POSITION = 0
END_GAME_Y_POSITION = 0

class Scoreboard(Turtle):
    def __init__(self,paddle: 'Paddle'):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.paddle = paddle
        if self.paddle.xcor() > 0:
            self.score_x_position = score_positive_x_position
        else:
            self.score_x_position = -1 * (score_positive_x_position)
            
        self.score_y_position = score_y_position
        self.goto(x=self.score_x_position,y=self.score_y_position)
        self.color('white')
        self.write(self.score,move=False,font=FONT_STYLE,align=ALIGN)
        self._write_paddle_name()
    
    def _write_paddle_name(self):
        self.goto(self.score_x_position,score_name_y_position)
        self.write(self.paddle.paddle_name,move=False,font=FONT_STYLE_PADDLES_NAMES,align=ALIGN)
    
    def update_score(self):
        self.clear()
        self.score += 1
        self.goto(x=self.score_x_position,y=self.score_y_position)
        self.write(self.score,move=False,font=FONT_STYLE,align=ALIGN)
        self._write_paddle_name()

    def end_game(self):
        self.goto(x=END_GAME_X_POSITION,y=END_GAME_Y_POSITION)
        self.write('GAME ENDED!', move=False, font=FONT_STYLE_GAME_OVER,align=ALIGN)   
    
    def print_winner(self):
        self.goto(x=END_GAME_X_POSITION,y=END_GAME_Y_POSITION - 60)
        self.write(f'The winner was {self.paddle.paddle_name}', move=False, font=FONT_STYLE_GAME_OVER,align=ALIGN) 
        
        