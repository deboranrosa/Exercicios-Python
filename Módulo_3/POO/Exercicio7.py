# Classe TV: Faça um programa que simule um televisor criando-o como um objeto. O
# usuário deve ser capaz de informar o número do canal e aumentar ou diminuir o volume.
# Certifique-se de que o número do canal e o nível do volume permanecem dentro de
# faixas válidas.

class Televisao:
    def __init__(self):
        self.numeroCanal = 0
        self.volume = 0
    
    def trocarCanal(self, numeroCanal):
        self.numeroCanal = numeroCanal
    
    def diminuirVolume(self):
        if(self.volume > 0):
            self.volume -= 1
    
    def aumentarVolume(self):
        if(self.volume < 100):
            self.volume += 1


tv1 = Televisao()
tv1.trocarCanal(56)
print(tv1.numeroCanal)
tv1.aumentarVolume()
tv1.aumentarVolume()
tv1.aumentarVolume()
tv1.aumentarVolume()
tv1.aumentarVolume()
tv1.aumentarVolume()
print(tv1.volume)
tv1.diminuirVolume()
tv1.diminuirVolume()
print(tv1.volume)
        