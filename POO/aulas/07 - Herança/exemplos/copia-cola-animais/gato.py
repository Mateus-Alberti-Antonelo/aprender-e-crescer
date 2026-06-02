class Gato:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def __str__(self):
        return f"Gato: {self.__nome}, Idade: {self.__idade} anos"

    #GETTERS E SETTERS
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome
        
    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, nova_idade):
        self.__idade = nova_idade
    

    # ------------------------------------------------
    # metodo comer e miar
    def comer(self):
        print( f"{self.nome} está comendo.")
    
    def miar(self):
        print("Miau!")