class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

# Problema:
p = Pessoa("Carlos", 25)
p.idade = -10  # Aceita idade negativa!
p.idade = "vinte"  # Aceita texto em vez de número!