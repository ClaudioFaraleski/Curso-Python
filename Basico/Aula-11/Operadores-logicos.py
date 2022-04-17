'''
Nesse modulo é um complemento do modulo anterior onde aprendemos operadores relacionais agora usaremos operadores
logicos onde vamos combinar com operadores relacionais

and = e
or = ou
not = não o inverso da expressão
veja no exemplo abaixo

sistema basico de login

Autor : Claudio Faraleski junior
'''

login = 'python' # crie uma entrada com input e crie outra variavel para armazenar usuario e senha e faça os testes
senha = 123

if login == 'python' and   senha == 123 :
    print('Acesso Liberado')

if not login: # quando a variavel estiver vazia ele entra nesse trecho de codigo usamos o not podemos usar laço
    #de repetição ate o usuario digitar corretamente vamos ver nos modulos seguintes
    print('Preencha o login ')
    if not senha:
        print('Preencha a senha ')


elif login != 'python' or senha != 123:
    # nesse trecho de codigo se colocarmos o else vai funcionar mais coloquei o elif so para vermos o que acontece mais
    # qualquer coisa que for  diferente do login e senha ele entra nesse trecho de codigo mais se colocarmos
    #else:
    #  print('acesso negado') vai funcionar faça o teste
    print('Acesso Negado ')
    print('PROGRAMA ENCERRADO')





