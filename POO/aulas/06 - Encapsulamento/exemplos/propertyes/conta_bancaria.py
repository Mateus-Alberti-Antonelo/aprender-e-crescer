class ContaBancaria:
    def __init__(self, titular, saldo_inicial=0):
        self.titular = titular  # público
        self.__saldo = 0  # privado
        self.depositar(saldo_inicial)  # usa o método com validação
    
    @property
    def saldo(self):
        """Permite consultar o saldo"""
        return self.__saldo
    
    #Não criamos setter para saldo!
    # Só pode alterar via depositar() ou sacar()
    
    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de depósito deve ser positivo")
        self.__saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado. Saldo: R$ {self.__saldo:.2f}")
    
    def sacar(self, valor):
        if valor <= 0:
            raise ValueError("Valor de saque deve ser positivo")
        if valor > self.__saldo:
            raise ValueError("Saldo insuficiente")
        self.__saldo -= valor
        print(f"Saque de R$ {valor:.2f} realizado. Saldo: R$ {self.__saldo:.2f}")

# Uso:
conta = ContaBancaria("Ana", 100)
print(conta.saldo)  # 100.0 (pode consultar)
conta.depositar(50)  # OK
conta.sacar(30)  #OK
conta.saldo = 999999  # ERRO! AttributeError: can't set attribute