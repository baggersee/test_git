"""
PYTHON PROJECT: HANGMAN
VERSION 0.1

Posibles mejoras: hacerlo con strings en lugar de con listas para mejorar la presentacion
                  borrar la palabra que escoge el jugador 1 para que no se vea
                  quitar los espacios en blanco, si se mete una frase (*)
                  coger palabras al azar de una base de datos. SQOL?
                  dibujar al ahorcado
"""



#%% FASE 1: Pillamos la palabra

word = input("PLayer 1, please enter a word: ") # palabra objetivo

word = list(word) # la convierto en una lista 

#%% FASE 2: Contamos cuántas letras tiene


def counting_letters(x):  # cuenta las letras de 'word'
    
    counter = 0
    
    while x[counter:]:     # no entiendo por qué esto funciona
        
        # OJO QUE ESTO TAMBIEN CUENTA LOS ESPACIOS EN BLANCO
        
        counter = counter + 1
    
    return counter  


letter_number = counting_letters(word) # contamos

#%% FASE 3: Creamos la lista de gaps 

def emptying(n):  # devulve una lista con 'n' gaps
    
    gap = "_"
    
    empty = gap*n
    
    empty =  list(empty)
    
    return empty


empty_word = emptying(letter_number) # inicializamos los gaps
    
#%% FASE 4: Empieza el primer feedback

print("\nPlayer 2, get ready")
print("Here's the challenge:")
print("\n",empty_word)






#%% FASE 5: Comprobamos si una letra suministrada pertenece o no a la palabra y sustuimos


# para meter un limite de turnos, habra que introducir otro 'while'


limit = 2

turns_left = limit


    
    
while empty_word != word:
    
        
    guess = input("\nGuess a letter: ")
    
    #guess = str(guess)
    
    c = word.count(guess)  # usamos el comando 'count'
    
    if c == 0:
        
        turns_left = turns_left - 1
        
        if turns_left ==0:
            
            break
        
        else:
            
            print("\nYou missed. Try again")
        
            print("\nTurns left=",turns_left)
            
        
        
    else:
        

        ind = word.index(guess)
        
        empty_word[ind] = word[ind]
        
        
        while ind != -1:
            
            try:
                    
                ind = word.index(guess,ind+1,letter_number+1)
                
                empty_word[ind] = word[ind]
        
            
            except ValueError:
    
                
                ind = -1
                
        print(empty_word)
        print("\nTurns left=",turns_left)
        

if turns_left == 0:    
                
    print("")
    print("YOU LOST")
    
else:
    
    print("")
    print("YOU WIN")
   
    
        





"""

(*): simplemente una rutina que detecte los espacios en blanco en la palabra
suministrada 'word' y automaticamente los sustituya en la palabra vacia.


"""





    

