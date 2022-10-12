"""
CPF = 168.995.350-09
_____________________________________________________

1 * 10 = 10           #    1 * 11 = 11 <-
6 * 9  = 54           #    6 * 10 = 60
6 * 8  = 64           #    8 *  9 = 72
6 * 7  = 63           #    9 *  8 = 72
6 * 6  = 54           #    9 *  7 = 63
6 * 5  = 25           #    5 *  6 = 30
6 * 4  = 12           #    3 *  5 = 15
6 * 3  = 15           #    5 *  4 = 20
6 * 2  = 0            #    0 *  3 = 0
'                     # -> 0 *  2 = 0
'        297          #             343
11 - (297 % 11) = 11  #     11 - (343 % 11) = 9
11 > 9 = 0            #
Digito 1 = 0          #   Digito 2 = 9
"""

print('\n' + '--' * 31 + '-\n')

while True:
    cpf = input('Digite um CPF: ')
    print('')
    novo_cpf = cpf[:-2]
    reverso = 10
    total = 0

    for index in range(19):
        if index > 8:
            index -= 9

        total += int(novo_cpf[index]) * reverso

        reverso -= 1
        if reverso < 2:
            reverso = 11
            d = 11 - (total % 11)

            if d > 9:
                d = 0
            total = 0
            novo_cpf += str(d)

    if cpf == novo_cpf:
        print('Válido')
    else:
        print('Inválido')

    print('\n' + '--' * 31 + '-\n')
