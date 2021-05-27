# -*- coding: utf-8 -*-
i = 0;
contadorPar = 0;
contadorImpar = 0
resultadoContadorPar = 0;
resultadoContadorImpar = 0;
somaPar = 0;
somaImpar = 0;

while i < 10:
    i += 1;
    if i % 2 == 0: 
        contadorPar = contadorPar + 1;
        resultadoContadorPar = contadorPar;
        somaPar = somaPar + i;
        
    else:
        contadorImpar = contadorImpar + 1;
        resultadoContadorImpar = contadorImpar;
        somaImpar = somaImpar + i;
    
print("Quantidade de numeros pares de 1 a 10:", resultadoContadorPar);
print("Soma dos numeros pares:", somaPar);
print("Quantidade de numeros impares de 1 a 10:", resultadoContadorImpar);
print("Soma dos numeros impares:", somaImpar);
    
