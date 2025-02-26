from class_screen import SetUpScreen
from class_border import Border
from class_turtle import MyTurtle
from class_car import Car
from class_scoreboard import ScoreBoard

from variables import border_center_offset_position, BORDER_CENTER_OFFSET
import time

set_up_screen = SetUpScreen()
screen = set_up_screen.screen
screen.tracer(0)

score = ScoreBoard()
# top_border_score = Border('top')
bottom_border = Border('bottom')
myTurtle = MyTurtle()

cars_list = []
cars_colors = ['red','blue','green','orange','purple']
for cars_chosen_color in cars_colors:
    for _ in range(4):
        car = Car(cars_chosen_color)
        cars_list.append(car)

screen.listen()
screen.onkey(fun=myTurtle.move_up,key='Up')
screen.onkey(fun=myTurtle.move_down,key='Down')
screen.onkey(fun=myTurtle.move_right,key='Right')
screen.onkey(fun=myTurtle.move_left,key='Left')
screen.update()

turtle_crash = False
game_on = True
top_border_limit = border_center_offset_position['top'] - BORDER_CENTER_OFFSET

while game_on:
    
    for car in cars_list:
        car.move_car()
    
    for cars in cars_list:
        turtle_crash = myTurtle.verify_toutch_with_car(cars)
        if turtle_crash:
            break
    
    if myTurtle.turtle_ycor_range[0] >= top_border_limit:
        score.add_score()
        myTurtle.restart_game()
        for car in cars_list:
            car.accelerate()
    
    if turtle_crash:
        score.end_game()
        game_on = False  
        
    screen.update()
    time.sleep(.15)
    
screen.exitonclick()