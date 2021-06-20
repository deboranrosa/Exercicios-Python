# Escreva scripts para mostrar os diversos formatos de tempo conforme se segue:
# Impressão da época padrão
# Segundos que se passaram desde a época
# Imprime dados do tempo no momento atual
# Cria um objeto time.localtime() e imprime o valor das horas, minutos e segundos
# Imprime se no momento atual estamos em horário de verão ou não

import time

# Impressao da época padrão
impressEpoquePadron = time.localtime()
print(impressEpoquePadron)

#Segundos que se passaram desde a época
secondsEpoque = time.mktime(impressEpoquePadron)
print(secondsEpoque)

# Imprime dados do tempo no momento atual
actualDate = time.ctime()
print(actualDate)

# Cria um objeto time.localtime() e imprime o valor das horas, minutos e segundos
actualTime = time.localtime()
print(f'Horas: {actualTime.tm_hour}')
print(f'Minutos: {actualTime.tm_min}')
print(f'Segundos: {actualTime.tm_sec}')

# Imprime se no momento atual estamos em horário de verão ou não

actualDateMoment = time.localtime()

if actualDateMoment.tm_mon == 1 or actualDateMoment.tm_mon == 2 or actualDateMoment.tm_mon == 10 or actualDateMoment == 11 or actualDateMoment == 12:
    print(f'Estamos em horário de verão pois estamos no mês: {actualDateMoment.tm_mon}')
else:
    print(f'Estamos fora do horário de verão pois estamos no mês: {actualDateMoment.tm_mon}')