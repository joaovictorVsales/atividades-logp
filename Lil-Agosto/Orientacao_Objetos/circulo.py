import math
class Circulo:
    def __init__(self,raio):
        self.raio = raio

    def calcular_area(self):
        return math.pi*self.raio**2
    
    def calcular_perimetro(self):
        return math.pi*2*self.raio

circ1 = Circulo(10)
print(circ1.calcular_area())
print(circ1.calcular_perimetro())