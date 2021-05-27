valorA = float(input("Insira o valor de A: "));
valorB = float(input("Insira o valor de B: "));
valorC = float(input("Insira o valor de C: "));

raizes = pow(valorB, 2) - 4 * valorA * valorC;

if valorA == 0:
    print("Valor de A não pode ser 0");
elif raizes < 0:
    print("Sem raizes reais");
else:
    x1 = (-valorB + pow(raizes, (1 / 2)) / (2 * valorA));
    x2 = (-valorB - pow(raizes, (1 / 2)) / (2 * valorA));

    print("x1: {}, x2: {}".format(x1, x2));