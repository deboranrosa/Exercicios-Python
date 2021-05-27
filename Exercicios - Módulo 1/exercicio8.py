# -*- coding: utf-8 -*-

import math;

def bhaskara(a, b, c):
    delta = b ** 2 - 4 * a * c;
    if delta < 0:
        return None;
    else:
        raizes = [];
        m1 = math.sqrt(delta);
        r1 = (-b + m1) / (2 * a);
        raizes.append(r1);
        r2 = (-b - m1) / (2 * a);
        raizes.append(r2);
        return raizes;

# O que significam palavras reservadas em Python?
    # São palavras que já tem uma utilização dentro da linguagem e devido a isso não podem ser usadas como nome de variavel.

# Quais são as palavras reservadas no código acima?
    # if, else, None, def, return, import.

# Qual a função de cada uma dessas palavras reservadas no código?
    # if - uma função de condição que só sera executada se for verdadeira
    # else - outra função de execução que será executada caso a condição do if seja false
    # None - é o retorno de nada
    # def - é para informar que está sendo criada uma função
    # return - é o valor de retorno de uma função
    # import - serve para importar alguma lib caso seja necessário

# Implemente a função acima e mostre na tela, o resultado da equação de segundo grau.

print(bhaskara(1, -5, 6))