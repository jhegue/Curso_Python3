"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

print('')
print('-=' * 31 + '-')
print('')

num1 = input('Digite um número inteiro: ')

print('')

try:
    num1 = int(num1)

    if num1 % 2 == 0:
        print('Este número é par!')

    elif num1 % 2 != 0:
        print('Este número é impar!')

    else:
        print('Erro no programa!')

except:
    print('           Digite apenas números inteiros!!!           ')

print('')
print('-=' * 31 + '-')
print('')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex.
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""

var = input('Que horas são?: ')

print('')
print('-=' * 31 + '-')
print('')

try:
    var = int(var)

    if var >= 0 and var <= 11:
        print('Bom Dia!')

    elif var >= 12 and var <= 17:
        print('Boa Tarde!')

    elif var >= 18 and var <= 23:
        print('Boa Noite!')

    elif var < 0 or var > 23:
        print('            Digite apenas números entre 0 e 23!!!            ')

    else:
        print('Erro no programa!')

except:
    print('           Digite apenas números inteiros!!!           ')

print('')
print('-=' * 31 + '-')
print('')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande".
"""

nome = input('Qual é o seu primeiro nome? ')

print('')
print('-=' * 31 + '-')
print('')

qtde_nome = len(nome)

if qtde_nome < 5:
    print('Seu nome é CURTO')

elif qtde_nome == 5 or qtde_nome == 6:
    print('Seu nome é NORMAL')

elif qtde_nome > 6:
    print('Seu nome é GRANDE')

else:
    print('Erro no programa!')

print('')
print('-=' * 31 + '-')
print('')
