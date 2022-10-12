"""
* Enumerate - Enumerar elementos da lista # list
"""

print('\n' + '--' * 31 + '-\n')

lista = [

    #    0      1       2
    ['Edu', 'João', 'Luiz'],        # 0
    ['Maria', 'Aline', 'Joana'],    # 1
    ['Helena', 'Ed', 'Lu'],         # 2

]

# print(lista[0][2])

'''
enumerada = enumerate(lista)
print(list(enumerada))
'''

"""
[ <-- Enumerate

     0  1
    (0, ['Edu', 'João', 'Luiz']), # 0
          0         1           2
    (1, ['Maria', 'Aline', 'Joana']), # 1
    (2, ['Helena', 'Ed', 'Lu']) # 2
]
"""

'''
print('\n' + '--' * 31 + '-\n')

enumerada = list(enumerate(lista))
print(enumerada[1][1][2])

print('\n' + '--' * 31 + '-\n')
'''

'''
for v1, v2 in enumerate(lista, 53):
    print(v1, v2)

for v1, v2 in enumerate(lista, 53):
    print(v1)    


print('\n' + '--' * 31 + '-\n')
'''

for v1 in enumerate(lista, 53):
    valor_enumerado, minha_lista = v1
    nome1, nome2, nome3 = minha_lista
    print(nome1, nome2, nome3)

print('\n' + '--' * 31 + '-\n')

