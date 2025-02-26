#SCREEN VARIABLES
#initial_wid and lenght --> the amount of 20px 
INITIAL_WID_STRETCH = 1
INITIAL_LEN_STRETCH = 1
INITIAL_20X20_SQUARE_AMOUNT_HEIGHT = 14
INITIAL_20X20_SQUARE_AMOUNT_WIDTH = 20

#define width and height in px:
width_screen_value = (20 * INITIAL_WID_STRETCH * INITIAL_20X20_SQUARE_AMOUNT_WIDTH) * 2
height_screen_value = (20 * INITIAL_LEN_STRETCH * INITIAL_20X20_SQUARE_AMOUNT_HEIGHT) * 2
max_width_turtle = int((width_screen_value)/2)
max_height_turtle = int((height_screen_value)/2)

TITLE_GAME = 'PONG GAME'
PACE_MOVEMENT = 20

#PADDLES VARIABLES
PADDLES_OFFSET = 30
r_paddle_x_initial_position = max_width_turtle - PADDLES_OFFSET
l_paddle_x_initial_position = - 1 * (max_width_turtle - PADDLES_OFFSET)
paddle_y_initial_position = 0
PADDLE_WID_STRETCH = 1
PADDLE_LEN_STRETCH = 5

#DIRECTIONS
SOUTH = 270
NORTH = 90
EAST = 0
WEST = 180