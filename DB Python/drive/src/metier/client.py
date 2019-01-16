'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

from bdd import accesBdd as bdd
from metier import exceptions as exceptions

class Client(object):
    '''
    Clients deja enregistres dans la bdd
    '''
    
    def __init__(self, nom, prenom, accord_sub, telephone, adresse_mail,**kwargs):
        '''
        Constructeur a partir de chaines de caracteres 
        '''
        super().__init__(**kwargs)
        self._nom = nom
        self._prenom = prenom
        self._accord_sub = accord_sub
        self._telephone = telephone
        self._adrese_mail = adresse_mail
        
    @property
    def nom (self):
        return self._nom

    @nom .setter
    def nom (self, ch):
        self._nom = ch

    @property
    def prenom(self):
        return self._libelle

    @prenom.setter
    def prenom(self, ch):
        self._prenom = ch
    
    @property
    def accord_sub (self):
        return self._accord_sub

    @accord_sub .setter
    def accord_sub (self, ch):
        self._accord_sub = ch  
        
    @property
    def telephone (self):
        return self._telephone

    @telephone .setter
    def telephone (self, ch):
        self._telephone = ch
    
    @property
    def adresse_mail (self):
        return self._adresse_mail

    @adresse_mail .setter
    def adresse_mail (self, ch):
        self._adresse_mail = ch
    

if __name__ == "__main__":
    '''user=employe('max','im',18)
    ajouter client ('jacques','chirac','5 rue Jean Jaures Paris' ,TRUE,'1234567891','jacques.titi@gmail.com')
    user.ajoutClient("'jacques'","'chirac'","'5 rue Jean Jaures Paris'" ,True,"'1234567891'","'jacques.titi@gmail.com'")
    user.modificationClient("'jacques'","'chirac'","'bernadette'" ,"'chirac'",True,"'0110101010'","'elysee@palais.fr'")'''