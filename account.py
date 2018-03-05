

class Account:
    '''
    Class that represents a simple bank account
    '''    
    def __init__(self, number, client, value, limit=1000.0):
        '''
        Init method with private attributes
        '''
        self.__number  = number
        self.__client = client
        self.__value = value
        self.__limit = limit
    
    def get_number(self):
        '''
        Returns the account number        
        '''
        return self.__number
    
    def get_client(self):
        '''
        Returns the account client        
        '''
        return self.__client

    def get_value(self):
        '''
        Returns the account value        
        '''
        return self.__value
    
    def get_limit(self):
        '''
        Returns the account limit        
        '''
        return self.__limit
    
    def set_limit(self, limit):
        '''
        Set the new limit        
        '''
        self.__limit = limit

    def deposit(self, value):
        '''
        Method to deposit a value in a bank account
        '''
        self.__value += value
    
    def take(self, value):
        '''
        Method to remove a value from a bank accountss
        '''
        self.__value -= value
    
    def transfer(self, value, destiny):
        '''
        Method to transfer a value between bank accounts
        '''
        self.take(value)
        destiny.depositar(value)
    
    def information(self):
        '''
        Method to get information from a bank account
        '''
        print("Valur of {} from client {}".format(self.__value, self.__client))
