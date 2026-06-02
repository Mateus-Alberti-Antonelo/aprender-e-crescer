class Animal:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, nova_idade):
        if nova_idade < 0:
            print("Idade inválida. A idade deve ser um número positivo.")
        else:
            self.__idade = nova_idade