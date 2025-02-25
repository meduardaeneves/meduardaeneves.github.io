from sec016_mine_data_project import MENU

class CoinValidation():
    coint_values = {
    'Penny': 0.01,
    'Nickel': 0.05,
    'Dime': 0.10,
    'Quarter': 0.25    
    }
       
    def __init__(self,beverage_chosen):
        self.beverage_chosen = beverage_chosen
        self.beverage_value = MENU[self.beverage_chosen]["cost"]
                           
    def insert_valid_int_amount_for_coint(self,type_coint):
        """Ask you to insert valid values for each type of coints"""
        valid_amount = False
        amount_coint_int = 0
        total_value = 0
        while not valid_amount:
            amout_coint = input(f' - How many {type_coint} (${CoinValidation.coint_values[type_coint]}) do you want to insert? ')
            try:
                amount_coint_int = int(amout_coint)
                total_value += (amount_coint_int * CoinValidation.coint_values[type_coint])
                valid_amount = True
            except:
                print('Insert a valid coint amount.')
        return total_value
    
    def coffe_insert_money(self):
        """Ask to pay for the coffee and return the total amount inserted in machine."""
        payment_total = 0
        print(f'Pay for your coffee. Total ${self.beverage_value}')
        for coint_type in CoinValidation.coint_values:
            payment_total += self.insert_valid_int_amount_for_coint(coint_type)        
        return round(payment_total,2)
    
    def buy_coffe(self):
        """With the total amount inserted in the machine, it validates the transaction"""
        amount_inserted_machine = self.coffe_insert_money()
        change = 0
        valid_transaction = True
        if amount_inserted_machine < self.beverage_value:
            print(f'The amout inserted is not sufficient to pay for the coffee. \n - Your beverage will be canceled and your money (${amount_inserted_machine}) returned.')
            valid_transaction = False
        elif amount_inserted_machine == self.beverage_value:
            print(f'Your coffee will be prepared now. You have inserted the right amount of money.\n - There will be no change.')
        else:
            change = amount_inserted_machine - self.beverage_value
            print(f'Your coffee will be prepared now. You have inserted ${amount_inserted_machine}, more than the right amount.\n - Your change will be ${round(change,2)}')
        return valid_transaction
