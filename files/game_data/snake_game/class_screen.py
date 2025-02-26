from turtle import Screen

#initial_wid and lenght --> the amount of 20px 
INITIAL_WID_STRETCH = 1
INITIAL_LEN_STRETCH = 1
INITIAL_20X20_SQUARE_AMOUNT_HEIGHT = 14
INITIAL_20X20_SQUARE_AMOUNT_WIDTH = 14

class SetUpScreen():
    
    def __init__(self):
        self.width_screen = (20 * INITIAL_WID_STRETCH * INITIAL_20X20_SQUARE_AMOUNT_WIDTH) * 2
        self.height_screen = (20 * INITIAL_LEN_STRETCH * INITIAL_20X20_SQUARE_AMOUNT_HEIGHT) * 2
        
        self.max_width_turtle = int((self.width_screen)/2 - INITIAL_WID_STRETCH*20)
        self.max_height_turtle = int((self.height_screen)/2 - INITIAL_LEN_STRETCH*20) 
        
        self.max_turtles_x_coordinates = [self.max_width_turtle - x*20 for x in range(INITIAL_20X20_SQUARE_AMOUNT_WIDTH*2-1)]
        self.max_turtles_y_coordinates = [self.max_height_turtle - x*20 for x in range(INITIAL_20X20_SQUARE_AMOUNT_HEIGHT*2-1)]        
        
        self.screen = Screen()
        self.screen.setup(width=self.width_screen,height=self.height_screen)
        self.screen.title('The Snake Game')
        self.screen.bgcolor('black')
        
 
    
    
        

