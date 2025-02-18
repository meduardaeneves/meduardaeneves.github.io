import random
import os
import copy
from sec011_mine_rules_project import rules, blackjack_intro

deck_of_cards_one_suit= ['A','2', '3', '4', '5', '6', '7', '8', '9', '10','J','Q','K']
suits = ['heart','diamond','club','spade']
complete_deck = {}

for suit in suits:
    complete_deck[suit] = copy.deepcopy(deck_of_cards_one_suit)    

def define_value_of_cards(deck_of_cards):
    """
    A Function to assign value to each card in the deck.
    It will return a dictionary where the keys are the card's name and the values are it's value in the blackjack game
    """
    value_of_cards = {}
    for card in deck_of_cards:
        if card == 'A':
            value_of_cards[card] = [1,11]
        elif card == 'J' or card == 'Q' or card == 'K':
            value_of_cards[card] = 10
        else:
            value_of_cards[card] = int(card)
    return value_of_cards       

value_of_cards = define_value_of_cards(deck_of_cards_one_suit)

def print_deck(deck_of_cards):
    """Function to print out the deck of cards before or after a card has been chosen from the deck"""
    print('DECK OF CARDS AVALIABLE:')
    for keys, values in deck_of_cards.items():
        print(f'Suit: {keys}- {len(values)} Cards avaliable: {values}')
    print()

def print_cards(list_of_cards):
    """Function to print in a F-String the cards own by a person. It prints out the card suit followed by its value"""
    total_of_cards = ''
    if len(list_of_cards) == 2 and isinstance(list_of_cards[0],str):
        total_of_cards += f'{list_of_cards[0]}: "{list_of_cards[1]}"'
    else:
        for i,cards in enumerate(list_of_cards):
            total_of_cards += f'{cards[0]}: "{cards[1]}"'
            if i < (len(list_of_cards)-1):
                total_of_cards += ' / '
    return  total_of_cards     

def pick_random_card_out_deck(deck_of_cards, number_cards_to_chose):
    """from a existing deck, it can pick various number of cards randomly and assignt it to a list of cards. It will also return the final deck, after these modifications."""
    cards = []
    for i in range(number_cards_to_chose):
        random_suit = random.choice(list(deck_of_cards.keys()))
        random_card = random.choice(deck_of_cards[random_suit])
        if number_cards_to_chose == 1:
            cards.append(random_suit)
            cards.append(random_card)
        else: 
            cards.append([random_suit,random_card])
        deck_of_cards[random_suit].remove(random_card)
    return cards, deck_of_cards   

def show_one_dealer_card(cards_dealer):
    """Choses, randomly a card from the dealers hand to show to the other player."""
    random_card = random.choice(cards_dealer)
    return random_card 

def final_sum_with_A(num_a_cards,actual_sum_withoud_a):
    """The value of A can be either 1 or 11. This function will define the value of A.
    If the person holds 1 A card, it will define it's value by analising the sum of the other cards, it they are greater then 10, A will be 1, otherwise it will be 11.
    If the person holds more de 1 A card, one will have value of 11, the others 1."""
    summatory = actual_sum_withoud_a
    if num_a_cards >= 2:
        for i in range(num_a_cards):
            if i == 0:
                summatory += value_of_cards['A'][1]
            else:
                summatory += value_of_cards['A'][0]
    elif num_a_cards == 1:
        if summatory > 10:
            summatory += value_of_cards['A'][0]
        else:
            summatory += value_of_cards['A'][1]
    return summatory    
               
def return_sum_of_cards(cards):
    """This function provides the sum of the cards in hold (Assisted by "final_sum_with_A function")."""   
    sum_withoud_A = []
    num_A_cards = 0
    num_cards = 0
    value = 0
    #If you only have 1 card, it will avaluate it's value here
    if len(cards) == 2 and isinstance(cards[0],str):
        num_cards += 1
        if cards[1] == 'A':
            num_A_cards += 1
        else:
            value = int(value_of_cards[cards[1]])
            sum_withoud_A.append(value)       
    #if you have more than one card, it will avaluate its value here.
    else:
        for card in cards:
            num_cards += 1
            if card[1] == 'A':
                num_A_cards += 1
            else:
                value = int(value_of_cards[card[1]])
                sum_withoud_A.append(value) 
    if num_A_cards > 0:
        final_summatory = final_sum_with_A(num_A_cards,sum(sum_withoud_A))    
    else: 
        final_summatory = sum(sum_withoud_A)
    
    return final_summatory, sum(sum_withoud_A), num_A_cards 
  
