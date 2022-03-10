

def conversorMoneda(tipoMoneda, cantida):
    valor = 0
    if(tipoMoneda == 1):  # dolar
        valor = cantida/3.961
        return valor
    elif(tipoMoneda == 2):  # pesoMexicano
        valor = cantida/194
        return valor
    elif(tipoMoneda == 3):  # euro
        valor = cantida/4.507
        return valor
    elif():
        print('error 404')


if __name__ == '__main__':
    resultado = 0.0
    cantida, aux = '', ''

    print('welcome to conversor the money')
    while True:
        tipoMoneda = int(input(
            'Elija el tipo de moneda \n 1.dolar\n 2.pesoMexicano\n 3.euro \n Ingrese un numero: '))
        if(tipoMoneda > 0 or tipoMoneda < 4):
            break

    # while True:

    #     if cantida.isdigit():
    #         break

    cantida = int(input('Ingrese la cantidad en pesos Col a convertir:'))
    resultado = round(conversorMoneda(tipoMoneda, cantida))
    if tipoMoneda == 1:
        aux = 'DLL'
    elif tipoMoneda == 2:
        aux = 'MXP'
    elif tipoMoneda == 3:
        aux = 'EU'

    cadena = str(cantida)
    resultado1 = str(resultado)
    print('De pesos COL :'+cadena+' la conversion de ' +
          aux+' el resultado es: ' + resultado1)
