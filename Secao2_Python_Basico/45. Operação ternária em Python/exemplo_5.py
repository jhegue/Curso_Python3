"""
Operador ternário em Python
"""

logged_user = True

print('\n' + '--' * 31 + '-\n')

'''
if logged_user:
    msg = 'Usuário logado.'

else:
    msg = 'Usuário precisa logar.'

print(msg)

print('\n' + '--' * 31 + '-\n')
'''

'''
msg = 'Usuário logado.' if (logged_user) else 'Usuário precisa logar.'

print(msg)

print('\n' + '--' * 31 + '-\n')
'''


#idade = 18

'''
if idade >= 18:
    print('Pode acessar.')

else:
    print('Não pode acessar.')

print('\n' + '--' * 31 + '-\n')
'''
'''
e_de_maior = (idade >= 18)
msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'

print(msg)

print('\n' + '--' * 31 + '-\n')
'''

idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('\n')
    print('Digite apenas números!!!')

else:
    print('')
    idade = int(idade)
    e_de_maior = (idade >= 18)
    msg = 'Pode acessar.' if e_de_maior else 'Não pode acessar.'

    print(msg)


print('\n' + '--' * 31 + '-\n')
