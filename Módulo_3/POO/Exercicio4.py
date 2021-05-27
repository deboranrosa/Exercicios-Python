# 4. Classe Pessoa: Crie uma classe que modele uma pessoa:
# a. Atributos: nome, idade, peso e altura
# b. Métodos: Envelhercer, engordar, emagrecer, crescer. Obs: Por padrão, a cada
# ano que nossa pessoa envelhece, sendo a idade dela menor que 21 anos, ela
# deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura

    def envelhecer(self, anos):
        self.idade += anos
        if(self.idade < 21):
            self.crescer(0.5)
    
    def engordar(self, peso):
        self.peso += peso
    
    def emagrecer(self, peso):
        self.peso -= peso
    
    def crescer(self, altura):
        self.altura += altura


pessoa1 = Pessoa('Debora', 22, 70, 156)
pessoa1.engordar(5)
pessoa1.crescer(2)
print(pessoa1.nome)
print(pessoa1.altura)
print(pessoa1.peso)
pessoa1.envelhecer(2)
print(pessoa1.idade)
print(pessoa1.altura)
pessoa1.emagrecer(7)
print(pessoa1.peso)
        