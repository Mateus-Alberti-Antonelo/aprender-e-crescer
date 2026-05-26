class Pessoa:
    def __init__(self, nome, idade):
        self._nome = nome
        self._idade = idade
    
    # GETTER - pega a idade
    def get_idade(self):
        return self._idade

    # GETTER - pega o nome
    def get_nome(self):
        return self._nome


    # SETTER - define a idade (com validação)
    def set_idade(self, valor):
        if not isinstance(valor, int):
            raise ValueError("Idade deve ser um número inteiro")
        
        if valor < 0 or valor > 150:
            raise ValueError("Idade deve estar entre 0 e 150")
        
        self._idade = valor

    # SETTER - define o nome (com validação)
    def set_nome(self, nome):
        if not isinstance(nome, str):
            raise ValueError("Nome deve ser um texto")
        
        if len(nome) == 0:
            raise ValueError("Nome não pode ser vazio")
        
        self._nome = nome



# Uso:
p = Pessoa("Carlos", 25)
print(p.get_idade())  # O que sai aqui?
p.set_idade(30)  # OK
p.set_idade(-5)  #  O que acontece aqui?
p.set_nome("")  # O que acontece aqui?
p.set_nome(123)  # O que acontece aqui?
p.set_nome("Ana") 
print(p.get_nome()) # o que sai aqui?