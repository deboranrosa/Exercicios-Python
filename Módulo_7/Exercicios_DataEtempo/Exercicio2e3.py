# Escreva um programa para imprimir uma string "Olá, mundo!" cinco vezes, em que cada
# uma das impressões demore três segundos entre uma e outra

import time

starScript = time.perf_counter()
inicioPrograma = time.time()

for i in range(0, 5):
    print('Olá, mundo!')
    time.sleep(3)

stopScript = time.perf_counter()
fimPrograma = time.time()

print('A variação de tempo foi: ', starScript, stopScript)
print('O tempo de todo programa foi: ', stopScript - starScript)

print('A variação de tempo foi: ', inicioPrograma, fimPrograma)
print('O tempo de todo programa foi: ', fimPrograma - inicioPrograma)


# Adapte o programa acima para calcular o tempo de processamento do script. Utilize
# time.time() e perf_counter() para apresentar a variação do tempo

