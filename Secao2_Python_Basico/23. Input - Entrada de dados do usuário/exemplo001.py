"""
Entrada de dados - Aula 3
"""

print('')
print('-=' * 31 + '-')
print('')

nome = input("Qual o seu nome? ")
idade = int(input("Qual a sua idade? "))
ano_nascimento = 2022 - idade

print('')
print('-=' * 31 + '-')
print('')

print('{n} tem {i} anos. {n} nasceu em {ano}' .format(n=nome, i=idade, ano=ano_nascimento))

print('')
print('-=' * 31 + '-')
print('')

numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite outro número: ') 
numero_2 = int(numero_2)

print('')
print('-=' * 31 + '-')
print('')

print(numero_1 + numero_2)

print('')
print('-=' * 31 + '-')
print('')