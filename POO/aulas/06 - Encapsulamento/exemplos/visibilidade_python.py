class ContaBancaria:
    
    """
    construtor, depositar, sacar
    e consultar saldo
    sao metodo publicos (sem nenhum underscore)
    """

    def __init__(self, numeroConta):
        """"
        meu numero da conta deve ser protegido
        entao eu adiciono UM UNDERSCORE na frente
        do seu nome
        """
        self._numero_conta = numeroConta

        """
        meu saldo deve ser privado
        entao um adiciono DOIS UNDERSCORES na frente
        do seu nome

        e altero os locais que usam ele
        """
        self.__saldo

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def consultarSaldo(self):
        return self.__saldo
    
    """
    quero poder verificar se tenho saldo
    mas os outros lugares que usam essa classe

    1 - nao precisam saber COMO eu valido
    2 - nao precisam saber QUANTO exatamente eu tenho
    """
    def _temSaldo(self):
        return self.__saldo > 0
    