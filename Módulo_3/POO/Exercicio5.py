# 5. Crie um programa que tenha uma classe Carro. Este programa deve ter no mínimo 3
# propriedades para a classe carro e no mínimo 3 métodos para ela, sendo um destes
# métodos para imprimir todos os dados de um carro.
# a. Crie 3 objetos para carros diferentes que recebem como entrada os parâmetros
# das propriedades que você definiu
# b. Consulte cada um desses parâmetros para cada um dos objetos criados no
# exercício anterior
# c. Chame cada um dos métodos criados para verificar o correto funcionamento

class Carro:
    def __init__(self, modelo, ano, potencia):
        self.modelo = modelo
        self.ano = ano
        self.potencia = potencia
    
    def alterarModelo(self, modelo):
        self.modelo = modelo
    
    def alterarPotencia(self, potencia):
        self.potencia = potencia
    
    def imprimirDadosCarro(self):
        return print('Modelo:', self.modelo, 'Ano:', self.ano, 'Potencia:', self.potencia)
    

carro1 = Carro('Palio', '2006', 86.7)
print(carro1.modelo)
print(carro1.ano)
print(carro1.potencia)

carro2 = Carro('Fusca', '2000', 50)
print(carro2.modelo)
print(carro2.ano)
print(carro2.potencia)

carro3 = Carro('Vectra', '2005', 75.9)
print(carro3.modelo)
print(carro3.ano)
print(carro3.potencia)

carro1.alterarModelo('Gol')
print(carro1.modelo)

carro2.alterarPotencia(45.5)
print(carro2.potencia)

carro3.imprimirDadosCarro()