"""
* Criar variáveis para nome (str), idade (int),
* altura (float) e peso (float) de uma pessoa
* Criar variável com o ano atual (int)
* Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
* Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

import datetime

nome = 'Luiz'
idade = 35
altura = 1.8
peso = 80
imc = peso / altura ** 2

agora = datetime.datetime.now()
dia = agora.date()
ano = dia.strftime("%Y")

nascimento = int(ano) - idade

print('')
print('-=' * 31 + '-')
print('')

print('{n} tem {i} anos, {a} de altura e pesa {p}kg.'.format(n=nome, i=idade, a=altura, p=peso))
print('O IMC de Luiz é {:.2f}.'.format(imc))
print('Luiz nasceu em {}'.format(nascimento))

print('')
print('-=' * 31 + '-')
print('')