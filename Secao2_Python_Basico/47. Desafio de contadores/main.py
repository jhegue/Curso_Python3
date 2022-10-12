"""
0   10
1   9
2   8
3   7
4   6
5   5
6   4
7   3
8   2
"""

# Eu fiz

print('\n' + '--' * 31 + '-\n')

x = 0
y = 10

print('Valor de X    Valor de Y\n')

while x <= 8:

    print(f'{x}             {y}')
    x += 1
    y -= 1

print('\n' + '--' * 31 + '-\n')

# Resolucao

for p, r in enumerate(range(10, 1, -1)):
    print(p, r)

print('\n' + '--' * 31 + '-\n')
