import string

letras = list(string.ascii_lowercase)
adicional_elements = ['á','à','â','ã','é','è','ê','ó','ò','ô','õ','í','ì','î','ú','ù','û','ç']
letras.extend(adicional_elements)
print(letras)

def encode_list(skip_param):
    real_skip = skip_param % len(letras)
    new_letras_encode= []
    for i in range(len(letras)):
        skip_index = i+real_skip
        if skip_index < len(letras):
            new_letras_encode.append(letras[skip_index]) 
        else:
            new_index = skip_index - len(letras)
            new_letras_encode.append(letras[new_index])
    return new_letras_encode

def encode_or_decode_text(text,principal_list,secondary_list):
    new_message = ''
    convert = False
    for letter in text:
        if letter.isupper():
            convert = True
            letter = letter.lower()
        else:
            convert = False        
        if letter in secondary_list:
            for i, letra in enumerate(secondary_list):
                if letra == letter:
                    encoded_letter = principal_list[i]
                    if convert:
                        encoded_letter = encoded_letter.upper()    
            new_message += encoded_letter      
        else:
            new_message += letter
    return  new_message 


encode_decode_continue = True
options_encode_decode = ['encode','decode']
encode_or_decode = ''

while encode_decode_continue:
    while encode_or_decode not in options_encode_decode:
        print('Type "encode" to encrypt, type "decode" to decrypt: ')
        encode_or_decode = input('Type the chosen element: ').lower()
        if encode_or_decode not in options_encode_decode:
            print('Chose a valid option.')    
    
    message = input('Type the message: ')
    shift_number = int(input('Type the shift number: '))

    if encode_or_decode == 'encode':
        principal_list = encode_list(shift_number)
        secondary_list = letras        
    if encode_or_decode == 'decode':
        principal_list = letras
        secondary_list = encode_list(shift_number)
        
    new_message = encode_or_decode_text(message,principal_list,secondary_list)
    
    print(f'Here is the {encode_or_decode}d result: {new_message}')
       
    print('Would you like to continue?')
    continue_while = input('[y] for yes or any other element to quit: ').lower()
    if continue_while == 'y':
        encode_or_decode = ''
    else:
        encode_decode_continue = False
        

    