# Escreva scripts para mostrar os diversos formatos de data e tempo conforme se segue:
# Data e hora atual
# Ano atual
# Mês atual
# Número da semana do ano
# Dia atual da semana
# Dia do ano
# Dia do mês
# Dia da semana

import datetime

dateNow = datetime.datetime.now()
print('Data e hora atual: ', dateNow.strftime('%d/%m/%Y %H:%M'))
print('Ano atual: ', dateNow.year)
print('Mês atual: ', dateNow.month)
print('Número da semana do ano: ', dateNow.weekday())
print('Dia do ano: ', dateNow.timetuple().tm_yday)
print('Dia do mês: ', dateNow.timetuple().tm_mday)
print('Dia da semana: ', dateNow.timetuple().tm_wday)