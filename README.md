# OpenCloude - Aprendizado de POO em Python

Este repositório reúne vários exercícios de programação orientada a objetos que eu fiz para aprender e praticar POO em Python.

## O que tem aqui

Cada arquivo é um projeto pequeno com foco em um conceito de POO:

- `aniversario.py` → classes, herança, métodos e uso de `super()`
- `personagem.py` → classe abstrata, herança, polimorfismo e simulação de batalha
- `cafetaria.py` → padrão de template, abstração e método concreto compartilhado
- `salario.py` → classe abstrata para cálculo de salário e especialização de subclasses
- `veiculo.py` → herança simples e cálculo de frete por tipo de transporte
- `desafio.py` → polígono abstrato, cálculo de área e perímetro
- `vida.py` → classes, herança, abstração, manipulação de datas e entrada de usuário

## Meu caminho de aprendizado em POO

Eu escrevi esse código como se fosse o meu diário de estudos. Aqui estão os passos que segui:

1. **Entender o que é uma classe**
   - Criei classes como `Pessoa`, `BebidaQuente`, `Funcionario`, `Transporte`, `Personagem` e `Poligono`.
   - Usei `__init__` para definir atributos e armazenar dados de cada objeto.

2. **Usar objetos para representar dados reais**
   - Em `aniversario.py` eu represento pessoas, alunos, professores e funcionários.
   - Em `vida.py` eu represento uma pessoa e um passageiro que chega a Portugal.

3. **Aprender herança**
   - Criei subclasses que herdam comportamento da classe pai.
   - Em `aniversario.py`, `Aluno`, `Professor` e `Funcionario` herdam de `Pessoa`.
   - Em `veiculo.py`, `Moto`, `Caminhao` e `Drone` herdam de `Transporte`.
   - Em `vida.py`, `Passageiro` herda de `Pessoa`.

4. **Usar abstração e classes abstratas**
   - Usei `ABC` e `@abstractmethod` para definir contratos obrigatórios.
   - `personagem.py` define `Personagem` com método abstrato `curar()`.
   - `cafetaria.py` define `BebidaQuente` com `misturar()` e `servir()` abstratos.
   - `salario.py` define `Funcionario` com `calc_sal()` abstrato.
   - `desafio.py` define `Poligono` com `perimetro()` e `area()` abstratos.

5. **Aplicar polimorfismo**
   - Em `personagem.py`, `Guerreiro` e `Mago` usam o mesmo método `curar()` de formas diferentes.
   - Em `cafetaria.py`, todas as bebidas usam `preparar()` igual, mas têm `misturar()` e `servir()` diferentes.
   - Em `desafio.py`, `Quadrado` e `Circulo` calculam `area()` e `perimetro()` de formas distintas.

6. **Praticar lógica com exemplos do dia a dia**
   - `salario.py`: cálculo de salário com desconto de INSS.
   - `veiculo.py`: cálculo de frete por distância.
   - `vida.py`: cálculo de idade, dias vividos e tempo desde chegada.

7. **Melhorar a experiência com saída bonita**
   - Usei a biblioteca `rich` em `salario.py` e `vida.py` para imprimir resultados mais bonitos.

## Como rodar os exemplos

Abra o terminal na pasta `opencloude` e execute qualquer um dos arquivos com Python, por exemplo:

```bash
python aniversario.py
python personagem.py
python cafetaria.py
python salario.py
python veiculo.py
python desafio.py
python vida.py
```

## O que aprendi com cada arquivo

### `aniversario.py`
- Criei uma hierarquia de classes.
- Usei `super()` para chamar o construtor da classe pai.
- Organizei funções externas que trabalham com objetos (`dar_aula`, `bater_ponto`).

### `personagem.py`
- Usei classes abstratas para forçar métodos nas subclasses.
- Pratiquei polimorfismo com `curar()` e `atacar()`.
- Fiz uma pequena simulação de turnos de batalha.

### `cafetaria.py`
- Entendi o padrão de projeto Template Method.
- Criei comportamento comum (`preparar`, `ferver_agua`) e personalizei partes no `Cafe`, `Cha` e `Leite`.

### `salario.py`
- Trabalhei com herança e classes abstratas de novo.
- Usei atributos de classe como `sal_min` e `inss`.
- Calculei salários líquidos para diferentes tipos de funcionário.

### `veiculo.py`
- Usei herança para compartilhar a lógica do transporte.
- Cada veículo calcula o frete com seu próprio fator.

### `desafio.py`
- Criei um polígono abstrato e implementei duas formas geométricas.
- Pratiquei cálculo de área e perímetro.

### `vida.py`
- Combinei POO com datas e horas.
- Exibi informações de idade, dias vividos, noites vividas e tempo desde chegada.
- Usei classes abstratas para estruturar `Registro` e implementei `resumo()`.

## Conclusão

Esse repositório é meu estudo prático de POO em Python.

Eu escrevi cada arquivo pensando em:
- entender como construir classes
- usar herança para reaproveitar código
- usar abstração para definir regras
- aplicar polimorfismo para adaptar comportamento
- transformar lógica em objetos

Se quiser, posso também adicionar um README em português mais curto para o GitHub ou criar exemplos de execução passo a passo.
