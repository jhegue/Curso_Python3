"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

print('')
print('-=' * 31 + '-')
print('')

nome = 'Luiz'
print(nome, type(nome))

print('')
print('-=' * 31 + '-')
print('')

nome = 'Luiz Otávio'
idade = 32
altura = 1.80
e_maior = idade > 18
peso = 80

print('Nome:', nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)

print('')
print('-=' * 31 + '-')
print('')

print(idade * altura)

imc = peso / (altura**2)

print('')
print('-=' * 31 + '-')
print('')

print('{} tem {} anos de idade e o seu imc é de {:.2f}'.format(nome, idade, imc))

print('')
print('-=' * 31 + '-')
print('')
