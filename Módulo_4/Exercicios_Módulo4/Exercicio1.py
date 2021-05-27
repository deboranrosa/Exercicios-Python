# Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos.

# O arquivo de entrada possui o seguinte formato:
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 257.32.4.5
# 85.345.1.2
# 1.2.3.4
# 9.8.234.5
# 192.168.0.256

# O arquivo de saída possui o seguinte formato:
# [Endereços válidos:]
# 200.135.80.9
# 192.168.1.1
# 8.35.67.74
# 1.2.3.4
# [Endereços inválidos:]
# 257.32.4.5
# 85.345.1.2
# 9.8.234.5
# 192.168.0.256

file = open("/home/debora/CURSO PYTHON/Módulo_4/Exercicios_Módulo4/ids.txt", "r")

listaIDS = file.readlines()

file.close()

ipsValidos = ""

ipsInvalidos = ""

for ids in range(len(listaIDS)):
    listaIDS2 = listaIDS[ids].split(".")
    if(int(listaIDS2[0])<=255 and int(listaIDS2[1])<=255 and int(listaIDS2[2])<=255 and int(listaIDS2[3])<=255):
        ipsValidos += listaIDS[ids] + "\n"
    else:
        ipsInvalidos += listaIDS[ids] + "\n"


file = open("/home/debora/CURSO PYTHON/Módulo_4/Exercicios_Módulo4/ipsValidos.txt", "w")
file.write(ipsValidos)
file.close()

file = open("/home/debora/CURSO PYTHON/Módulo_4/Exercicios_Módulo4/ipsInvalidos.txt", "w")
file.write(ipsInvalidos)
file.close()


