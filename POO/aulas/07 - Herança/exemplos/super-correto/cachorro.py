from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        self.__nome = nome #repete da classe pai
        self.__idade = idade #repete da classe pai

        self.__raca = raca # isso eh tudo que a classe cachorro tem de diferente da classe animal, sera que eu preciso repetir tudo mesmo?

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca):
        self.__raca = nova_raca