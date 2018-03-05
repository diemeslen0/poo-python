

class Data:
    '''
    Toy Class that receive 3 ints to represent a day, a month and a year 
    '''
    def __init__(self, dia, mes, ano):
        self.dia = dia
        self.mes = mes
        self.ano = ano
    
    def formatada(self):
        '''
        Returns the numbers attributes as follow 26/11/2018
        '''
        return '{0}/{1}/{2}'.format(self.dia, self.mes, self.ano)
