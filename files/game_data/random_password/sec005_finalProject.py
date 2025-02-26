import random
import string

#listas com os elementos:
letters = list(string.ascii_lowercase)
letters_upper = list(string.ascii_uppercase)
letters.extend(letters_upper)
numbers = [str(numero) for numero in range(0,10)]
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

#criar funções:
#1- função que retorna a quantidade de elementos que eu quero para cada unidade
def receive_values(list_of_element, name_of_element):
    print(f'How many {name_of_element} would you like in your password?')
    element_wrong = True    
    while element_wrong == True:
        quanty_element = input(f'Quantity of {name_of_element} (1 - {len(list_of_element)}): ')
        try:
            quanty_element_int = int(quanty_element)
            if quanty_element_int < 1 or quanty_element_int > len(list_of_element):
                print('The value you chose is not in valid range.')
            else:
                element_wrong = False
        except:
            print('The value you chose is not a valid number.')
    return quanty_element_int

#2-Função para adicionar a qnt de elementos escolhidos para a uma lista de senha
def add_elements_to_password(list_to_add,list_to_extract,qnt_elements_to_add):
    for number in range(qnt_elements_to_add):
        index_letters = random.randint(0,(len(list_to_extract)-1))
        number = list_to_extract[index_letters]
        list_to_add.append(number)
    return list_to_add
    
print('Welcome to the PyPassword Generator!')
qnt_letters = receive_values(letters,'letters')
qnt_symbols = receive_values(symbols,'symbols')
qnt_numbers = receive_values(numbers,'numbers')

password_unshuffled = []
password_unshuffled = add_elements_to_password(password_unshuffled,letters,qnt_letters)
password_unshuffled = add_elements_to_password(password_unshuffled,symbols,qnt_symbols)
password_unshuffled = add_elements_to_password(password_unshuffled,numbers,qnt_numbers)

print(f'Password Unshuffled:\n{password_unshuffled}')
random.shuffle(password_unshuffled)
final_password = password_unshuffled
print(f'Password Shuffled:\n{password_unshuffled}')

final_password_str = ''
for word in final_password:
    final_password_str += word

print(f'Final password: {final_password_str}')



    