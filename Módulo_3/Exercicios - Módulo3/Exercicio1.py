# 1. Classe Bola: Crie uma classe que modele uma bola:
# a. Atributos: Cor, circunferência, material
# b. Métodos: trocaCor e mostraCor

class Bola:
    def __init__(self, cor, circunferencia, material):
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material

    def trocaCor(self, cor):
        self.cor = cor

    def mostraCor(self):
        return self.cor


bola1 = Bola('Azul', 'Redonda', 'Plastico')

bola1.trocaCor('Vermelho')

print(bola1.mostraCor())