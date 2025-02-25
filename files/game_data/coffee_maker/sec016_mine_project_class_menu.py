from sec016_mine_data_project import MENU

class MenuCoffee():
    
    menu = MENU
    
    def __init__(self):
        self.avaliable_beverages = [beverage for beverage in MenuCoffee.menu]
    
    
    def chose_beverage_or_report(self):     
        """Show the user the options it can chose: A machine report, chose a beverage or stop using machine"""
        print(f'Do you want to print the machine report, chose a beverage or stop using the coffee machie?')
        print(' - [R] or [REPORT] for the machine report;\n - [N] or [END] to stop using the coffee machine;\n - Anything else to chose a beverage;')
        option = input('Input your choice: ').upper()
        if option == 'R' or option == 'REPORT':
            final_element_chosen = 'report'
        elif option == 'N' or option == 'END':
            final_element_chosen = 'end_machine'
        else:    
            final_element_chosen = 'beverage'
        return final_element_chosen

    def chose_beverage(self):    
        """If the user decides to chose a beverage it provides the user with its options"""
        valid_beverage = False
        avaliable_beverages_string = ''
        for i in range(len(self.avaliable_beverages)):
            if i == 0:
                avaliable_beverages_string = f'\nAvaliable beverages: {self.avaliable_beverages[i]}'
            else:
                avaliable_beverages_string += f'; {self.avaliable_beverages[i]}'
        print(f'\nChose the beverage you would like to order: {avaliable_beverages_string}')
        while not valid_beverage:
            final_beverage = input(' - Insert your choice: ').lower()
            if final_beverage not in self.avaliable_beverages:
                print('You inserted an invalid option. Please verify your beverage.')
            else:
                valid_beverage = True
        return final_beverage
