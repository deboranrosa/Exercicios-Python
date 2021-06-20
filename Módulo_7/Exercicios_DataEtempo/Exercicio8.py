# Escreva um programa Python para calcular o número de dias entre dois datetimes. A diferença entre os dias deve ser igual a 10.

from datetime import datetime

dataInicial = str(input('Insira a data inicial: '))
dataFinal = str(input('Insira a data final: '))

dataInicialFormatada = datetime.strptime(dataInicial, '%d/%m/%Y')
dataFinalFormatada = datetime.strptime(dataFinal, '%d/%m/%Y')

quantidadeDias = abs((dataFinalFormatada - dataInicialFormatada).days)

if quantidadeDias == 10:
    print('A quantidade de dias é igual 10')
    print(f'A quantidade de dias foi {quantidadeDias}')
else:
    print('A quantidade de dias é diferente de 10')
    print(f'A quantidade de dias foi {quantidadeDias}')