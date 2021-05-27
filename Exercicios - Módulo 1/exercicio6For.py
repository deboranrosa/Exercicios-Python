# coding=UTF-8

numerosPar = [];
numerosImpar = [];

for numero in range(1, 11):
    if numero % 2 == 0:
        numerosPar.append(numero)
    else:
        numerosImpar.append(numero)

print("Os numeros pares sao", numerosPar);
print("Os numeros impares sao", numerosImpar);
print("A soma dos numeros pares eh: ", sum(numerosPar));
print("A soma dos numeros impares eh: ", sum(numerosImpar));
