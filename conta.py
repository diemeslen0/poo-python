

class Conta:
    '''
    Class that represents a simple bank account
    '''    
    def __init__(self, numero, titular, saldo, limite=1000.0):
        self.__numero  = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def depositar(self, valor):
        '''
        Method to deposit a value in a bank account
        '''
        self.__saldo += valor
    
    def sacar(self, valor):
        '''
        Method to remove a velue from a bank accountss
        '''
        self.__saldo -= valor
    
    def transferir(self, valor, destino):
        '''
        Method to transfer a value between bank accounts
        '''
        self.sacar(valor)
        destino.depositar(valor)
    
    def extrato(self):
        '''
        Method to get information from a bank account
        '''
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))
