class ContaBancaria:
    total_contas = 0

    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular
        self.saldo = saldo_inicial
        ContaBancaria.total_contas += 1

    @classmethod #sem isso aqui, eu tenho um erro na chamada, pois precisa de um objeto criado
    def obter_total_contas(cls):
        return cls.total_contas
    
c1 = ContaBancaria("Alice", 1000)
c2 = ContaBancaria("Bob", 500)
print(f"Total de contas criadas: {ContaBancaria.obter_total_contas()}")