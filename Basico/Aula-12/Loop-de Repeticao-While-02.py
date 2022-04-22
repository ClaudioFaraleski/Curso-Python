'''
Nesse Modeulo vamos ver acumuladores de numeros dentro da expressão while

Veja o exemplo abaixo


Autor : Claudio Faraleski Junior
'''

contador = 0 # contador - voce pode dar o nome que quiser para variavel
acumulador = 0 # acumulador

while contador <= 20:
    print(contador,acumulador)


    acumulador = acumulador + contador  # acumula e soma
    contador = contador + 1
