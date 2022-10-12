"""
Tipos de dados
str - string - texto 'Assim' "Assim"
int - inteiro - 123456 0 -10 -20 -50 -60 -15000 1500
float - real/ponto flutuante - 10.50 1.5 -10.10 -50.93 0.0
bool - booleano/lógico - True/False 10 == 10
"""

print('\n')

print('Luiz', type('Luiz'))
print(10, type(10))
print(0.0, type(0.0))
print('l' == 'L', type('l' == 'L'))

print(bool(0))

print('luiz', type('luiz'), bool('luiz'))
print('10', type('10'), type(int('10')))

print(10 + 10)
print('10' + '10')

print('\n')


# String: nome
print('Luiz Otávio', type('Luiz Otávio'))

# Idade: int
print(32, type(32))

# Altura: float
print(1.80, type(1.80))

# É maior de idade 10 > 20
print(32 > 18, type(32 > 18))
