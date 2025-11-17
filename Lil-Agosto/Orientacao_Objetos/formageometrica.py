from abc import ABC, abstractmethod
import math

class FormaGeometrica(ABC):

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class Retangulo(FormaGeometrica):
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)


class Triangulo(FormaGeometrica):
    def __init__(self, lado1: float, lado2: float, lado3: float):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3

    def calcular_area(self):
        p = self.calcular_perimetro() / 2
        return math.sqrt(p * (p - self.lado1) * (p - self.lado2) * (p - self.lado3))

    def calcular_perimetro(self):
        return self.lado1 + self.lado2 + self.lado3


formas = [
    Retangulo(4, 8),
    Triangulo(3, 4, 5),
    Retangulo(2, 6),
    Triangulo(6, 7, 8)
]

for forma in formas:
    print(f"{type(forma).__name__}:")
    print("  Area:", forma.calcular_area())
    print("  Perimetro:", forma.calcular_perimetro(),"\n")