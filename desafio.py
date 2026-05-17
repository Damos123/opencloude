from abc import ABC, abstractmethod
import math


class Poligono(ABC):
    def __init__(self, qtd_lados):
        self.qtd_lados = qtd_lados

    @abstractmethod
    def perimetro(self):
        pass

    @abstractmethod
    def area(self):
        pass


class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(4)
        self.lado = lado

    def perimetro(self):
        return 4 * self.lado

    def area(self):
        return self.lado ** 2


class Circulo(Poligono):
    def __init__(self, raio):
        super().__init__(0)
        self.raio = raio

    def perimetro(self):
        return 2 * math.pi * self.raio

    def area(self):
        return math.pi * self.raio ** 2


def main():
    print("--- Cálculo de Quadrado ---")
    lado = float(input("Digite o comprimento do lado do quadrado: "))
    quadrado = Quadrado(lado)
    print(f"Quadrado: perímetro = {quadrado.perimetro():.2f}")
    print(f"Quadrado: área = {quadrado.area():.2f}")

    print("\n--- Cálculo de Círculo ---")
    raio = float(input("Digite o raio do círculo: "))
    circulo = Circulo(raio)
    print(f"Círculo: perímetro = {circulo.perimetro():.2f}")
    print(f"Círculo: área = {circulo.area():.2f}")


if __name__ == "__main__":
    main()
