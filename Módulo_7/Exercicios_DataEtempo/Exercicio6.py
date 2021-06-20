# Escreva um programa Python capaz de converter uma string em data e hora.
# • String de exemplo: 01 de janeiro de 2021 13h53
# • Resultado esperado: 2021-01-01 13:53:00

from datetime import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

dataEHora = str(input('Digite uma data/hora: '))

formatDateHour = datetime.strptime(dataEHora, '%d de %B de %Y %Hh%M')
print(formatDateHour)