def continue_getting_cards(final_summatory, cards, sum_withoud_A,num_A_cards,deck_in_game,dealer=None):
    """This funcition allows either you or the dealer to get more cards. If the summatory of the cards equal or over 17, the dealer will stop getting cards. If your summatory is equal or over 17 and you wish to continue getting cards, it will ask if you are sure."""
    
    pick_other_card_conditional = True
    while pick_other_card_conditional:
        #Other_Card is a status if you want or not to pick other card
        #Confirmation is a status if you are or not sure to continue picking new card
        if dealer == 'dealer':
            if final_summatory < 17:
                other_card = 'Y'
                confirmation = 'Y'
            else:
                other_card = 'N'
        else:
            other_card = input('    - Do you want to pick other card? [Y] for YES or anything else for no: ').upper()
            if final_summatory < 17:
                confirmation = 'Y'
            else:
                confirmation = 'N'
        
        if other_card == 'Y':
            if confirmation != 'Y' and dealer != 'dealer':
                confirmation = input('  - Are you sure you want to pick other card? [Y] for YES or anything else for no: ').upper()    
            if  confirmation != 'Y':
                pick_other_card_conditional = False                
            else:
                    new_card, deck_in_game = pick_random_card_out_deck(deck_in_game, 1)
                    cards.append(new_card)
                    final_summatory, sum_withoud_A, num_A_cards = return_sum_of_cards(cards) 
                    if dealer != 'dealer':
                        #If not the dealer it will print the cards in hold and it's sum. If it is over 21 it will end the possibility of chosing another card.
                        print(f'YOUR CARDS - {print_cards(cards)}')                              
                        if final_summatory <= 21:
                            print(f'YOUR SOMMATORY WITHOUD "A" ({len(cards) - num_A_cards} CARDS): {sum_withoud_A}; Values of "A" ({num_A_cards} CARDS): {value_of_cards['A'][0]} or {value_of_cards['A'][1]}.')
                        else:
                            print(f'Your summatory ({final_summatory}) is over 21')
                            pick_other_card_conditional = False   
        else:
            pick_other_card_conditional = False            
    return final_summatory, cards, sum_withoud_A,num_A_cards,deck_in_game

def blackjack_winner(sum,num_of_cards):
    """Define the rules for a winning as BLACKJACK"""
    if sum == 21 and len(num_of_cards) == 2:
        return True

def define_winner(my_summatory,dealers_summatory,my_cards, dealers_cards):
    """Provides the winner of the game according to it's rulles."""
    maximum_sum = 21
    mine_dif  = maximum_sum - my_summatory
    dealer_dif  = maximum_sum - dealers_summatory
    comparing_sum = f'(Your Sum: {my_summatory} x Dealers Sum: {dealers_summatory})'
    
    mine_blackjack_result = blackjack_winner(my_summatory,my_cards)
    dealers_blackjack_result = blackjack_winner(dealers_summatory,dealers_cards)
        
    if mine_blackjack_result and not dealers_blackjack_result:
        return print(f'YOU ACHIVED A BLACKJACK AND WON!! {comparing_sum}')
    elif dealers_blackjack_result and not mine_blackjack_result:
        return print(f'THE DEALER ACHIVED A BLACKJACK. YOU LOST!! {comparing_sum}')    
    elif my_summatory > maximum_sum:
        return print(f'YOU LOST!! YOUR SUM WAS {my_summatory}. YOU WERE OVER THE MAXIMUM SUM ({maximum_sum})!')
    elif dealers_summatory > maximum_sum:
        return print(f'YOU WIN!! DEALERS SUM WAS {dealers_summatory}. DEALER WAS OVER THE MAXIMUM SUM ({maximum_sum})!')
    elif mine_dif == dealer_dif:
        if mine_blackjack_result and dealers_blackjack_result:
            return print(f'ITS A DRAW WITH TWO BLACKJACKs!! {comparing_sum}')    
        else:
            return print(f'ITS A DRAW!! {comparing_sum}')    
    elif my_summatory <= maximum_sum and mine_dif < dealer_dif:
        return print(f'YOU WIN!! {comparing_sum}')
    else:
        return print(f'YOU LOST!! {comparing_sum}')  

def blackjack():
    """Function of the game itself. Allows you to play it."""
    print(blackjack_intro)
    print(rules,'\n')
    deck_in_game = copy.deepcopy(complete_deck)

    dealers_cards, deck_in_game = pick_random_card_out_deck(deck_in_game, 2)
    dealer_random_card = show_one_dealer_card(dealers_cards)
    print(f'DEALERS FIRST CARD - {print_cards(dealer_random_card)}\n') 

    my_cards, deck_in_game = pick_random_card_out_deck(deck_in_game, 2)
    print(f'YOUR CARDS - {print_cards(my_cards)}')
    my_final_summatory, my_sum_withoud_A, my_num_A_cards = return_sum_of_cards(my_cards)     
    print(f'YOU SOMMATORY WITHOUD "A" ({len(my_cards) - my_num_A_cards} CARDS): {my_sum_withoud_A}; Values of "A" ({my_num_A_cards} CARDS): {value_of_cards['A'][0]} or {value_of_cards['A'][1]}.')
    
    my_final_summatory, my_cards, my_sum_withoud_A,my_num_A_cards,deck_in_game = continue_getting_cards(my_final_summatory, my_cards, my_sum_withoud_A,my_num_A_cards,deck_in_game)
    
    dealers_final_summatory, dealers_sum_withoud_A, dealers_num_A_cards = return_sum_of_cards(dealers_cards)
    dealers_final_summatory, dealers_cards, dealers_sum_withoud_A,dealers_num_A_cards,deck_in_game = continue_getting_cards(dealers_final_summatory, dealers_cards, dealers_sum_withoud_A,dealers_num_A_cards,deck_in_game,'dealer')
    
    print('\nRESULT:')
    print(f'DEALERS FINAL CARDS - {print_cards(dealers_cards)}')
    print(f'Dealers Final Sommatory: {dealers_final_summatory}')
    print(f'\nYOUR FINAL CARDS - {print_cards(my_cards)}.')
    print(f'Your Final Sommatory: {my_final_summatory}')

    define_winner(my_final_summatory,dealers_final_summatory,my_cards,dealers_cards)   
    
    continue_game = input('\nDo you want to play another game? [Y] for yes, other thing for no: ').upper()
    if continue_game == 'Y':
        os.system('cls')
        blackjack()
    else:
        return

blackjack()