# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
# No final, mostre:
# a) Quantas pessoas foram cadastradas
# b) A média de idade
# c) Uma lista com as mulheres
# d) Uma lista de pessoas com idade acima da média

# -*- coding: utf-8 -*-
cadastroPessoa = list()
pessoa = dict()
somaIdades = 0
mediaIdades = 0

while True:
    # Apagando a pessoa para ser incrementada na lista
    pessoa.clear()
    pessoa['nome'] = str(input("Digite o nome: ")).upper()

    # Validando a opção no cadastro
    while True:

    # Transformando a letra em maiuscula (upper) e pegando somente a primeira letra [0]
        pessoa['sexo'] = str(input("Digite o sexo: [F/M] ")).upper()[0]

        if pessoa['sexo'] in 'MF':
            break
        print("Opção inválida! Digite novamente as opções [M ou F]")

    pessoa['idade'] = int(input("Digite a idade: "))
    somaIdades = somaIdades + pessoa['idade']    

    # Copiando os dados do dicionario pessoa para a lista cadastroPessoa
    cadastroPessoa.append(pessoa.copy())

    while True:
        continuarCadastro = str(input("Gostaria de continuar cadastrando? [S/N]")).upper()[0]
        if continuarCadastro in 'SN':
            break
        print("Opção inválida! Digite novamente as opções [S ou N]")
    if continuarCadastro == 'N':
        break    




# Resposta da letra A
print(f'Ao todo foram cadastradas {len(cadastroPessoa)} pessoas.')

# Resposta da letra B
mediaIdades = somaIdades / len(cadastroPessoa)
print(f'A media de idade é {mediaIdades:2.2f} anos.')

# Resposta da letra C
for nomeMulheres in cadastroPessoa:
    if nomeMulheres['sexo'] == 'F':
        print(f'As mulheres cadastradas foram {nomeMulheres["nome"]}')

# Resposta da letra D
for pessoasAcimaMedia in cadastroPessoa:
    if pessoasAcimaMedia['idade'] >= mediaIdades:
        print(f'As pessoas que estão acima da media foam {pessoasAcimaMedia}')
