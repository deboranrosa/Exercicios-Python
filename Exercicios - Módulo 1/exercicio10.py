# -*- coding: utf-8 -*-

# 10. Escreva um programa que receba como entrada do usuário o nome “João” 
# sobrenome “da Silva”, idade “25”, Cidade “São Paulo”, ddd “11”, telefone “3333-3333” e
# faça as seguintes instruções:
# a) imprima na tela o nome completo em uma única linha
# Nome: João da Silva
# b) imprima na tela o telefone com ddd em uma única linha
# Telefone: (11)3333-3333
# c) Imprima na tela a idade
# Idade: 25
# d) Imprima na tela a cidade
# Cidade: São Paulo

# -*- coding: utf-8 -*-

nome = input("Digite o nome: ");
sobrenome = input("Digite o sobrenome: ");
idade = input("Digite a idade: ");
cidade = input("Digite a cidade: ");
phoneDDD = input("Digite o ddd correspondente a sua cidade (formato(dd)) : ");
telefone = input("Digite o telefone: formato xxxx-xxxx ");


print("Nome: "+ nome + ' ' + sobrenome);
print("Telefone: "+ str(phoneDDD) + str(telefone));
print("Idade: "+ str(idade));
print("Cidade: " + cidade);
