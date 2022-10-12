"""
Operadores Relacionais - Aula 4

== igualdade
> maior que
>= maior que ou igual a
< menor que
<= menor que ou igual a
!= diferente
"""

num_1 = 2  # int
num_2 = 2  # int

var_1 = 'Luiz'
var_2 = 'Otávio'

expressao = (num_1 == num_2)

print('')
print('-=' * 31 + '-')
print('')

print(expressao)

print('')
print('-=' * 31 + '-')
print('')

nome = str(input('Qual o seu nome? '))
idade = int(input('Qual a sua idade? '))

# Limite para pegar empréstimo
idade_menor = 20
idade_maior = 30

print('')
print('-=' * 31 + '-')
print('')

if idade >= idade_menor and idade <= idade_maior:
    print('{n} pode pegar o empréstimo.'.format(n=nome))

else:
    print('{n} não pode pegar empréstimo'.format(n=nome))

print('')
print('-=' * 31 + '-')
print('')
