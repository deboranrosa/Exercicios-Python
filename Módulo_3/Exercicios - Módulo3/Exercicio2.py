# 2. Classe Quadrado: Crie uma classe que modele um quadrado:
# a. Atributos: Tamanho do lado
# b. Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
    
    def mudarValorLado(self, tamanhoLado):
        self.tamanhoLado = tamanhoLado
    
    def mostrarValorDoLado(self):
        return self.tamanhoLado

    def calcularArea(self):
        return self.tamanhoLado * self.tamanhoLado


quadrado1 = Quadrado(10)
quadrado1.mudarValorLado(20)
print(quadrado1.mostrarValorDoLado())
print(quadrado1.calcularArea())