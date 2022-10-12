"""
Formatando valores com modificadores - Aula 5

:s - Texto (strings)
:d - Inteiros (int)
:f - Números de ponto flutuante (float)
:.(NÚMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

print('\n' + '-=' * 31 + '-\n')

num_1 = 1
print(f'{num_1:0>10}')

print('\n' + '-=' * 31 + '-\n')

num_2 = 1150
print(f'{num_2:0>10.2f}')

print('\n' + '-=' * 31 + '-\n')

nome = 'Luiz Otávio Miranda'

print(f'{nome:#^50}')

print('\n' + '-=' * 31 + '-\n')

print(nome.lower())  # tudo minusculo
print(nome.upper())  # tudo maiusculo
print(nome.title())  # Primeiras letras maiusculas

print('\n' + '-=' * 31 + '-\n')
