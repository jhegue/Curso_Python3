"""
Split, Join, Enumerate em Python
* Split - Dividr uma string # str
* Join - Juntar uma lista # str
* Enumerate - Enumerar elementos da lista # list
"""

"""
string = "O Brasil é o país do futebol, o Brasil é penta."
lista1 = string.split(' ')
lista2 = string.split(',')

print('\n' + '-=' * 31 + '-\n')

print(lista1)

print('\n' + '-=' * 31 + '-\n')

print(lista2)

print('\n' + '-=' * 31 + '-\n')

for valor in lista1:
    print(valor)

print('\n' + '-=' * 31 + '-\n')

for valor in lista1:
    print(f'A palavra {valor} apareceu {lista1.count(valor)}x na frase')

print('\n' + '-=' * 31 + '-\n')

palavra = ''
contagem = 0
for valor in lista1:
    qtd_vezes = lista1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apreceu mais vezes é {palavra} ({contagem}x)')

print('\n' + '-=' * 31 + '-\n')

for valor in lista2:
    print(valor.strip().capitalize())

print('\n' + '-=' * 31 + '-\n')

string1 = 'O Bostil é Penta.'
lista = string1.split(' ')
string2 = ','.join(lista)
    
print(string1)
print(lista)
print(string2)

print('\n' + '--' * 31 + '-\n')

string = 'O Brasil é penta.'
lista = string.split(' ')

for indice, valor in enumerate(lista):
    print(indice, valor, lista[indice])

print('\n' + '--' * 31 + '-\n')


print('\n' + '--' * 31 + '-\n')

lista = [
    [0,'Luiz'],
    [1,'João'],
    [2,'Maria']
]

for indice, nome in lista:
    print(indice, nome)

print('\n' + '--' * 31 + '-\n')

lista = ['Luiz', 'João', 'Maria']

for indice, nome in enumerate(lista):
    print(indice, nome)

print('\n' + '--' * 31 + '-\n')

"""

print('\n' + '--' * 31 + '-\n')

lista = ['Luiz', 'João', 'Maria']

n1, n2, n3 = lista

print(n1)

print('\n' + '--' * 31 + '-\n')
