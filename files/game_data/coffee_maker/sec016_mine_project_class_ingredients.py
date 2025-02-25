from sec016_mine_data_project import MENU

class CoffeIngredients():
       
    def __init__(self,coffee, resources):
        self.coffee = coffee
        self.resources = resources
        self.coffe_ingredients = MENU[self.coffee] 
           
    def enouth_resources_coffe(self): #type:ignore
        """From the beverage chosen, it will compare it's ingredients with the list of existing resources, returning the remaning ingredients"""
        remaining_ingredients = {}
        for ingredient in self.resources:
            if ingredient in self.coffe_ingredients['ingredients']:
                remaining_ingredients[ingredient] = self.resources[ingredient] - self.coffe_ingredients['ingredients'][ingredient]
            else:
                remaining_ingredients[ingredient] = self.resources[ingredient]
        return remaining_ingredients

    def verify_valid_resources(self):
        """Return a list of the remaining resources and the validation to prepare the beverage.
        If there are insufficient resources, it will print its list and return the validation to continue as False."""
        resources = self.enouth_resources_coffe()
        avaliable_resources = True
        insufficient_resources_string = f'\nThere are no sufficient ingredients to make the beverage. Missing ingredients:'
        if resources['water'] < 0:
            missing_water = f'\n  - Water: {-resources['water']}ml.'
            avaliable_resources = False
        else:
            missing_water = ''
        if resources['milk'] < 0:
            missing_milk = f'\n  - Milk: {-resources['milk']}ml.'
            avaliable_resources = False
        else:
            missing_milk = ''
        if resources['coffee'] < 0:
            missing_coffee = f'\n  - Coffee: {-resources['coffee']}g.'
            avaliable_resources = False
        else:
            missing_coffee = ''
        if not avaliable_resources:
            insufficient_resources_string += f'{missing_water}{missing_milk}{missing_coffee}'
            print(insufficient_resources_string)
        else:
            print('There are sufficient ingredients to prepare your beverage.')        
        return resources, avaliable_resources    