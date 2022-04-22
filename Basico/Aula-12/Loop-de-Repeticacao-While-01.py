'''
Nesse Modulo vamos continuar nosse estudo com operador de repetição while

vamos ver o exemplo

nesse exemplo vamos usar expressão continue e break

vamos criar um simples algoritimo onde vamos criar sistema simples de cadastro onde ele coloca o nome e idade
se for menor não podera se cadastrar

Autor : Claudio Faraleski Junior
'''

while True: # Condição sempre verdadeira

    nome = input('Digite seu nome : ')
    idade = input('Digite sua Idade :')

    sair = input('Digite [s]air ou [c]continuar')

    if not idade.isnumeric(): # estamos validando se usuario digitou um numero
        print('Digite somente numero')
        continue # para ele continuar o programa
    idade = int(idade) # fazendo o Casting

    if sair == 's': # se usuario digitar s encerra o programa
        break # usamos o break para parar o programa

    if  idade < 18:
        print(f'Você tem {idade} anos .Menor de idade ! Desculpe você ainda não pode se cadastrar')
    else:
        print(f'Parabêns Voce ja tem {idade} anos . Você já pode se cadastrar ')
        cadastro = input('Digite o Curso :')
        area = input('Area de Interesse ')
        print("Cadastrado com sucesso")

print('Fim do Programa')

# use a imaginação tente criar outrar situações colocando em partica o que aprendemos




