"""
Manipulando strings - Aula 6
* String indices
* Fatiamento de strings [inicio:fim:passo]
* Funções built-in len, abs, type, print, etc...
Essas funções podem ser usadas diretamente em cada tipo.

Você pode conferir tudo isso em:
 https://docs.python.org/3/library/stdtypes.html (tipos built-in)
 https://docs.python.org/3/library/functions.html (funções built-in)
"""

print('\n' + '-=' * 31 + '-\n')

# positivos       [012345678]
texto           = 'Python_s2'
# negativos      -[987654321]

print( texto[0])

print('\n' + '-=' * 31 + '-\n')

url = 'www.google.com.br/'

print( url[:-1])

print('\n' + '-=' * 31 + '-\n')

nova_string = texto[0:6]
print(nova_string)

print('\n' + '-=' * 31 + '-\n')

nova_string = texto[0::3]
print(nova_string)

print('\n' + '-=' * 31 + '-\n')

for letra in texto:
    print(letra)

print('\n' + '-=' * 31 + '-\n')
