# realizar la creacion del juego ahorcado
import random
posicion = list()
carater = ''


def espaciado(palabra):
    x = 0
    texto = ''
    espacios = len(palabra)
    while x != espacios:
        texto += '_'
        x = x+1
    return texto


def aletoriedadPalabras():
    palabras = list()
    palabras.append('perro')
    palabras.append('tortuga')
    palabras.append('caballo')
    palabras.append('leopardo')
    palabras.append('iguana')

    aletorio = random.randint(1, 5)
    return palabras[aletorio]


def evaluarCaracteres(carater, palabra, cadena):
    n, i = 0, 0
    while n != len(palabra):
        if (palabra[n] == carater[0]):
            posicion.append(n)
        n = n+1

    while i != len(posicion):
        char = list(cadena)
        char[posicion[i]] = carater[0]
        cadena = "".join(char)
        i = i+1

    del posicion[:]
    return cadena


def pista(palabra):
    if palabra == 'perro':
        print('Ayuda-> tener un sentido del olfato muy agudo. Tener un amplio espectro auditivo. ')
    elif palabra == 'tortuga':
        print(('Ayuda-> son un tipo de reptiles caracterizados por el sólido caparazón que protege sus órganos vitales del que emergen la cabeza, las patas y la cola.'))
    elif palabra == 'caballo':
        print('Ayuda-> herbívoro perisodáctilo de gran porte, y cuello largo y arqueado poblado por largas crines')
    elif palabra == 'leopardo':
        print('Ayuda-> mamífero carnívoro de la familia de los félidos. Al igual que tres de los demás félidos')
    elif palabra == 'iguana':
        print('Ayuda-> saurópsidos escamosos de la familia Iguanidae nativos de zonas tropicales')
    else:
        print('error 404')


if __name__ == '__main__':
    palabra = aletoriedadPalabras()
    cadena = espaciado(palabra)
    print('\n\twelcome the game ahorcado\n')
    pista(palabra)
    print('\n')

    while cadena != palabra:
        carater = input('ingrese una letra:')
        # validador
        while True:
            if carater.isalpha():
                break
            carater = input('ingrese caracter adecuado:')

        cadena = evaluarCaracteres(carater, palabra, cadena)
        print(cadena)
    print('\n\tFinal Game')
