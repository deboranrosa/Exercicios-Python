# Crie um programa que faça a impressão de uma mensagem e a multiplicação de dois
# números. Utilize módulos e funções para resolução desse problema.
# a) O usuário deve entrar com a mensagem e com o uso de módulos e funções, essa
# mensagem deve ser impressa na tela
# b) O usuário deve entrar com os valores dos dois multiplicadores e o programa deve exibir
# o resultado na tela.


from moduloMensagem import mensagem

mensagem('Hello World')

def multiplicar(a,b):
    resultado = a * b
    return print(resultado)


multiplicar(10,2)