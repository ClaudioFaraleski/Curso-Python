'''
Nesse Modulo vamos falar da entrada de dados ou seja usuario passa o valor digitado para que isso aconteça precisamos
usar uma função no python que se chama input() vamos ver no exemplo

para isso vamos criar uma variavel e apelidar ela
nome sera nossa variavel  e com isso vamos  armazenar o valor que usuario digitar

lembrando no modulo anterior tipos de variaveis estamos criando uma avriavel tipo string tudo que o usuario digitar
sera reconhecido pelo interpretador como texto mais se relembrar o modelo de casting podemos fazer a conversão ou
inicializar a entrada de dados com tipo de dados que queremos mais dependendo o que usuario digitar o programa pode
quebrar vamos corrigir esse erro no modulo de tratamento de exceções que vocês iram aprender logo mais então vamos
praticar o basico por enquanto vamos la

Autor :Claudio Faraleski Junior

'''

nome = input('Digite o Nome :')
print(nome)

idade = input('Digite sua idade :')
print(int(idade)) # fazendo Casting ou Convertendo str para int

ano = int(input('em que ano estamos no momento ? :'))# estamos definindo a variavel que ela sera tipo inteira
print(ano)

'''
faça alguns testes coloque valores tipo float dentro das variaveis inteiras e ve o que acontece 
sera que vai ser comlidado, vai aparecer algum erro , tente e pratique para que você consiga pegar o conceito e 
aplicar dentro dos seus proximos algoritimos 
'''