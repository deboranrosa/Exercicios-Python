# 3. Para explorar os erros e as exceções em Python, convido vocês a revisitarem os
# exercícios do primeiro módulo e para cada um deles, provocar alguns erros e avaliar as
# mensagens do interpretador. Nesse estágio do nosso curso, deve estar mais claro e
# “menos aterrorizante” perceber que o Python nos ajuda a entender alguns dos erros que
# cometemos. Podemos implementar métodos de tratamento de exceções para as
# respectivas entradas de dados em cada um dos exercícios propostos. Você pode
# considerar a utilização dos seguintes recursos:

# a) Tente primeiramente utilizar os blocos try e except tratando as entradas de dados. Por
# exemplo: se o programa pede para que entre uma string, caso o usuário entre com um número inteiro,
#  uma mensagem de erro deve aparecer e indicar o usuário o caminho correto.
# b) Tente tratar as exceções com mensagens especificas. Dessa forma, melhoramos a
# usabilidade do código.
# c) Tente utilizar quando possível, a construção completa envolvendo try, except, else e
# finally

# Exercicio A e B
try:
    primeiroNumero = int(input("Digite o primeiro valor: "))
    segundoNumro = int(input("Digite o segundo valor: "))

    print(primeiroNumero + segundoNumro)
    print(primeiroNumero - segundoNumro)
    print(primeiroNumero * segundoNumro)
    print(primeiroNumero / segundoNumro)

except ValueError:
    print('Não é um número válido. Insira novamente')



# Exercicio C
try: 
    valorA = float(input("Insira o valor de A: "))
    valorB = float(input("Insira o valor de B: "))
    valorC = float(input("Insira o valor de C: "))

except ValueError:
    print("Valor inválido. Digite somente números.")

else:
    raizes = (valorB ** 2) - 4 * valorA * valorC
             
    if valorA == 0:
        print("Valor de A não pode ser 0")
    elif raizes < 0:
        print("Sem raizes reais\n");
    else:
        x1 = (-valorB + raizes ** (1 / 2) / (2 * valorA))
        x2 = (-valorB - raizes ** (1 / 2) / (2 * valorA))
        print("x1: {}, x2: {}".format(x1, x2))

finally:
    print("Programa executado")
