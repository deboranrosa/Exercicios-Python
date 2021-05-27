# Um objeto de função é um valor que pode ser atribuído a uma variável ou
# passado como argumento. Por exemplo, do_twice é uma função que toma um
# objeto de função como argumento e o chama duas vezes:
# def do_twice(f):
# f()
# f()
# Aqui está um exemplo que usa do_twice para chamar uma função chamada
# print_spam duas vezes:
# def print_spam():
# print('spam')
# do_twice(print_spam)
# a) Digite este exemplo em um script e teste-o.
# b) Altere do_twice para que receba dois argumentos, um objeto de função e
# um valor, e chame a função duas vezes, passando o valor como um
# argumento.

def do_twice(obj, valor):
    obj(valor)
    obj(valor)

def print_spam():
    print('spam')

do_twice(print, 'spam')