from funcionario import Funcionario

class Gerente(Funcionario):
    
    def aprovar_ferias(self, quem):
        print(f"{self.nome} aprovou as férias de {quem.nome}.") #aqui to usando nome do gerente, mas eu nem disse que esse cara tem nome...