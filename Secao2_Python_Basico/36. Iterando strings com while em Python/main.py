print('\n' + '-=' * 31 + '-\n')

#        Índices
#        0123456789......................33
frase = 'o rato roeu a roupa do rei de roma'  # Iterável
tamanho_frase = len(frase)
contador = 0
nova_string = ''

x = input('Qual letra quer que fique maromba? ')

print('\n' + '-=' * 31 + '-\n')

while contador < tamanho_frase:
    # print(frase[contador], contador)
    letra = frase[contador]

    if letra == x:
        nova_string += x.upper()

    else:
        nova_string += letra

    contador += 1

    print(nova_string)

print('\n' + '-=' * 31 + '-\n')
