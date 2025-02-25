class MachineReport():
    def __init__(self,resources):
        self.resources = resources
        
    def report(self):        
        """Prints the machine report"""
        element_string = ''
        for element in self.resources:
            if element == 'water' or element == 'milk':
                element_string += f'\n - {element.title()}: {self.resources[element]}ml'    
            elif element == 'coffee':
                element_string += f'\n - {element.title()}: {self.resources[element]}g'
            else:
                element_string += f'\n - {element.title()}: $ {self.resources[element]}'
        return f'\nResources avaliable:{element_string}'      