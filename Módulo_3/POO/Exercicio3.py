# 3. Classe Retangulo: Crie uma classe que modele um retangulo:
# a. Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# b. Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# c. Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe 
# as medidades de um local. Depois, deve criar um objeto com as medidas e
# calcular a quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def mudarValorBase(self, base):
        self.base = base
    
    def mudarValorAltura(self, altura):
        self.altura = altura
    
    def retornarValorBase(self):
        return self.base
    
    def retornarValorAltura(self):
        return self.altura
    
    def calcularArea(self):
        return self.base * self.altura
    
    def calcularPerimetro(self):
        return 2 * (self.base + self.altura)


valorBase = int(input("Digite o valor da base: "))
valorAltura = int(input("Digite o valor da altura: "))

r = Retangulo(valorBase, valorAltura)

print("O valor da area sera: ", r.calcularArea())
print("O valor do perimetro sera: ", r.calcularPerimetro())