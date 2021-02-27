"""
EN ESTE SECRIPT ESTAN TODAS LAS PRUEBAS PARCIALES QUE HE USADO 
PARA EL PROGRAMA DE HANGMAN


"""
#%% PRUEBA DEL COMNANDO count
example = "Esto es una prueba"


def count_char(word,char):
    
    n = word.count(char)
    
    return n
    
N = count_char(example,'e')

print(N)


#%% PRUEBA DEL COMANDO find

place = example.find('g')

print(place)  # si no está, devuelve '-1'


#%% PRUEBA DE ENCONTRAR ELEMENTOS EN UNA LISTA UNA VEZ (PRESENTES O NO)

a = 'ventana'

a = list(a)


    
try:
        
    n = a.index('y') # 
        
    print(n)
    
except ValueError:
        
    n = -1
        
    print(n)

#%% PRUEBA PARA ENCONTRAR ELEMENTOS REPETIDOS EN UNA LISTA

a = 'parapetada en la casa'

n = 20

a = list(a)

ind = a.index('a')

print("\n",ind)

while ind != -1:
    
    try:
        
        ind = a.index('a',ind+1,n+1)
        
        print("\n",ind)
    
    except ValueError:
        
        ind = -1
        
        print("\n",ind)
        
# puedo ir encontrando los indices y sustituyendo.

#%% SINTAXIS CONFLICTIVA EN UNA LISTA

a = 'casa'

a = list(a)

letter = 'c'

i = a.index(letter)

#%% TEST SINTAXIS LIST PARA VER SI UN OBJETO PERTENECE A UNA LISTA


example = 'example'

example = list(example)

result = 'j' in example # sintaxis importante!!

print(result)


#%% PRUEBA DEL COMANDO string.ascii

import string

print(string.ascii_letters)

#%% PRUEBA DEL COMANDO 'join'

# comando para pasar de una lista a un string

example = 'example'

example = list(example)


example_str = "".join(example)

example_str_2 = " ".join(example)

example_str_3 = "-".join(example)

example_str_4 = "@".join(example)









