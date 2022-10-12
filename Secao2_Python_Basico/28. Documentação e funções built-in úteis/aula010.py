import re
 
def is_float(val):
    if isinstance(val, float): return True
    if re.search(r'^\-{,1}[0-9]+\.{1}[0-9]+$', val): return True
 
    return False
 
def is_int(val):
    if isinstance(val, int): return True
    if re.search(r'^\-{,1}[0-9]+$', val): return True
 
    return False
 
def is_number(val):
    return is_int(val) or is_float(val)
 
###########
#  USAGE  #
###########

print('')
print('-=' * 31 + '-')
print('')

num1 = input('Digite um número: ')
num2 = input('Digite um número: ')

print('')
print('-=' * 31 + '-')
print('')

if is_number(num1) and is_number(num2):
    num1 = float(num1)
    num2 = float(num2)

    print(num1 + num2)

else:
    print('ERROR')

print('')
print('-=' * 31 + '-')
print('')

numero01 = input('Digite um número: ')
numero02 = input('Digite um número: ')

print('')
print('-=' * 31 + '-')
print('')

try:
    numero01 = float(numero01)
    numero02 = float(numero02)

    print(numero01 + numero02)
except:
    print('ERROR')

print('')
print('-=' * 31 + '-')
print('')