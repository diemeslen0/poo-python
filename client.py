

class Client:
    '''
    Class to represent a simple client
    '''
    def __init__(self, name):
        '''
        The only attribute will be name
        '''
        self.__name = name
    
    @property
    def name(self):
        '''
        Using properties as getter
        '''
        return self.__name.title()

    @name.setter    
    def name(self, name):
        '''
        Using properties as setter
        '''
        self.__name = name


'''
from client import Client

client = Client('diemesleno')

client.name

client.name = 'outro'

client.name
'''