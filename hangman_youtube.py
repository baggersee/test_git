"""
PYTHON PROJECT: HANGMAN
VERSION 0.2

Version de youtube: ESTUDIAR SU CODIGO

Empieza con un banco de palabras en ingles

Resuelve una de mis mejoras del banco de palabras (con 'import')

Filtra las palabras segun tengan '-' o ' ' con una sintaxis para strings que no conocia

Da un comando ('join') para convertir de forma guay 'lists' en 'strings'

Hace una cosa rara para crear una lista en solo una linea de codigo

En conclusion: No tengo que agobiarme por no saber programar.
               Simplemente lo que pasa es que debo aprender más sintaxis

"""



import random as r

import string

# del archivo 'words.py', importamos la variable 'words'
# notar que no hace falta la extension '.py'
# esto es muy util!!!

from words import words 




#ahora creamos una funcion para filtrar las palabras conflictivas

def get_valid_words(words):
    
    word = r.choice(words) # dada una lista selecciona un item al azar
    
    space = ' '
    dash = '-'

    while space in word or dash in word: # esta sintaxis no la conocía
        
         word = r.choice(words)
         
    return word.upper()  # al final del dia, trabajaremos en mayusuculas

# necesitamos:
# 1) tener un track de las letras que YA hemos probado
# 2) tener un track de las letras que ya hemos acertado
# 3) implementar el criterio que decida qué letras son válidas y cuáles no
        
        
def hangman():
    
    word = get_valid_words(words) # ya tenemos nuestra palabra secreta
    
    #print(word)
    
    word_letters = set(word) # con esto obtenemos las letras que son validas
    
    alphabet = set(string.ascii_uppercase) # esto lo desconocia: simplemente una funcion más
                                           # ya tenemos todas las posibles letras, válidas o no
    
    used_letters = set() # inicializamos un conjunto vacio que se 
                         # irá llenando con las palabras que vayamos usando
    
    
    turns_left = 9
                         
    while len(word_letters) > 0 and turns_left >0 :
        
        
        print("You have " ,turns_left, "turns left and you have already used: "," ".join(used_letters))
        
        # el comando 'joint' es util para transofrmar una 'list' en un 'string'
        
        # ahora vamos a mostrar el estado actual de la palabra
        # esta sintaxis me parte la cabeza en dos:
        # (se aclara un poco si lo leo de derecha a izquierda)
            
        #word_state = [letter if letter in used_letters else '_' for letter in word]
        
        # yo lo haría asi (lo he comprobado y funciona):
        
        #"""
        word_state = []
        
        for letter in word:
            
            if letter in used_letters:
                
                word_state.append(letter)
                
            else:
                
                word_state.append("_")
        
        
        
        #""        
        # ahora mostramos en pantalla el estado de la palabra:
            
        print("Current word: "," ".join(word_state))
        
        
        
        user_letter = input("Guess a letter: ").upper() # el usuario introduce una letra
                                                        # sintaxis mas directa para ponerlo en MAYUS
        
        if user_letter in alphabet - used_letters:
            
            # conjunto de letras aun no usadas
            
            used_letters.add(user_letter) # en el manual lo similar seria el comando 'update'
            
            if user_letter in word_letters:
                
                word_letters.remove(user_letter) # cuando acertamos, quitamos esa letra
                                                 # ganaremos cuando lo vaciemos por completo
                                                
            else:
                
                turns_left = turns_left - 1
                
                print(f"The letter {user_letter} is not in the word ")
                                                    
        
        elif user_letter in used_letters:
            
            print("You have already used that character. Try again")
            
            
        else:
            
            # si llega aqui, es que lo que ha puesto no esta en el alfabeto
            
            print("The character you entered is not in the alphabet. Try again")
        
    
    # aqui llega si ganamos o perdemos
    
    
    if turns_left == 0:
        
        print("YOU LOST")

    else:
        
        print("YOU WIN")
    
hangman()
    
    
    
    
    
    
    
    
    
    
    
    
        
    
    
    
    
    
    
    
    