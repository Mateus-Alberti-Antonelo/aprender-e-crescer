class Pessoa: 
    def __init__(self, nome):
        self.__nome = nome
        self.__idade = 0  # Atributo privado

    @property
    def idade(self):
        print("chamando getter")
        return self.__idade


    @idade.setter
    def idade(self, valor):
        print("chamando setter")
        if isinstance(valor, int) and valor >= 0:
            self.__idade = valor
        else:
            print("Idade inválida! Deve ser um número inteiro não negativo.")

    @property
    def nome(self):
        print("chamando getter do nome")
        return self.__nome

    @nome.setter
    def nome(self, valor):
        print("chamando setter do nome")
        if isinstance(valor, str) and valor.strip():
            self.__nome = valor
        else:
            print("Nome inválido! Deve ser uma string não vazia.")

p1 = Pessoa("angelo")
p1.idade = -5  # Tenta atribuir idade negativa
print(p1.idade)  # Verifica a idade após a tentativa de atribuição


print(p1.nome)