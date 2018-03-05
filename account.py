

class Account:
    '''
    Class that represents a simple bank account
    '''    
    def __init__(self, number, client, value, limit=1000.0):
        '''
        Init method with "private" attributes
        '''
        self.__number  = number
        self.__client = client
        self.__value = value
        self.__limit = limit

    @property
    def number(self):
        '''
        Returns the account number        
        '''
        return self.__number
    
    @property
    def client(self):
        '''
        Returns the account client        
        '''
        return self.__client
    
    @property
    def value(self):
        '''
        Returns the account value        
        '''
        return self.__value
    
    @property
    def limit(self):
        '''
        Returns the account limit        
        '''
        return self.__limit
    
    @limit.setter
    def limit(self, limit):
        '''
        Set the new limit        
        '''
        self.__limit = limit
    
    @staticmethod
    def bank():
        '''
        Static method that returns the bank number
        '''
        return "001"
    
    @staticmethod
    def banks():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

    def deposit(self, value):
        '''
        Method to deposit a value in a bank account
        '''
        self.__value += value
    
    def __can_take(self, value):
        '''
        "Private" method that returns True if the value is less or equal 
        the account balance. If not, return False
        '''
        return value <= self.__value + self.__limit
    
    def take(self, value):
        '''
        Method to remove a value from a bank accounts 
        '''
        if self.__can_take(value):
            self.__value -= value
        else:
            print('You have no enough money to take. Check you balance.')
    
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
