class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    @property
    def nome(self):
        return self.__nome

    @property
    def salario(self):
        return self.__salario
    

    def apresentar(self):
        print(f"Olá, meu nome é {self.__nome} e meu salário é R${self.__salario:.2f}.")