

class Date:
    '''
    Toy Class that receive 3 ints to represent a day, a month and a year 
    '''
    def __init__(self, day, month, year):
        self.__day = day
        self.__month = month
        self.__year = year
    
    def format_date(self):
        '''
        Returns the numbers attributes as follow 26/11/2018
        '''
        return '{0}/{1}/{2}'.format(self.__day, self.__month, self.__year)
