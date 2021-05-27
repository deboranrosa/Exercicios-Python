# Dada uma lista encadeada de caracteres formada por uma sequência alternada de
# letras e dígitos, construa um método que retorne uma lista na qual as letras são
# mantidas na sequência original e os dígitos são colocados na ordem inversa. Exemplos:
# A 1 E 5 T 7 W 8 G → A E T W G 8 7 5 1
# 3 C 9 H 4 Q 6 → C H Q 6 4 9 3
# Como mostram os exemplos, as letras devem ser mostradas primeiro, seguidas dos
# dígitos. Sugestões:
# a) usar uma fila e uma pilha;
# b) supor um método ehDigito() que retorna um valor booleano, como por exemplo,
# verdadeiro caso um caractere seja um dígito.

letras = []
numeros = []
digitos = ["0", "1", "2", "3", "4", "5", "6", "7", "8" , "9"]

listaSequencia = input("Digite uma sequência que contenha letras e numeros: ")

for sequencia in listaSequencia:
    if sequencia in digitos:
        numeros.append(sequencia)
        numeros.sort(reverse=True)
    else:
        letras.append(sequencia)

print(letras + numeros)