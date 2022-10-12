"""
Operadores Lógicos - Aula 4
and, or, not
in e not in
"""

print('')
print('-=' * 31 + '-')
print('')

a = 2
b = 3

if b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')

print('')
print('-=' * 31 + '-')
print('')

nome = 'Luiz Otávio'

if 'u' in nome:
    print('Existe a letra U no seu nome.')

print('')
print('-=' * 31 + '-')
print('')

usuario = str(input('Nome de usuário: '))
senha = str(input('Senha do usuário: '))

print('')
print('-=' * 31 + '-')
print('')

usuario_bd = 'luiz'
senha_bd = '123456'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')

print('')
print('-=' * 31 + '-')
print('')

num_1 = 0
num_2 = 0

if not num_1 != num_2:
    print('Retorno 1')

else:
    print('Retorno 2')

print('')
print('-=' * 31 + '-')
print('')
