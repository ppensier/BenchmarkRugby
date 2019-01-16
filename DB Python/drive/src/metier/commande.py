'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

# -*- coding: Latin-1 -*-

import datetime
from bdd import accesBdd as bdd
from metier import exceptions as exceptions

class Commande(object):
    '''
    Commandes de courses effectuees par le client
    '''

    def __init__(self, date_de_commande, date_de_livraison, faisabilite, chaine_course,**kwargs):
        '''
        Constructeur à partir de chaînes de caractères
        '''
        super().__init__(**kwargs)
        self._date_de_commande = date_de_commande
        self._date_de_livraison = date_de_livraison
        self._faisabilite = None
        self._chaine_course = chaine_course

    @property
    def date_de_commande(self):
        return self._date_de_commande

    @date_de_commande.setter
    def date_de_commande(self, ch):
        self._date_de_commande = ch

    @property
    def date_de_livraison(self):
        return self._date_de_livraison

    @date_de_livraison.setter
    def date_de_livraison(self, ch):
        self._date_de_livraison = ch

    @property
    def faisabilite(self):
        return self._faisabilite()
    
    @faisabilite.setter
    def faisabilite(self, ch):
        self._faisabilite= ch
        
    @property
    def liste_course(self):
        return self._liste_course

    @liste_course.setter
    def liste_course(self, ch):
        self._liste_course = ch
    
    @property
    def chaine_course(self):
        return self._chaine_course

    @chaine_course.setter
    def chaine_course(self, ch):
        self._chaine_course = ch
    
    def selection_chaine_course(self,id_commande):
        # Cette fonction a un rôle uniquement dans l'interaction avec la base de donnée
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "SELECT chaine_de_course FROM commande WHERE idc=%s;", (id_commande,))
        chaine_course = cur.fetchone()[0]
        bdd.fermerConnexion(cur, conn)
        return chaine_course
        
    def conversion_liste_course (self,chaine_course):
        """on stock une chaine de caracteres de type ""Banane 2 Orange 4 "" et avec la 
        methode conversion on la transforme en une liste ["Banane",2,"Orange",4]"""
        return chaine_course.split()
    
    def verification_existence(self,liste_course,id_commande):
        """on verifie l'existence des produits sur la commande. C'est une securite avant d'interroger la BDD"""
        #on verifie en premier que la liste est non vide et de longueur paire
        (cur, conn) = bdd.ouvrirConnexion()
        i=0
        existence = True 
        if (len(liste_course) != 0 ) and ((len(liste_course) % 2) == 0):   
            for i in range(0,len(liste_course),2):
                article=liste_course[i]
                bdd.executerReq(cur, "SELECT nom FROM produit WHERE nom=%s;", (article,))
                res = cur.fetchone()
                if res == None: 
                    existence = False
        else:
            existence = False
        bdd.executerReq(cur, "UPDATE commande SET faisabilite = %s WHERE idc = %s ;", (existence,id_commande,))
        bdd.fermerConnexion(cur, conn)
        return existence
        
        
    def verification_quantite(self,liste_course,id_commande):
        """le test existence a deja ete fait."""
        #on verifie en premier que la liste est non vide et de longueur paire
        (cur, conn) = bdd.ouvrirConnexion()
        verif = True
        if (len(liste_course) != 0 ) and ((len(liste_course) % 2) == 0):   
            for i in range(1,len(liste_course)+1,2):
                article=liste_course[i-1]
                quantite=int(liste_course[i])
                bdd.executerReq(cur, "SELECT stock_reel FROM produit WHERE nom=%s;", (article,))
                res = cur.fetchone()[0]
                if (quantite <= 0) or (quantite > res) :
                    verif = False
        else:
            verif = False
        bdd.executerReq(cur, "UPDATE commande SET faisabilite = %s WHERE idc = %s ;", (verif,id_commande,))
        bdd.fermerConnexion(cur, conn)
        return verif
        
         
    def trierListeDeCourse(self, liste_course):
        # Cette fonction permet de trier une liste de course en fonction des zones et place les produits frais en dernier
        (cur, conn) = bdd.ouvrirConnexion()
        fruit=['Allez à la zone fruit-légume','']
        viande=['Allez à la zone viande-poisson','(Stocker les produits au rayon frais)']
        laitier=['Allez à la zone laitier-fromage','(Stocker les produits au rayon frais)']
        drink=['Allez à la zone boisson','']
        pain=['Allez à la zone épicerie-pâtisserie','']
        quantite=0
        for i in range(0,len(liste_course)-1,2):
            article=liste_course[i]
            quantite=liste_course[i+1]
            bdd.executerReq(cur, "SELECT categorie FROM produit WHERE nom=%s;",(article,))
            res = cur.fetchone()
            if res != None:
                if res[0] == 'laitier_fromage':
                    laitier.append(article)
                    laitier.append(quantite)
                elif res[0] == 'viande_poisson':
                    viande.append(article)
                    viande.append(quantite)
                elif res[0] == 'fruit_legume':
                    fruit.append(article)
                    fruit.append(quantite)
                elif res[0] == 'boisson':
                    drink.append(article)
                    drink.append(quantite)
                elif res[0] == 'epicerie_patisserie':
                    pain.append(article)
                    pain.append(quantite)
            else:
                print("Le produit %s n'est pas vendu par le magasin" % (article,))
        bdd.fermerConnexion(cur, conn)
        liste_triee=[]
        liste_triee.extend(pain)
        liste_triee.extend(fruit)
        liste_triee.extend(drink)
        liste_triee.extend(viande)
        liste_triee.extend(laitier)
        return liste_triee
    
    def calculPoids(self, liste_course):
        (cur, conn) = bdd.ouvrirConnexion()
        poids_commande=0
        for i in range(0,len(liste_course)-1,2):
            article=liste_course[i]
            bdd.executerReq(cur, "SELECT poids FROM produit WHERE nom=%s;",(article,))
            res = cur.fetchone()
            poids_commande=poids_commande+res[0]
        bdd.fermerConnexion(cur, conn)
        print('La commande a un poids de '+str(poids_commande)+' grammes.')
        return poids_commande
    
    def calculVolume(self, liste_course):
        (cur, conn) = bdd.ouvrirConnexion()
        volume_commande=1
        for i in range(0,len(liste_course)-1,2):
            article=liste_course[i]
            bdd.executerReq(cur, "SELECT volume FROM produit WHERE nom=%s;",(article,))
            res = cur.fetchone()
            volume_commande=volume_commande+res[0]
        bdd.fermerConnexion(cur, conn)
        print('La commande fait '+str(volume_commande)+' litres.')
        return volume_commande

    def calculPoidsFrais(self, liste_course):
        (cur, conn) = bdd.ouvrirConnexion()
        poids_commande=0
        for i in range(0,len(liste_course)-1,2):
            article=liste_course[i]
            bdd.executerReq(cur, "SELECT poids FROM produit WHERE nom=%s AND frais=%s;",(article,True))
            res = cur.fetchone()
            if res != None:
                poids_commande=poids_commande+res[0]
        bdd.fermerConnexion(cur, conn)
        print('Les produits frais un poids de '+str(poids_commande)+' grammes.')
        return poids_commande
    
    def calculVolumeFrais(self, liste_course):
        (cur, conn) = bdd.ouvrirConnexion()
        volume_commande=1
        for i in range(0,len(liste_course)-1,2):
            article=liste_course[i]
            bdd.executerReq(cur, "SELECT volume FROM produit WHERE nom=%s AND frais=%s;",(article,True))
            res = cur.fetchone()
            if res != None:
                volume_commande=volume_commande+res[0]
        bdd.fermerConnexion(cur, conn)
        print('Les produits frais font '+str(volume_commande)+' litres.')
        return volume_commande
    
    # La fonction retirerProduit est différente de la fonction employe.Employe.enleverProduit 
    # car ici les tests verification_existence et verification_quantite ont été effectués au préalable.
    
    def retirerProduit(self, liste_course):
        (cur, conn) = bdd.ouvrirConnexion()
        for i in range(0,len(liste_course)-1,2):
            article=liste_course[i]
            bdd.executerReq(cur, "SELECT stock_reel FROM produit WHERE nom=%s;",(article,))
            quantite_nouv=int(cur.fetchone()[0])-int(liste_course[i+1])
            bdd.executerReq(cur, "UPDATE produit SET stock_reel=%s WHERE nom=%s;",(quantite_nouv, article,))
            bdd.validerModifs(conn)
        bdd.fermerConnexion(cur, conn)
        
    def annulerCommande(self, id_commande):
        if id_commande != "" :
            (cur, conn) = bdd.ouvrirConnexion()
            try:
                bdd.executerReq(cur, "SELECT * FROM commande WHERE idc=%s;",(id_commande,))
                tout=cur.fetchone()
                if tout != None:
                    bdd.executerReq(cur, "DELETE FROM commande WHERE idc=%s;",(id_commande,))
                    bdd.validerModifs(conn)
                    bdd.fermerConnexion(cur, conn)
                    return True
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
        else:
            raise exceptions.ExceptionEntreeVide()
        
    def interaction(self,liste_course):
        # Fonction qui propose un produit de substitution au client en cas de rupture de stock
        (cur, conn) = bdd.ouvrirConnexion()
        for i in range(0,len(liste_course)-1,2):
            article=liste_course[i]
            nombre=liste_course[i+1]
            bdd.executerReq(cur, "SELECT stock_virtuel FROM produit WHERE nom=%s;",(article,))
            res=cur.fetchone()
            if res == (0,) :
                print('On vous propose les produits suivants :')
                bdd.executerReq(cur, "SELECT categorie FROM produit WHERE nom=%s;",(article,))
                ca=cur.fetchone()
                bdd.executerReq(cur, "SELECT idp , nom FROM produit WHERE categorie=%s;",(ca,))
                tr=False
                while (tr == False ) :
                    for row in cur:
                        print(row)
                    nm=input('Entrez idp du produit : ')
                    bdd.executerReq(cur, "SELECT nom FROM produit WHERE idp=%s;",(nm,))
                    fa=cur.fetchone()
                    if fa !=None:
                        tr=True
                liste_course[i]=fa[0]
        bdd.fermerConnexion(cur, conn)
        
    @staticmethod    
    def historique(nom,prenom):
        # Retourne l'ensemble des commandes d'un client spécifié
        if nom !="" and prenom!="" :    
            (cur, conn) = bdd.ouvrirConnexion()
            try :
                bdd.executerReq(cur, "SELECT idc FROM client WHERE nom=%s AND prenom=%s ;",(nom,prenom,))
                lst=[]
                res=cur.fetchone()[0]
                if res != None:
                    bdd.executerReq(cur, "SELECT idco FROM lien_client_commande WHERE idcl=%s ;",(res,))
                    id_co=cur.fetchall()
                    for i in range(0,len(id_co)):
                        bdd.executerReq(cur, "SELECT date_de_commande, date_de_livrasion, en_preparation, prete, livree, idc FROM commande WHERE idc=%s ;",(id_co[i],))
                        com=cur.fetchall()
                        lst.extend(com)
                else:
                    print("Le client n'existe pas.")
            except Exception:
                raise
            finally:
                bdd.fermerConnexion(cur, conn)
                return lst
    
    @staticmethod     
    def SelectionCommande():
        # Méthode qui donne à un employé la commande à traiter, elle est déjà triée par date. 
        # On va donc chercher le min de son identifiant.
        # Une fois appellée on modifie la table. On suppose donc que l'employé n'a pas son mot à dire sur la commande qu'il doit preparer. 
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "SELECT MIN(idc) FROM commande WHERE en_preparation=%s AND prete=%s AND livree=%s;",(False,False,False))
        id_commande_a_faire=cur.fetchone()[0]
        if id_commande_a_faire != None:
            bdd.executerReq(cur, "UPDATE commande SET en_preparation=%s WHERE idc=%s;",(True,id_commande_a_faire,))
            bdd.validerModifs(conn)
            bdd.fermerConnexion(cur, conn)
            return id_commande_a_faire
        bdd.fermerConnexion(cur, conn)
        
    @staticmethod
    def AfficherCommande():
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "SELECT date_de_commande, date_de_livrasion, en_preparation, prete, livree FROM commande;")
        coco=cur.fetchall()
        bdd.fermerConnexion(cur, conn)
        return coco
    
    @staticmethod
    def MarquerCommandePrete(id_commande):
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "UPDATE commande SET prete=%s WHERE idc=%s;",(True, id_commande,))
        bdd.validerModifs(conn)
        bdd.fermerConnexion(cur, conn)
        
    @staticmethod
    def MarquerCommandeLivree(id_commande):
        (cur, conn) = bdd.ouvrirConnexion()
        bdd.executerReq(cur, "UPDATE commande SET livree=%s WHERE idc=%s;",(True, id_commande,))
        bdd.validerModifs(conn)
        bdd.fermerConnexion(cur, conn)
    
    
#if __name__ == "__main__":
    #com=Commande('2004-10-19 10:23:54','2004-10-25 16:20:00',True,'Dorade 1 Orange 5')
    #ch=com.chaine_course
    #print(ch)
    #liste_course=com.conversion_liste_course(ch)
    #date_commande=com.date_de_commande
    #print(liste_course)
    #ex=com.verification_existence(liste_course,date_commande)
    #print(ex)
    #qu=com.verification_quantite(liste_course,date_commande)
    #print(qu)
    #trie=com.trierListeDeCourse(liste_course)
    #print(trie)
    #poids=com.calculPoids(liste_course)
    #print(poids)
    #volume=com.calculVolume(liste_course)
    #print(volume)
    #com.interaction(liste_course)
    #print(liste_course)