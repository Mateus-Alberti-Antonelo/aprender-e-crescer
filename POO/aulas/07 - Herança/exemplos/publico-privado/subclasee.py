from base import Base

class SubBase(Base):
    def __init__(self, nome):
        super().__init__(nome)

    def mostrar_informacoes(self):
        print(f'Nome: {self.nome}')  # Acesso ao atributo público
        print(f'Sobrenome: {self.__sobrenome}')  # Acesso ao método público para obter o atributo privado
