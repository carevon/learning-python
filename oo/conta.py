
class Conta:
    def __init__(self, numero, titular, saldo, limite):
        print("Construindo um objeto... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_titular(self):
        return self.__titular

    def get_numero(self):
        return self.__numero

    def extrato(self):
        print("Saldo {} do titular {}".format(self.__saldo, self.__titular))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        if(self.__disponibilidade_saques(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite.".format(valor))

    def __disponibilidade_saques(self, valor_saque):
        valor_disponivel = self.__saldo + self.__limite
        return valor_saque <= valor_disponivel

    def transferir(self, valor, destino):
        self.sacar(valor)
        destino.depositar(valor)



    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite

    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self, saldo):
        self.__saldo = saldo
