# -*- coding: utf-8 -*-
frutas = ["banana", "maça", "laranja", "carambola"];
for x in frutas:
    print(x);

for x in "carambola":
    print(x);

for x in range (5):
    print(x)


i = 0;
while i < 5:
    print(i);
    i += 1;

# utilizando um contador
# for

contador = 0;
for elemento in range(0,10):
    print(contador);
    contador = contador + 1;

#acumuladores
n = 1;
soma = 0;
while n <= 10:
    x = int(input("Digite o %d número:"%n));
    soma = soma + x;
    n = n + 1;
    print("Soma: %d" %soma);

#interrompendo a repetição
contador = 1;
while contador <= 5:
    print("Olá, mundo");
    contador = contador + 1;
    break;