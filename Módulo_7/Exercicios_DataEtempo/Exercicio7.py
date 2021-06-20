# Escreva um programa Python para subtrair 8 dias da data atual.
# • Data atual: 25/01/2021
# • Data esperada: 17/01/2021

from datetime import datetime, timedelta

dataSubtracao = datetime.now() - timedelta(days=8)
print(dataSubtracao.strftime('%d/%m/%Y'))