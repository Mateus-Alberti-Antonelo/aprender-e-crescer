from animal import Animal

class Cachorro(Animal):
    def __init__(self, nome, idade, raca):
        # onde sera que vou parar quando fizer um ctrl_click nesse init?
        super().__init__(nome, idade) # aqui eu chamo o construtor da classe pai para inicializar os atributos nome e idade, assim eu nao preciso repetir o codigo do construtor da classe pai
        self.__raca = raca # isso eh tudo que a classe cachorro tem de diferente da classe animal, sera que eu preciso repetir tudo mesmo?

    @property
    def raca(self):
        return self.__raca

    @raca.setter
    def raca(self, nova_raca):
        self.__raca = nova_raca