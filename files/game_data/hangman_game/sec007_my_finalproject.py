import random
import string
from hangman_words import words_pt, words_en

# word_list = ['melancia','abacaxi','escola','zebra','creche','edificio','avenida']
word_list = words_pt
existing_letters = list(string.ascii_lowercase)
lives = 8
#TODO1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it
def complete_chosen_word(list_chosen_word_gaps):
    final_chosen_word = ''
    for word in list_chosen_word_gaps:
        final_chosen_word += word
    return final_chosen_word

rand_index = random.randint(0,(len(word_list)-1))
chosen_word = word_list[rand_index]
chosen_word_gaps = ['_' for _ in range(len(chosen_word))]
chosen_word_gaps_ensambled = complete_chosen_word(chosen_word_gaps)
   
# print(chosen_word)
# print(chosen_word_gaps)
print(f'CHOSEN WORD:  {chosen_word_gaps_ensambled} ({len(chosen_word_gaps_ensambled)} letters)')
print(f'Lives: {lives}\n') 
#TODO2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase
letters_guessed = set()

while lives > 0 and chosen_word_gaps_ensambled != chosen_word:
    guess_right = False
    while not guess_right:
        guess = input('Choose a letter: ').lower()
        if guess not in existing_letters:
            print('The chosen letter is not valid.')
        else:
            if guess in letters_guessed:
                print(f'You already chose this letter. Letters choosen: {letters_guessed}')
            else:
                letters_guessed.add(guess)
                print(f'Letters guessed: {letters_guessed}')
                guess_right = True 

    #TODO3 - Check if the letter the user guessed is one of the letters in the chosen_word. Print right if it is and wrong if not
    #TODO4 - REPLACE BLANKS WITH THE LETTERS
    if guess in chosen_word:
        print('You have chosen a letter within the word.')
        for i, letter in enumerate(chosen_word):
            if guess == letter:
                chosen_word_gaps[i] = guess
        chosen_word_gaps_ensambled = complete_chosen_word(chosen_word_gaps)   
    else:
        print('The letter is not in the word.')
        lives -= 1
    print(f'Word in the moment: {chosen_word_gaps_ensambled}. Remaining {lives} lives.\n')

#PRINT OUT FINAL GAME RESULT
if lives == 0 and chosen_word_gaps_ensambled != chosen_word:
    print(f'You ran out of lives and lost the game. Correct word: {chosen_word}')
if chosen_word_gaps_ensambled == chosen_word:
    print(f'You guessed the correct word "{chosen_word_gaps_ensambled}" and won the game')
