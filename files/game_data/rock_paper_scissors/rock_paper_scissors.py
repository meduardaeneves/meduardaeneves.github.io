import random

def play_game():
    print('Let´s play rock, papper scissors')
    print('Choose what you want to play:\n[0] Rock\n[1] Paper\n[2] Scissors')

    wrong_element = True
    elements_game = [[0,1,2],['Rock','Papper','Scissors']]

    while wrong_element:   
        element = input('Input your decision: ')
        if element == '0' or element =='1' or element == '2':
            element_int = int(element)
            wrong_element = False
        else: 
            print('You chose a wrong value. Please verify your answer')

    rock_paper_scissors_random = random.randint(0,2)

    print()
    
    pc_choice = f'PC´s Choice: {elements_game[1][rock_paper_scissors_random]}'
    user_choice = f'Your Choice: {elements_game[1][element_int]}'
    
    print(pc_choice)
    print(user_choice)

    comparison_element = ''

    def pc_wins(pc_element,your_element):
        comparison = f'{elements_game[1][pc_element]} beats {elements_game[1][your_element]}.'      
        result = 'YOU LOST!'
        return comparison, result
        
    def user_wins(pc_element,your_element):
        comparison = f'{elements_game[1][your_element]} beats {elements_game[1][pc_element]}.'      
        result = 'YOU WIN!'
        return comparison, result
        
    print('\nRESULT:')
    if element_int == rock_paper_scissors_random:
        result = 'The game is a tie!'
        # print('The game is a tie!')
    else:
        if element_int == 0:
            if rock_paper_scissors_random == 1:
                comparison_element, result = pc_wins(rock_paper_scissors_random,element_int)
            elif rock_paper_scissors_random == 2:
                comparison_element, result = user_wins(rock_paper_scissors_random,element_int)

        elif element_int == 1:
            if rock_paper_scissors_random == 0:
                comparison_element, result = user_wins(rock_paper_scissors_random,element_int)
            elif rock_paper_scissors_random == 2:
                comparison_element, result = pc_wins(rock_paper_scissors_random,element_int)

        elif element_int == 2:
            if rock_paper_scissors_random == 0:
                comparison_element, result = pc_wins(rock_paper_scissors_random,element_int)                
            elif rock_paper_scissors_random == 1:
                comparison_element, result = user_wins(rock_paper_scissors_random,element_int)                
                
    if len(comparison_element) > 0:
        print(f'{comparison_element}\n{result}')
    else:
        print(result)

play_game()