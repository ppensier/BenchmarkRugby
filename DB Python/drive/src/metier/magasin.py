'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''


from bdd import accesBdd as bdd
from metier import exceptions as exceptions

class Magasin(object):
    
    def __init__(self,nom,role,**kwargs):
        super().__init__(**kwargs)
        self._nom= nom
        self._role= role
        
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, ch):
        self._nom = ch
        
    @property
    def role(self):
        return self._role
    @role.setter
    def role(self,ch):
        self._role = ch

    

class Emplacement(object):
    def __init__(self,geographie,nom,categorie,capacite,**kwargs) :
        self._geographie=geographie
        self._nom=nom
        self._categorie=categorie
        self._capacite=capacite
      
    @property
    def geographie(self):
        return self._geographie
    @geographie.setter
    def geographie(self,ch):
        self._geographie=ch 
         
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self,ch):
        self._nom=ch
    
    @property
    def categorie(self):
        return self._categorie
    @categorie.setter
    def categorie(self,ch):
        self._categorie=ch 
         
    @property
    def capacite(self):
        return self._capacite
    @capacite.setter
    def capacite(self,ch):
        self._capacite=ch
        
    def __str__(self):
        return "( "+self.nom.__str__()+", NW NE SW SE "+self.lst.__str__()+", Capacité :"+self.capacite.__str__()+")"
    def __repr__(self):
        return self.__str__()
    
    def determinerEmplacement(self,categorie):
        (cur, conn) = bdd.ouvrirConnexion()
        try:
            bdd.executerReq(cur, "SELECT nom FROM emplacement WHERE categorie=%s;" , (categorie,))
            res = cur.fetchone()[0]
        except Exception:
            raise
        finally:
            bdd.fermerConnexion(cur, conn)
        return res
    
    def verification_capacite(self,nom_emplacement,quantite):
        """On verifie que l'emplacement selectionne n'est pas en sur capacite"""
        #on va faire la somme des stock_reel de la zone selectionnee, retourne True si cette somme est inferieur a la capacite de la zone.
        #une zone pourra contenir plusieur categories differentes.
        if nom_emplacement != "":
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                #on selectionne la ou les categories qui sont dans la zone demandee.
                bdd.executerReq(cur, "SELECT categorie FROM emplacement WHERE nom=%s;" , (nom_emplacement,))
                res = cur.fetchone()
                #print(res)
                #on fait la somme des produits qui sont dans cette zone.
                bdd.executerReq(cur, "SELECT SUM(stock_reel) FROM produit WHERE categorie =%s;" , (res[0],))
                summ = cur.fetchone()
                somme_finale = int(summ[0])+quantite
                #print(summ[0])
                #on selectionne la capacite de la zone demandee.
                bdd.executerReq(cur, "SELECT capacite FROM emplacement WHERE nom=%s;" , (nom_emplacement,))
                capa = cur.fetchone()
                #print(capa[0])
                #on test en comparant capa[0] et summ[0]. 
                if somme_finale > int(capa[0]) : 
                    #print("Attention, la capacite de l'emplacement ne peut pas etre depassee. !")
                    return False
                else:
                    #print("On peut encore ajouter des produits dans cet emplacement")
                    return True
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()
    
    
class Produit(object):
    
    def __init__(self,nom,volume,poids,zone,stockReel,stockVirtuel,frais,**kwargs):
        super().__init__(**kwargs)
        self._nom = nom
        self._volume = volume
        self._poids = poids
        self._stockReel = stockReel
        self._stockVirtuel = stockVirtuel
        self._frais=frais
        self._zone=zone
        
    @property
    def nom(self):
        return self._nom

    @nom.setter
    def nom(self, nom):
        self._nom = nom
    @property
    def volume(self):
        return self._volume
    @volume.setter
    def volume(self,volume):
        self._volume=volume    
    @property
    def poids(self):
        return self._poids
    @poids.setter
    def poids(self,poids):
        self._poids=poids
    @property
    def stockReel(self):
        return self._stockReel
    @stockReel.setter
    def stockReel(self,stockReel):
        self._stockReel = stockReel
    @property
    def stockVirtuel(self):
        return self._stockVirtuel
    @stockVirtuel.setter
    def stockVirtuel(self,stockVirtuel):
        self._stockVirtuel=stockVirtuel 
    @property
    def frais(self):
        return self._frais
    @frais.setter
    def frais(self,frais):
        self._frais=frais
    @property
    def zone(self):
        return self._zone
    @zone.setter
    def zone(self, zone):
        self._zone = zone
        
    def __str__(self):
        return "( "+self.nom.__str__()+", volume :"+self.volume.__str__()+", poids :"+self.poids.__str__()+", \
        Zone : "+self.zone.__str__()+", stock réel :"+self.stockReel.__str__()+", stock virtuel :"+self.stockVirtuel.__str__()+", frais :"+self.frais.__str__()+")"
    def __repr__(self):
        return self.__str__()



if __name__ =="__main__" :
    #shop=Magasin('Le magasin','escroc en entrepot')
    place=Emplacement('Nord-Ouest','zone_A','fruit_legume',400)
    test=place.verification_capacite('zone_A')
    print(test)