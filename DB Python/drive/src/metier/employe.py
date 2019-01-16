'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

# -*- coding: Latin-1 -*-

from bdd import accesBdd as bdd
from metier import exceptions as exceptions
from pbkdf2 import crypt
from metier import magasin as magasin

class Employe(object):
    '''
    classdocs
    '''
         
    def __init__(self, nom, prenom, login,motDePasse,**kwargs):
        '''
        Constructor
        '''
        super().__init__(**kwargs)
        self._nom = nom
        self._prenom = prenom
        self._login = login
        self._motDePasse = motDePasse
        
    @property
    def nom(self):
        return self._nom
    @nom.setter
    def nom(self, ch):
        self._nom= ch
        
    @property
    def prenom(self):
        return self._prenom
    @prenom.setter
    def prenom(self, ch):
        self._prenom= ch
    
    @property
    def login(self):
        return self._identifiant
    @login.setter
    def login(self, ch):
        self._login= ch
    
    @property
    def motDePasse(self):
        return self._motDePasse
    @motDePasse.setter
    def motDePasse(self, ch):
        self._motDePasse= ch  
    
    @staticmethod
    def authentification(login, motDePasse):
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "SELECT mdp FROM employe WHERE login = %s ;", (login,))
        resR = cur.fetchone()
        if resR == None:
            raise exceptions.ExceptionAuthentification("Utilisateur inconnu")
        else:
            if resR[0] != crypt(motDePasse, resR[0]):
                raise exceptions.ExceptionAuthentification("MDP incorrect")
        bdd.fermerConnexion(cur, conn) 


    def ajoutClient(self,nom, prenom, adresse, accord_sub, telephone, adresse_mail):
        if nom != "" and prenom !="" and accord_sub != "" and telephone !="" and adresse_mail !="":
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                bdd.executerReq(cur, "INSERT INTO client (nom, prenom, adresse, accord_sub, telephone, adresse_mail) \
                        VALUES (%s, %s, %s, %s, %s, %s);",(nom, prenom, adresse, accord_sub, telephone, adresse_mail))
                bdd.validerModifs(conn)
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()

    def suppressionClient(self, nom, prenom):
        if nom != "" and prenom !="":
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                bdd.executerReq(cur, "SELECT * FROM client WHERE nom = %s AND prenom = %s;", (nom, prenom,))
                res = cur.fetchone()
                if res != None:
                    bdd.executerReq(cur, "DELETE FROM client WHERE nom=%s AND prenom=%s", (nom, prenom,))
                    bdd.validerModifs(conn)
                    bdd.fermerConnexion(cur, conn)
                    return True
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()
    
    def modificationClient(self,nom_ancien,prenom_ancien,nom_nouv,prenom_nouv,adresse_nouv,accord_sub_nouv,telephone_nouv,adresse_mail_nouv):
        if nom_ancien != "" and prenom_ancien !="" and nom_nouv != "" and prenom_nouv !="" and adresse_nouv != "" \
        and accord_sub_nouv !="" and telephone_nouv !="" and adresse_mail_nouv !="" :
            (cur, conn) = bdd.ouvrirConnexion()
            try: 
                #on verifie l'existence du client qui doit être modifie. 
                bdd.executerReq(cur, "SELECT idc FROM client WHERE nom = %s AND prenom = %s;",(nom_ancien,prenom_ancien,))
                res = cur.fetchone()
                if res != None:
                    idd=res[0]
                    bdd.executerReq(cur, " UPDATE client SET nom=%s, prenom=%s, adresse=%s, accord_sub=%s, telephone=%s, adresse_mail=%s WHERE idc= %s ;", \
                                    (nom_nouv, prenom_nouv, adresse_nouv, accord_sub_nouv, telephone_nouv, adresse_mail_nouv, idd, ))                     
                    bdd.validerModifs(conn)
                    bdd.fermerConnexion(cur, conn)
                    return True
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()
        
    # Les deux fonctions qui suivent diffèrent en ce que la première permet de créer un nouveau produit inexistant dans la base de donnée.
    # La seconde fonction permet simplement d'ajouter une certaine quantité d'un produit existant.
        
    def nouveauProduit(self,nom,categorie,volume,poids,quantite,frais):
        if nom != "" and categorie !="" and volume != "" and poids !="" and quantite!="" and frais!="":
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                #verification que c'est bien un nouveau produit
                bdd.executerReq(cur, "SELECT * FROM produit WHERE nom = %s ;",(nom,))
                res = cur.fetchone()
                if res == None: 
                    bdd.executerReq(cur, "INSERT INTO produit (nom, categorie, volume, poids, stock_virtuel, stock_reel,frais) \
                        VALUES (%s, %s, %s, %s, %s, %s, %s);", (nom, categorie, volume, poids,quantite,quantite,frais,))
                    bdd.validerModifs(conn)
                    bdd.fermerConnexion(cur, conn)
                    return True
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()
        
    def ajoutProduit(self,nom,categorie,quantite):
        #attention, le poids est celui du produit seul.
        conf=False
        if nom != "" and categorie !="" and quantite != "":
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                #on verifie si le produit ajouter existe deja. Si c'est la cas, on mettera a jour les stock.
                #on part du principe que le poids et le volume est unique pour le nom.
                bdd.executerReq(cur, "SELECT * FROM produit WHERE nom = %s ;", (nom,))
                res1 = cur.fetchall()
                if res1 != []:
                    res=res1[0]
                    conf=True
                    idd=res[0]
                    stockVirt_nouv=int(res[5])+quantite
                    stockReel_nouv=int(res[6])+quantite
                    bdd.executerReq(cur, "UPDATE produit SET stock_virtuel=%s, stock_reel=%s WHERE idp=%s;", (stockVirt_nouv, stockReel_nouv, idd,))
                    bdd.validerModifs(conn)
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()
        return conf
        
    def enleverProduit(self, nom, quantite):
        conf=[False,False,False]
        if nom != "":
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                #on verifie si le produit que l'on souhaite supprimer existe.
                bdd.executerReq(cur, "SELECT * FROM produit WHERE nom = %s; ",(nom,))
                res = cur.fetchone()
                if res != None: 
                    conf[0]=True
                    if quantite == 0:
                        conf[1]=True
                        bdd.executerReq(cur, "DELETE FROM produit WHERE nom = %s; ",(nom,))
                        bdd.validerModifs(conn)
                    else:
                        idp=res[0]
                        stockVirt_nouv=res[5]-quantite
                        #print(res[5])
                        #print(stockVirt_nouv)
                        stockReel_nouv=res[6]-quantite
                        #on s'assure de ne pas supprimer trop de produits
                        if stockVirt_nouv>0 and stockReel_nouv>0:
                            conf[2]=True
                            req1 =("UPDATE produit SET stock_virtuel=%s, stock_reel=%s WHERE idp=%s;" %(stockVirt_nouv,stockReel_nouv,idp,) )
                            bdd.executerReq(cur, req1)
                            bdd.validerModifs(conn)
                            print("suppression du produit reussie" )
                        else:
                            print("impossible d'enlever autant de produit, diminuez la quantite!")
                else: 
                    print("suppression impossible, assurez-vous de l'existence de ce produit")
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()
        return conf

    def modificationProduit(self,nom_ancien,nom_nouv,categorie_nouv,volume_nouv,poids_nouv,stock_virtuel_nouv,stock_reel_nouv,frais_nouv):
        if nom_ancien != "" and nom_nouv !="" and categorie_nouv != "" and volume_nouv !="" and poids_nouv != "" \
        and stock_virtuel_nouv !="" and stock_reel_nouv !="" and frais_nouv !="" :
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                #on verifie l'existence du produit que l'on souhaite modifier. 
                bdd.executerReq(cur, "SELECT idp FROM produit WHERE nom = %s;",(nom_ancien,))
                res = cur.fetchone()
                if res != None:
                    print("le produit est modifie")
                    #print(res[0])
                    idp=res[0]
                    bdd.executerReq(cur, " UPDATE produit SET nom=%s, categorie=%s, volume=%s, poids=%s, stock_virtuel=%s, stock_reel=%s, frais=%s \
                        WHERE idp= %s ;", (nom_nouv, categorie_nouv, volume_nouv, poids_nouv, stock_virtuel_nouv, stock_reel_nouv,frais_nouv, idp,))                     
                    bdd.validerModifs(conn)
                    bdd.fermerConnexion(cur, conn)
                    return True
                else:
                    print("le produit ne peut pas etre modifie. Assurez-vous de son existence ou des parametres de modifications.")
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()

    @staticmethod
    def RelationClient(nom,prenom):
        """ methode qui permet a l'employe de rendre une commande prete au client. On a donc besoin du nom de son prenom 
        du client pour retrouver la commande (et l'identifier par securite) si elle a ete terminee. 
        On a egalement besoin de la reference de la commande, qui est ici l'id de la commande (idc).
        On imagine que cette reference a ete donnee au client lors de son payement.
        Si la ou les commandes ne sont pas encore pretes, on informe le client sur l'avancement de sa commande.
        On peut imaginer cette methode utilisee uniquemement par le client, sur internet. """
        (cur, conn) = bdd.ouvrirConnexion()
        #on recupere la ou les commandes du client. Pour ce faire, on recupere l'id du client.
        #ensuite on va a lien_client_commande.
        #puis commande.
        bdd.executerReq(cur, "SELECT idc FROM client WHERE nom=%s AND prenom=%s;",(nom,prenom,))
        res=cur.fetchone()
        if res != None: 
            bdd.executerReq(cur, "SELECT idco FROM lien_client_commande WHERE idcl=%s;",(res[0],))        
            liste_commande=cur.fetchall()
            lst=[]
            #print(liste_commande)
            #on parcourt cette liste et on donne les etats des commandes.
            for i in range(0,len(liste_commande)):
                bdd.executerReq(cur, "SELECT * FROM commande WHERE idc=%s;",(liste_commande[i],))
                res1=cur.fetchall()
                if res1[5] == True:  
                    lst.append(res1[4])
                    lst.append('La commande est en preparation, revenez dans quelques minutes!')
                    #en_preparation == True
                    print("La commande est en preparation, revenez dans quelques minutes! ")
                elif res1[6] == True:  
                    lst.append(res1[4])
                    lst.append('La commande est faite et au depot, je vais la chercher !')
                    #prete == True ie Au depot prete a etre rendu au client
                    print("La commande est faite et au depot, je vais la chercher !")
                    bdd.executerReq(cur, "UPDATE commande SET livree=%s WHERE idc=%;",(True,res1[7],))
                elif res1[7] == True:  
                    #livree == True 
                    print("La commande a deja ete livree !")
                else:
                    lst.append(res1[4])
                    lst.append('La commande n a pas encore ete traite')
                    print("La commande n'a pas encore ete traite")
            return lst
        else:
            print("Aucune commande est enregistree")
        bdd.fermerConnexion(cur, conn)
    
    
    @staticmethod
    def AssocierCommandeClient(nom, prenom, id_commande):
        conf=[False,False]
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "SELECT idc FROM client WHERE nom=%s AND prenom=%s ;", (nom, prenom,))
        client=cur.fetchone()
        bdd.executerReq(cur, "SELECT * FROM commande WHERE idc=%s ;", (id_commande,))
        tout=cur.fetchone()
        if tout != None:
            conf[0]=True
            if client != None:
                conf[1]=True
                id_client=client[0]
                bdd.executerReq(cur, "UPDATE lien_client_commande SET idcl=%s WHERE idco=%s ;", (id_client, id_commande,))
                bdd.validerModifs(conn)
        bdd.fermerConnexion(cur, conn)
        return conf


if __name__ == "__main__":
    user=Employe('max','im','dédé','dédé')
    user.ajoutClient("chirac","jacques","5 rue Jean Jaures Paris" ,True,"1234567891","jacques.titi@gmail.com")
    #user.suppressionClient('chirac','bernadette')
    #user.modificationClient('toto','titi','chirac','jacques','5 rue Jean Jaures Paris',True,'0110101010','elysee@palais.fr')
    #user.ajoutProduit('abricot','fruit_legume',100)
    #user.ajoutProduit("'haricot'","'fruit_legume'",0,0,10,False)
    #user.nouveauProduit('haricot','fruit_legume',0,0,10,False) 
    #user.enleverProduit('abricot','')
    #user.modificationProduit('abricot', 'abricot', 'fruit_legume', 100, 50 , 54, 43,False)
    a=Employe.RelationClient('chirac','jacques')
    print(a)