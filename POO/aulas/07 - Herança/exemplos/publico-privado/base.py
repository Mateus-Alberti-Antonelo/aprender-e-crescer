class Base:
    def __init__(self, nome):
        self.nome = nome
        self.sobrenome = 'Silva'  # Atributo privado

    def get_sobrenome(self):
        return self.__sobrenome  # Método público para acessar o atributo privado
    


# TODO terminar implementacao