from abc import ABC, abstractmethod
from rich import print

class Transporte(ABC):
    def __init__(self, distancia):
        self.distancia = distancia
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete


class Caminhao(Transporte):
    fator = 1.20

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete


class Drone(Transporte):
    fator = 9.50

    def calc_frete(self):
        self.frete = self.distancia * self.fator
        return self.frete


def main():
    distancia = float(input("Digite a distância em km: "))
    veiculos = [Moto(distancia), Caminhao(distancia), Drone(distancia)]

    for veiculo in veiculos:
        valor = veiculo.calc_frete()
        print(f"{type(veiculo).__name__}: frete = €{valor:.2f}")


if __name__ == "__main__":
    main()
