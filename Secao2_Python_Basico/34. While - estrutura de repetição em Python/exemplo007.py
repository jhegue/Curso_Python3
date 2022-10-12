"""
while em Python - Aula 7
utilizado para realizar ações enquanto
uma condição for verdadeira.

Resuisitos: Entender condiç~ies e operadores
"""

# while True: # loop infinito
# 
#     print('\n' + '-=' * 31 + '-\n')
# 
#     nome = input('Qual o seu nome? ')
#     print(f'\nOlá {nome}!')
#     
#     print('\n' + '-=' * 31 + '-\n')
# 
# print('Não será executada.')

print('\n' + '-=' * 31 + '-\n')

x = 0

while x <= 10:
    print(x)
    x += 1

print('            Acabou          ')

print('\n' + '-=' * 31 + '-\n')

x = 0

while x < 10:
    if x == 3:
        x += 1
        continue  # break


    print(x)
    x += 1

print('            Acabou          ')

print('\n' + '-=' * 31 + '-\n')


x = 0 # coluna
while x < 10:
    
    y = 0 # linha
    
    while y < 5:
        print(f'({x}, {y})')
        y += 1
    x += 1

print('            Acabou          ')

print('\n' + '-=' * 31 + '-\n')

while True:
    print()
    num_1 = input('Digite um número: ')
    num_2 = input('Digite outro número: ')
    operador = input('Digite um operador: ')

    if not num_1.isnumeric() or not num_2.isnumeric():
        print('Você precisa digitar um número!!!')
        continue

    num_1 = int(num_1)
    num_2 = int(num_2)

    # + - / *

    if operador == '+':
        print(num_1 + num_2)

    elif operador == '-':
        print(num_1 - num_2)
    
    elif operador == '/':
        print(num_1 / num_2)
    
    elif operador == '*':
        print(num_1 * num_2)

    break

print('\n' + '-=' * 31 + '-\n')
