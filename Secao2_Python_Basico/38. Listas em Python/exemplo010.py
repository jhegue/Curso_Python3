"""
Listas em Python
fatiamento
append, insert, pop, del, clear, extend, +
muin, max
range
"""

print('\n' + '-=' * 31 + '-\n')

#         0    1    2    3    4    5
lista = ['A', 'B', 'C', 'D', 'E', 10.5]

# lista[5] = 'Qualquer outra coisa.'

print(lista[0:3])

print('\n' + '-=' * 31 + '-\n')

print(lista[1:4])
print(lista[:3])  # Começa no primeiro indice e termina no 2
print(lista[2:])  # Começa no 2 e termina no ultimo indice
print(lista[::2])
print(lista[::-1])

print('\n' + '-=' * 31 + '-\n')

# l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l2)
# l3 = l1 + l2
# l1.extend(l2)
# l2.append('b')  # append adiciona mais um valor no final da lista

l2.insert(0, 'Banana')  # Insere um valor na lista com o indice
print(l2)

l2.pop()

# print(l1)
print(l2)
# print(l3)

print('\n' + '-=' * 31 + '-\n')

#     0  1  2  3  4  5  6  7  8
l4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l4)

l4.insert(0, 'Banana')
print(l4)

del(l4[0])  # exclui alguns registros
print(l4)

print(max(l4))
print(min(l4))

print('\n' + '-=' * 31 + '-\n')

l5 = list(range(0, 100, 8))
print(l5)

print('\n' + '-=' * 31 + '-\n')

soma = 0

for valor in l4:
    soma = soma + valor

print(soma)

print('\n' + '-=' * 31 + '-\n')

l6 = ['String', True, 10, -20.5]

for elem in l6:
    print(f'O tipo de elem é {type(elem)} e seu valor é {elem}')

print('\n' + '-=' * 31 + '-\n')

secreto = 'PYTHON'
digitadas = []
chances = 3

while True:

    if chances <= 0:
        print(f'Você perdeu!!! A palavra secreta era "{secreto}"')
        break

    letra = input('Dgite uma letra: ')

    if len(letra) > 1:
        print('\nAhhh isso não vale, digite apenas uma letra.')
        print('\n' + '-=' * 31 + '-\n')
        continue

    digitadas.append(letra)

    if letra in secreto:
        print(f'\nUHUULLL, a letra "{letra}" existe na palavra secreta.')

    else:
        print(f'\nAFFFzzz: a letra "{letra}" NÃO EXISTE na palavra secreta')
        digitadas.pop()

    secreto_temporario = ''

    for letra_secreta in secreto:
        if letra_secreta in digitadas:
            secreto_temporario += letra_secreta
        else:
            secreto_temporario += '_'

    if letra not in secreto:
        chances -= 1

    if secreto_temporario == secreto:
        print('\n' + '-=' * 31 + '-\n')
        print(
            f'Que legal, VOCÊ GANHOU!!! A palavra secreta era "{secreto_temporario}"')
        break
    else:

        print(f'A palavra secreta está assim: {secreto_temporario}')
        print(f'Você ainda tem {chances} chances.')
        print('\n' + '-=' * 31 + '-\n')


print('\n' + '-=' * 31 + '-\n')
