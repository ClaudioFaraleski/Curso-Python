'''
Nesse Modeulo vamos usar expressão while para iterar com texto

Vamos ver no exemplo abaixo

Autor: Claudio Faraleski Junior
'''


texto = 'Curso de python'
tamanho_frase = len(texto)
cont = 0

while cont < tamanho_frase:
    print(texto[cont], cont)
    cont = cont + 1