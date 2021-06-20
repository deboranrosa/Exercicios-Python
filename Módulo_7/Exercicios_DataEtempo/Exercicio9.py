# Faça um programa que calcule a diferença em dias entre antes de ontem e depois de amanhã.

from datetime import datetime

diaAntesDeOntem = str(input('Insira a data que foi antes de ontem: '))
diaDepoisDeAmanha = str(input('Insira a data que será depois de amanhã: '))

diaAntesDeOntemFormatada = datetime.strptime(diaAntesDeOntem, '%d/%m/%Y')
diaDepoisDeAmanhaFormatada = datetime.strptime(diaDepoisDeAmanha, '%d/%m/%Y')

quantidadeDias = abs((diaDepoisDeAmanhaFormatada - diaAntesDeOntemFormatada).days)

print('A quantidade de dias foi: ', quantidadeDias)