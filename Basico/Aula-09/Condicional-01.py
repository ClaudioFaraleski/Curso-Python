'''
Nesse Modulo vamos aprender um pouco mais sobre condicional usamos if e else no mulo anterior agora vamos implementar

o Elif = senão

vamos abordar alguns exemplos

preste atenção nos blocos onde cada bloco representa situaçoes verdadeiras e falsas aonde você vai conseguir
visualizar por blocos algumas situaçoes e veja o que sera impresso

Autor : Claudio Faraleski Junior

'''
print("Bloco 1",("#"*50))

if True:  # mudar expressaõ para true e false e veja os resultados
    print(' Expressão Verdadeira - Aplicação do "If" na Expressão')
elif False:
    print('Agora essa é Expressão Verdadeira')
else:
    print('Agora sou eu ')
print("Bloco 2",("#"*50))


if False:  # mudar expressaõ para true e false e veja os resultados
    print('Expressão Verdadeira Bloco 2')
elif True:
    print('Agora essa é Expressão Verdadeira Bloco 2 - Aplicação do "Elif" na Expressão')
else:
    print('Agora sou eu Bloco 2')

print("Bloco 3", ("#" * 50))

if False:  # mudar expressaõ para true e false e veja os resultados
    print('Expressão Verdadeira Bloco 3')
elif False:
    print('Agora essa é Expressão Verdadeira Bloco 3')
else:
    print('Agora sou eu Bloco 3 - Aplicação do "Else" na Expressão')

