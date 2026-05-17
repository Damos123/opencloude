from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel

class Funcionario(ABC):
    sal_min = 920.00
    inss = 7.5

    def __init__(self, nome, sal_bruto):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = 0

    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        if self.salario < self.sal_min:
            print(f"Salário abaixo do mínimo!")
        else:
            print(f"Salário dentro dos padrões.")


class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trab):
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        sal_bruto = valor_hora * horas_trab
        super().__init__(nome, sal_bruto)

    def calc_sal(self):
        desconto = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - desconto
        return self.salario


class Mensalista(Funcionario):
    def calc_sal(self):
        desconto = self.sal_bruto * (self.inss / 100)
        self.salario = self.sal_bruto - desconto
        return self.salario


def main():
    print("[bold cyan]--- Cálculo de Salários ---[/bold cyan]\n")

    horista = Horista("João", 17.00, 160)
    horista.calc_sal()
    info_horista = f"[bold]{horista.nome}[/bold]\n"
    info_horista += f"Salário Bruto: €{horista.sal_bruto:.2f}\n"
    info_horista += f"Salário Líquido: €{horista.salario:.2f}"
    print(Panel(info_horista, title="[bold magenta]Horista[/bold magenta]", expand=False))

    mensalista = Mensalista("Maria", 9000)
    mensalista.calc_sal()
    info_mensalista = f"[bold]{mensalista.nome}[/bold]\n"
    info_mensalista += f"Salário Bruto: €{mensalista.sal_bruto:.2f}\n"
    info_mensalista += f"Salário Líquido: €{mensalista.salario:.2f}"
    print(Panel(info_mensalista, title="[bold magenta]Mensalista[/bold magenta]", expand=False))


if __name__ == "__main__":
    main()
