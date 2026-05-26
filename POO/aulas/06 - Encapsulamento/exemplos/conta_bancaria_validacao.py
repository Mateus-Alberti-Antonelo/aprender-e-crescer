class ContaBancaria:
    def __init__(self, numeroConta):
        self._numero_conta = numeroConta
        self.__saldo = 0

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor_a_sacar):
        if self.consultarSaldo() < valor_a_sacar:
            raise ValueError("Saldo insuficiente")
        
        self.__saldo -= valor_a_sacar

    def consultarSaldo(self):
        return self.__saldo