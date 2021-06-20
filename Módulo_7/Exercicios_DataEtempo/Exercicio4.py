# Escreva um programa para obter uma lista de datas entre duas datas. Considere o passo de
# um dia e reproduza o intervalo das datas entre 16/10/87 e 25/10/87

import datetime

firstDate = '16/10/87'
secondDate = '25/10/87'

firstDateFormat = datetime.datetime.strptime(firstDate, '%d/%m/%y').date()
secondDateFormat = datetime.datetime.strptime(secondDate, '%d/%m/%y').date()

aDay = datetime.timedelta(days=1)

while firstDateFormat <= secondDateFormat:
    print(firstDateFormat)
    firstDateFormat += aDay