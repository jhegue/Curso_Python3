"""
While / Else - Aula 8
contadores
acumuladores
"""

print('\n' + '-=' * 31 + '-\n')

contador = 1
acumulador = 1

while contador <= 10:
    print(f'({contador}, {acumulador})')

    if contador > 5:
        break

    acumulador = acumulador + contador
    contador += 1
else:
    print('\nCheguei no else.')

print('              Isso será executado.             ')

print('\n' + '-=' * 31 + '-\n')
