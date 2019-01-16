'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

class ExceptionEntreeVide(Exception):
    '''
    classdocs
    '''


    def __init__(self, message = None):
        '''
        Constructor
        '''
        super().__init__(message)
        

class ExceptionAuthentification(Exception):
    '''
    classdocs
    '''


    def __init__(self, message = None):
        '''
        Constructor
        '''
        super().__init__(message)