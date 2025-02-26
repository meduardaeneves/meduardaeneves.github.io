from class_fruit import Fruit
from class_snake import Snake
from class_screen import SetUpScreen
from class_score import Score
import time

screen_setup = SetUpScreen()
screen = screen_setup.screen
# print(screen_setup.width_screen)
# print(screen_setup.height_screen)
# print(screen_setup.max_turtles_x_coordinates)
# print(screen_setup.max_turtles_y_coordinates)
print(screen.setup())

fruit = Fruit()
snake = Snake()
score = Score()
fruit.move_fruit()

snake.continue_game = False
start_game = screen.textinput(title='Start Game',prompt='Press any key to start the game')

if start_game == '' or start_game != '':
    snake.continue_game = True
screen.tracer(0)

while snake.continue_game: 
    
    snake.move_snake()
    screen.update()
    time.sleep(0.08)  
      
    screen.listen()
    screen.onkey(fun=snake.head_north,key='Up')    
    screen.onkey(fun=snake.head_south,key='Down')    
    screen.onkey(fun=snake.head_east,key='Right')    
    screen.onkey(fun=snake.head_west,key='Left') 
    
    for snake_part in snake.complete_snake[1:]:
        if snake.head.distance(snake_part) < 15:
            snake.continue_game = False
            break 
    
    screen.update()
    time.sleep(0.08)
    
    if snake.head.xcor() > screen_setup.max_turtles_x_coordinates[0] or snake.head.xcor() < screen_setup.max_turtles_x_coordinates[-1] or snake.head.ycor() > screen_setup.max_turtles_y_coordinates[0] or snake.head.ycor() < screen_setup.max_turtles_y_coordinates[-1]:
        snake.continue_game = False
        break 
    
    if snake.head.distance(fruit) < 15:
        score.add_score()
        snake.add_snake() 
        fruit.move_fruit()
    
score.game_over()
screen.exitonclick()

