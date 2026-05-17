from abc import ABC, abstractmethod


class BebidaQuente(ABC):
    def preparar(self):
        self.ferver_agua()
        self.misturar()

    def ferver_agua(self):
        temperatura = 100
        print(f"Fervendo a água a {temperatura}°C...")

    @abstractmethod
    def misturar(self):
        pass

    @abstractmethod
    def servir(self):
        pass


class Cafe(BebidaQuente):
    def misturar(self):
        print("Misturando café com água quente.")

    def servir(self):
        print("Servindo o café quente.")


class Cha(BebidaQuente):
    def misturar(self):
        print("Misturando chá com água quente.")

    def servir(self):
        print("Servindo o chá quente.")


class Leite(BebidaQuente):
    def misturar(self):
        print("Misturando leite com água quente.")

    def servir(self):
        print("Servindo o leite quente.")


def main():
    bebidas = [Cafe(), Cha(), Leite()]

    for bebida in bebidas:
        print(f"\nPreparando {type(bebida).__name__}:")
        bebida.preparar()
        bebida.servir()


if __name__ == "__main__":
    main()
