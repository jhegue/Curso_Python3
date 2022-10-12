"""
For / Else em Python
"""

print('\n' + '-=' * 31 + '-\n')

variavel = ['Luiz Otávio', 'Cleiton', 'Mario']

for valor in variavel:

    print(valor)
    # break
    print(valor)

print('\n' + '-=' * 31 + '-\n')

for valor in variavel:
    if valor.startswith('C'):
        print('Começa com C', valor)
    else:
        print('Não começa com C', valor)

print('\n' + '-=' * 31 + '-\n')

comeca_com_c = False

for valor in variavel:
    if valor.startswith('C'):
        comeca_com_c = True

if comeca_com_c:
    print('Existe uma palavra que começa com C.')

else:
    print('Não existe uma palavra que comça com C.')

print('\n' + '-=' * 31 + '-\n')

for valor in variavel:
    if valor.lower().startswith('c'):
        continue
    print(valor)
else:
    print('Nao existe uma palavra que começa com C.')

print('\n' + '-=' * 31 + '-\n')
