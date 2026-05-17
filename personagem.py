from abc import ABC, abstractmethod
import random


class Personagem(ABC):
    def __init__(self, nome, vida, golpes):
        self.nome = nome
        self.vida = vida
        self.golpes = golpes

    def atacar(self, alvo, forca):
        dano = random.randint(int(forca * 0.8), int(forca * 1.2))
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} com {dano} de dano!")

    def receber_dano(self, dano):
        self.vida -= dano
        if self.vida < 0:
            self.vida = 0
        print(f"{self.nome} recebeu {dano} de dano. Vida restante: {self.vida}")

    @abstractmethod
    def curar(self):
        pass

    def esta_vivo(self):
        return self.vida > 0


class Guerreiro(Personagem):
    def __init__(self, nome, vida, golpes):
        super().__init__(nome, vida, golpes)
        self.curas_realizadas = 0

    def curar(self):
        cura = 30
        self.vida += cura
        self.curas_realizadas += 1
        print(f"{self.nome} se curou em {cura} de vida!")
        return self.vida


class Mago(Personagem):
    def curar(self):
        cura = 50
        self.vida += cura
        print(f"{self.nome} se curou em {cura} de vida com magia!")
        return self.vida


def batalha():
    print("=== BATALHA RPG ===\n")
    
    guerreiro = Guerreiro("Conan", 100, 20)
    mago = Mago("Merlin", 80, 25)
    
    turno = 1
    while guerreiro.esta_vivo() and mago.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        print(f"{guerreiro.nome}: {guerreiro.vida} de vida")
        print(f"{mago.nome}: {mago.vida} de vida\n")
        
        # Guerreiro ataca
        if random.choice([True, False]):
            guerreiro.atacar(mago, 15)
        else:
            guerreiro.curar()
        
        if not mago.esta_vivo():
            break
        
        # Mago ataca
        if random.choice([True, False]):
            mago.atacar(guerreiro, 20)
        else:
            mago.curar()
        
        turno += 1
    
    print("\n=== FIM DA BATALHA ===")
    if guerreiro.esta_vivo():
        print(f"\n✓ {guerreiro.nome} VENCEU!")
        print(f"  Vida restante: {guerreiro.vida}")
        print(f"  Vezes que se curou: {guerreiro.curas_realizadas}")
    else:
        print(f"\n✗ {guerreiro.nome} foi derrotado!")
        print(f"  Vida final: {guerreiro.vida}")
        print(f"  Vezes que se curou: {guerreiro.curas_realizadas}")
        print(f"\n✓ {mago.nome} venceu a batalha!")


if __name__ == "__main__":
    batalha()
