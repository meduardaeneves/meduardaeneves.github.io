from turtle import Turtle
from variables import width_screen_value, height_screen_value, border_center_offset_position, BORDER_CENTER_OFFSET

class Border(Turtle):
    def __init__(self,position):
        super().__init__()
        self.penup()
        self.position = position
        self.offset_limit = border_center_offset_position[self.position]
        if self.position == 'top' or self.position == 'bottom':
            x_coord = 0
            y_coord = self.offset_limit
            height_ajust = (2*BORDER_CENTER_OFFSET)/20
            width_ajust = (width_screen_value)/20
        elif self.position == 'right' or self.position == 'left':
            x_coord = self.offset_limit
            y_coord = 0
            height_ajust = height_screen_value/20
            width_ajust = (2*BORDER_CENTER_OFFSET)/20
        self.shapesize(stretch_wid=height_ajust,stretch_len=width_ajust)
        self.color('brown')
        self.shape('square')
        self.goto(x_coord,y_coord)
    