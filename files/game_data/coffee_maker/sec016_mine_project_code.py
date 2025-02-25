import os

from sec016_mine_data_project import resources, MENU
from sec016_mine_project_class_report import MachineReport
from sec016_mine_project_class_menu import MenuCoffee
from sec016_mine_project_class_cointvalidation import CoinValidation
from sec016_mine_project_class_ingredients import CoffeIngredients

            
# initial_resources = resources
resources['Total amount inside machine'] = 0
continue_making_beverages = True

machine_menu = MenuCoffee()

while continue_making_beverages:
    my_choice = machine_menu.chose_beverage_or_report()

    if my_choice == 'report':
        my_report = MachineReport(resources)
        print(my_report.report())
        make_a_beverage = input('\nNow do you want to chose a beverage? [Y or YES] for YES or anything else to end machine: ').upper()   
        if make_a_beverage == 'Y' or make_a_beverage == 'YES':
            my_choice = 'beverage' 
        else:
            continue_making_beverages = False     
            
    if my_choice == 'end_machine':
        continue_making_beverages = False       
    elif my_choice == 'beverage':
        my_beverage = machine_menu.chose_beverage()
        my_beverage_class = CoffeIngredients(my_beverage,resources)  
        recursos_restantes, avaliable_resources = my_beverage_class.verify_valid_resources()
        
        if avaliable_resources:
            coint_validation = CoinValidation(my_beverage)
            valid_coint_transaction = coint_validation.buy_coffe()            
        
            if valid_coint_transaction:
                resources = recursos_restantes
                resources['Total amount inside machine'] += MENU[my_beverage]["cost"]
                              
        continue_using_machine = input('\nDo you want to continue using the machine? [Y or YES] for YES, or anything else for no: ').upper()
        if continue_using_machine == 'Y' or continue_using_machine == 'YES':
            os.system('cls')
        else:
            continue_making_beverages = False