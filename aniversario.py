from rich import inspect

class Pessoa:
    def __init__(self, nome, idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
        return self.idade


class Aluno(Pessoa):
    def __init__(self, nome, idade, curso):
        super().__init__(nome, idade)
        self.curso = curso

    def fazer_matricula(self, curso):
        self.curso = curso


class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel


def dar_aula(professor, aluno):
    print(f"{professor.nome} está dando aula para {aluno.nome} sobre {professor.especialidade}.")

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo):
        super().__init__(nome, idade)
        self.cargo = cargo

    def promover(self, novo_cargo):
        self.cargo = novo_cargo

def bater_ponto(funcionario):
    print(f"{funcionario.nome} bateu o ponto como {funcionario.cargo}.")

if __name__ == "__main__":
    a1 = Aluno("João", 20, curso="Engenharia, turma=T0P1")
    print(a1.nome)  # Saída: João
    p1 = Professor("Dr. Silva", 45, especialidade="Matemática", nivel="Doutor")
    f1 = Funcionario("Maria", 30, cargo="Secretária")

    p1.fazer_aniversario()
    inspect(p1, methods=True)
    bater_ponto(f1)
    print(f"Professor: {p1.nome}, idade: {p1.idade}, especialidade: {p1.especialidade}")
    print(f"Funcionário: {f1.nome}, cargo: {f1.cargo}")

