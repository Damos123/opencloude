from __future__ import annotations

from abc import ABC, abstractmethod
from datetime import date, datetime, timedelta

from rich import print
from rich.panel import Panel
class Registro(ABC):
    @abstractmethod
    def resumo(self) -> str:
        pass


class Pessoa(Registro):
    def __init__(self, nome: str, data_nascimento: date):
        self.nome = nome.strip()
        self.data_nascimento = data_nascimento

    @staticmethod
    def _dias_no_mes(ano: int, mes: int) -> int:
        if mes == 12:
            return 31
        return (date(ano, mes + 1, 1) - timedelta(days=1)).day

    def idade(self, referencia: date | datetime | None = None) -> tuple[int, int, int]:
        if referencia is None:
            referencia = date.today()
        if isinstance(referencia, datetime):
            referencia = referencia.date()

        anos = referencia.year - self.data_nascimento.year
        meses = referencia.month - self.data_nascimento.month
        dias = referencia.day - self.data_nascimento.day

        if dias < 0:
            meses -= 1
            mes_anterior = referencia.month - 1 or 12
            ano_mes_anterior = referencia.year if referencia.month != 1 else referencia.year - 1
            dias += self._dias_no_mes(ano_mes_anterior, mes_anterior)

        if meses < 0:
            anos -= 1
            meses += 12

        return anos, meses, dias

    def dias_vividos(self, referencia: date | datetime | None = None) -> int:
        if referencia is None:
            referencia = date.today()
        if isinstance(referencia, datetime):
            referencia = referencia.date()
        return max(0, (referencia - self.data_nascimento).days)

    def noites_vividas(self, referencia: date | datetime | None = None) -> int:
        return self.dias_vividos(referencia)

    def resumo(self) -> str:
        hoje = datetime.now()
        anos, meses, dias = self.idade(hoje)
        dias_vividos = self.dias_vividos(hoje)
        noites_vividas = self.noites_vividas(hoje)

        return (
            f"Nome: {self.nome}\n"
            f"Data de nascimento: {self.data_nascimento.strftime('%d/%m/%Y')}\n"
            f"Idade atual: {anos} anos, {meses} meses e {dias} dias\n"
            f"Dias vividos: {dias_vividos}\n"
            f"Noites vividas: {noites_vividas}\n"
            f"Total para {anos} anos, {meses} meses e {dias} dias: {dias_vividos} dias e {noites_vividas} noites\n"
            f"Data atual e hora: {hoje.strftime('%d/%m/%Y %H:%M:%S')}"
        )


class Passageiro(Pessoa):
    def __init__(self, nome: str, data_nascimento: date, chegada_portugal: datetime):
        super().__init__(nome, data_nascimento)
        self.chegada_portugal = chegada_portugal

    def tempo_desde_chegada(self, referencia: datetime | None = None) -> tuple[int, int, int, int]:
        if referencia is None:
            referencia = datetime.now()

        delta = referencia - self.chegada_portugal
        if delta.total_seconds() < 0:
            return 0, 0, 0, 0

        dias = delta.days
        horas = delta.seconds // 3600
        minutos = (delta.seconds % 3600) // 60
        segundos = delta.seconds % 60
        noites = max(0, dias)
        return dias, noites, horas, minutos

    def resumo(self) -> str:
        agora = datetime.now()
        dias_desde_chegada, noites_desde_chegada, horas_desde_chegada, minutos_desde_chegada = self.tempo_desde_chegada(agora)

        return (
            super().resumo()
            + "\n\n"
            + f"Data e hora de chegada em Portugal: {self.chegada_portugal.strftime('%d/%m/%Y %H:%M')}\n"
            + f"Tempo desde a chegada: {dias_desde_chegada} dias, {noites_desde_chegada} noites, "
            + f"{horas_desde_chegada} horas e {minutos_desde_chegada} minutos"
        )


def ler_data(texto: str) -> date:
    while True:
        entrada = input(texto).strip()
        try:
            dia, mes, ano = [int(p) for p in entrada.split('/')]
            return date(ano, mes, dia)
        except (ValueError, TypeError):
            print("Entrada inválida. Use o formato DD/MM/AAAA.")


def ler_hora(texto: str) -> tuple[int, int]:
    while True:
        entrada = input(texto).strip()
        try:
            hora_int, minuto_int = [int(p) for p in entrada.split(':')]
            if 0 <= hora_int < 24 and 0 <= minuto_int < 60:
                return hora_int, minuto_int
            raise ValueError
        except (ValueError, TypeError):
            print("Entrada inválida. Use o formato HH:MM.")


def ler_data_hora(texto: str) -> datetime:
    while True:
        entrada = input(texto).strip()
        try:
            partes = entrada.split()
            data = partes[0]
            hora = partes[1] if len(partes) > 1 else "00:00"
            dia, mes, ano = [int(p) for p in data.split('/')]
            hora_int, minuto_int = [int(p) for p in hora.split(':')]
            return datetime(ano, mes, dia, hora_int, minuto_int)
        except (ValueError, IndexError):
            print("Entrada inválida. Use o formato DD/MM/AAAA HH:MM.")


def calcular_data_nascimento_por_idade(anos: int, meses: int, dias: int, referencia: date | None = None) -> date:
    if referencia is None:
        referencia = date.today()

    ano = referencia.year - anos
    mes = referencia.month - meses
    dia = referencia.day - dias

    while dia <= 0:
        mes -= 1
        if mes <= 0:
            ano -= 1
            mes += 12
        dia += Pessoa._dias_no_mes(ano, mes)

    while mes <= 0:
        ano -= 1
        mes += 12

    return date(ano, mes, min(dia, Pessoa._dias_no_mes(ano, mes)))


def main() -> None:
    print("--- Programa de Datas e Horas em POO ---\n")
    nome = input("Nome: ").strip()

    data_nascimento = ler_data("Data de nascimento (DD/MM/AAAA): ")

    data_chegada = ler_data("Data de chegada em Portugal (DD/MM/AAAA): ")
    hora_chegada, minuto_chegada = ler_hora("Hora de chegada em Portugal (HH:MM): ")
    chegada_portugal = datetime(
        data_chegada.year,
        data_chegada.month,
        data_chegada.day,
        hora_chegada,
        minuto_chegada,
    )
    passageiro = Passageiro(nome, data_nascimento, chegada_portugal)

    print("\n--- Resultado ---\n")
    print(passageiro.resumo())


if __name__ == "__main__":
    main()
