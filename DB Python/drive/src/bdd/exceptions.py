'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''


class ExceptionContrainte(Exception):
    '''
    classdocs
    '''


    def __init__(self, message = None):
        '''
        Constructor
        '''
        super().__init__(message)


class ExceptionFormatInadequat(Exception):
    '''
    classdocs
    '''


    def __init__(self, message = None):
        '''
        Constructor
        '''
        super().__init__(message)