import random
import os
H = (
    """
 ------
|     |
|
|
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|
|
|
|
|
----------
"""
   ,
"""
 ------
|     |
|     0
|     +
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|    -+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|
|
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    |
|    |
----------
"""
    ,
"""
 ------
|     |
|     0
|   /-+-/
|     |
|     |
|    | |
|    | |
----------
"""
)


def listar(nombre):
    d = {'á':'a','é':'e','í':'i','ó':'o','ú':'u', 'ñ':'n'}
    pal = lambda o: ''.join([d[i] if (i in d.keys()) else i for i in o])

    with open(nombre, "r", encoding="utf-8") as f:
        words = [pal(line.strip("\n")) for line in f]
    return words

def obtener(lista):
    n = random.randint(0, len(lista))
    return lista[n]                           

def run():
    words = listar("./data.txt")
    palabra=obtener(words)

    ingresadas = []
    vi = 7
    letra='0'
    while True:
        check = all(elem in set(ingresadas) for elem in set(palabra))
        if check or vi == 0 :
            criterio = False
            os.system('clear')
            break
        os.system('clear')
        li = ' '.join(['_' if i not in ingresadas else i for i in palabra])
        print('\n',li,'\n')
        if letra not in palabra: vi-=1 
        vidas= ['*' for _ in range(vi)]
        
        # print(check)
        print(f'Vidas {" ".join(vidas)}')
        print(f'\nLetras ingresadas:\n{"-".join(sorted([x.upper() for x in ingresadas]))}\n')
        letra=input('Ingresa una letra: ')
        ingresadas.append(letra)
        # print(set(palabra))
        # print(set(ingresadas))
        
        
    if vi > 0:
        print ('\n',f"GANASTEEEE\n La palabra era {palabra}",'\n'*5)
    else:
        print(f'\nAhorcado :(\nLa palabra era {palabra}\nllevabas : {li}', '\n'*5)

if __name__ == '__main__':
    run()