from .funcionario import Funcionario

class Secretario(Funcionario):
    def apresentar(self):
        super().apresentar() # chama o método apresentar da classe pai (Funcionario)
        print("Eu sou um secretário.")