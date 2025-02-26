import random
import os

def chose_game_difficulty():
    """Allows the user to chose the dificulty of the game and return the number of guesses avaliable acording to game dificulty."""
    correct_answer = False
    while not correct_answer:
        dificulty = input('Chose the dificulty of the game. [easy] or [hard]: ').lower()
        possible_answers = ['easy','hard']
        if dificulty not in possible_answers:
            print('You chose an invalid option.')
        else:
            correct_answer = True
    if dificulty == 'easy':
        number_of_guesses = 10
    elif dificulty == 'hard':
        number_of_guesses = 5
    return number_of_guesses

def chose_valid_number():
    valid_range = False
    
    while not valid_range:
        valid_number = False
        while not valid_number:
            number_str = input('Chose a number between 0 and 100 (INT format): ')
            try:
                number_int = int(number_str)
                valid_number = True
            except:
                print(' -The number you entered is not a valid INT number.')
        if number_int < 0 or number_int > 100:
            print(' -The number you chose is out of range.')
        else:
            valid_range = True
    return number_int

def verify_number(right_number,my_guess):
    correct_or_wrong_number = False
    if my_guess == right_number:
        correct_or_wrong_number = True
        return  correct_or_wrong_number
    elif my_guess < right_number:
        print('Your guess is too low.')
    else:
        print('Your guess is to high.')
    return correct_or_wrong_number  

def guess_random_number():
    random_numer = random.randint(1,100)
    # print(f'Test: random number = {random_numer}')
    
    print(f'{14*'*'} WELCOME TO THE NUMBER GUESSING GAME {14*'*'}')
    print(f'{10*'*'} I AM THINKING OF A NUMBER BETWEEN 1 AND 100 {10*'*'}')

    number_guesses = chose_game_difficulty()
    game_ended = False
    while not game_ended:
        print(f'\nYou have {number_guesses} attempts remaining to guess the number.')

        number_chosen = chose_valid_number()
        win_or_lose_game = verify_number(random_numer,number_chosen)

        if win_or_lose_game == True:
            print(f'\nYou chose correct. YOU WIN. Correct number was "{random_numer}"')
            game_ended = True
        else:
            number_guesses -= 1
            if number_guesses > 0:
                print('Guess Again.')
            else:
                print(f'\nYou have run out of guesses. YOU LOSE. Correct number was "{random_numer}"')
                game_ended = True
    if input('Do you want to play again? [Y] for YES. Anything else for NO: ').upper() == 'Y':
        os.system('cls')
        guess_random_number()
    else:
        print('Jogo Encerrado.')
        
guess_random_number()