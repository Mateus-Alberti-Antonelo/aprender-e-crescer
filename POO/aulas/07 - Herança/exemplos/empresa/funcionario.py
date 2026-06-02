class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

    def apresentar(self):
        print(f"Olá, meu nome é {self.nome} e meu salário é {self.salario}.")