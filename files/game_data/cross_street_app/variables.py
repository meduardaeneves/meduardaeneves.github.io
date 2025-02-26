#initial_wid and lenght --> the amount of 20px 
INITIAL_WID_STRETCH = 1
INITIAL_LEN_STRETCH = 1
INITIAL_20X20_SQUARE_AMOUNT_HEIGHT = 14
INITIAL_20X20_SQUARE_AMOUNT_WIDTH = 14

#define width and height in px:
width_screen_value = (20 * INITIAL_WID_STRETCH * INITIAL_20X20_SQUARE_AMOUNT_WIDTH) * 2
height_screen_value = (20 * INITIAL_LEN_STRETCH * INITIAL_20X20_SQUARE_AMOUNT_HEIGHT) * 2
max_width_turtle = int((width_screen_value)/2)
max_height_turtle = int((height_screen_value)/2)

TITLE_GAME = 'CROSS THE ROAD'

#borders positions
#OFSET POSITIONS
BORDER_CENTER_OFFSET = 40 
border_center_offset_position = {
    'top': max_height_turtle - BORDER_CENTER_OFFSET,
    'bottom':  - (max_height_turtle - BORDER_CENTER_OFFSET),
    'right': max_width_turtle - BORDER_CENTER_OFFSET,
    'left':  - (max_width_turtle - BORDER_CENTER_OFFSET),
}

#DIRECTIONS
SOUTH = 270
NORTH = 90
EAST = 0
WEST = 180