# 8. Classe Bomba de Combustível: Faça um programa completo utilizando classes e
# métodos que:
# a. Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
# i.tipoCombustivel.
# ii.valorLitro
# iii.quantidadeCombustivel
# b. Possua no mínimo esses métodos:
# abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
# abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
# alterarValor( ) – altera o valor do litro do combustível.
# alterarCombustivel( ) – altera o tipo do combustível.
# alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
# OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba

class BombaDeCombustivel:
    def __init__(self, tipoCombustivel, valorLitro, quantidadeCombustivel):
        self.tipoCombustivel = tipoCombustivel
        self.valorLitro = valorLitro
        self.quantidadeCombustivel = quantidadeCombustivel
    
    def abastecerPorValor(self, valor):
        quantLitros = valor / self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - quantLitros)
        return quantLitros
    
    def abastecerPorLitro(self, litro):
        totalValor = litro * self.valorLitro
        self.alterarQuantidadeCombustivel(self.quantidadeCombustivel - totalValor)
        return totalValor
    
    def alterarValor(self, valorLitro):
        self.valorLitro = valorLitro
    
    def alterarCombustivel(self, tipoCombustivel):
        self.tipoCombustivel = tipoCombustivel
    
    def alterarQuantidadeCombustivel(self, quantidadeCombustivel):
        self.quantidadeCombustivel = quantidadeCombustivel


bombaCombustivel1 = BombaDeCombustivel('Gasolina', 1.50, 500)
print(bombaCombustivel1.tipoCombustivel)
print(bombaCombustivel1.valorLitro)
print(bombaCombustivel1.quantidadeCombustivel)

bombaCombustivel1.abastecerPorValor(200)
print(bombaCombustivel1.quantidadeCombustivel)

bombaCombustivel1.abastecerPorLitro(100)
print(bombaCombustivel1.quantidadeCombustivel)

bombaCombustivel1.alterarValor(2)
print(bombaCombustivel1.valorLitro)

bombaCombustivel1.alterarCombustivel('Alcool')
print(bombaCombustivel1.tipoCombustivel)

bombaCombustivel1.alterarQuantidadeCombustivel(200)
print(bombaCombustivel1.quantidadeCombustivel)
