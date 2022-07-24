import random
import os
H = [
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
|    | |
|    | |
----------
"""
]

H.reverse()


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
    vi = 6
    letra='0'
    
    while True:
        check = all(elem in set(ingresadas) for elem in set(palabra))

        if check or vi == 0 :                           ##Continuidad del juego
            criterio = False
            break

        os.system('clear')                              ##Limpiar la consola

        interface = ' '.join(['_' if i not in ingresadas else i for i in palabra])
        print('\n',interface,'\n')                      ##Imprime la palbra incognita
        
        print(H[vi])                                    ##Ilustracion 
        print(f'\nLetras ingresadas:\n{"-".join(sorted([x.upper() for x in ingresadas]))}\n')

        if letra not in palabra: vi-=1                  ##Restar vidas
        vidas= ['*' for _ in range(vi)]
        print(f'Vidas Restantes: {" ".join(vidas)}')    ##Muestra de vidas


        letra = input('Ingrese una letra : ')           ##Ingreso de letra

        
        ingresadas.append(letra)                        ##Se añade la letra a ingresadas[Array]
        
    os.system('clear')

    if vi > 0:
        print (f'\n {H[vi]}\n',f" GANASTEEEEEEEEEEEEEE\n\n  La palabra era {palabra}",'\n'*5)
    else:
        print(f'\n {H[0]}\nLa palabra era {palabra}\n\nllevabas : {interface}', '\n'*5)

if __name__ == '__main__':
    run()