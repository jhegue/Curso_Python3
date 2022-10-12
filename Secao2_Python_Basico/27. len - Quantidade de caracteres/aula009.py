
print('')
print('-=' * 31 + '-')
print('')

usuario = str(input('Digite seu usuário: '))
qtd_caracteres = len(usuario)

print('')
print('-=' * 31 + '-')
print('')

if qtd_caracteres < 6:
    print('Você precisa digitar pelo menos 6 caracteres')

else:
    print('Você foi cadastrado no sistema')

print('')
print('-=' * 31 + '-')
print('')

string1 = str(input('Digite alguma coisa: '))
string2 = str(input('Digite outra coisa: '))

print('')
print('-=' * 31 + '-')
print('')

print('A quantidade total de caracteres digitados foi {0}' .format(
    len(string1) + len(string2)))

print('')
print('-=' * 31 + '-')
print('')

string = str(input('Digite alguma coisa: '))

print('')
print('-=' * 31 + '-')
print('')

print(string.__len__())

print('')
print('-=' * 31 + '-')
print('')
