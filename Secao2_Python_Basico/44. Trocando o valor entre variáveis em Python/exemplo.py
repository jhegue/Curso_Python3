
# forma errada

print('\n' + '--' * 31 + '-\n')

x = 10 # Luiz
y = 'Luiz' # 10
z = 'Otávio'

'''
z = x
x = y
y = z

print(f'x={x} e y={y}')

print('\n' + '--' * 31 + '-\n')
'''

'''
# forma correta

x, y = y, x

print(f'x={x} e y={y}')


print('\n' + '--' * 31 + '-\n')
'''

x, y, z = z, x, y

print(f'x={x} e y={y} e z={z}')

print('\n' + '--' * 31 + '-\n')