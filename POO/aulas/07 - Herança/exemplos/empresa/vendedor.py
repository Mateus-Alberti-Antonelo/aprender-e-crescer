from funcionario import Funcionario

class Vendedor(Funcionario):    
    def vender(self):
        print(f"{self.nome} vendeu")