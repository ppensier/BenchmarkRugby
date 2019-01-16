'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

# -*- coding: Latin-1 -*-

from tkinter import *
import tkinter as tk
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox
import metier.employe as employe
import metier.exceptions as excpMetier
import bdd.exceptions as excpBdd
import metier.commande as commande
import datetime
import metier.magasin as magasin

class FenetreAppli(tk.Tk):
    '''
    Fenêtre principale de l'application.
    '''
    
    def __init__(self, parent):
        '''
        Constructeur à partir de la fenêtre parente.
        '''
        super().__init__()
        self.parent = parent
        self.affiche()
        
        
        
    def affiche(self):
        self.title("Drive")
        
        cadreAffichage = ttk.Frame(self)
        cadreAffichage.pack(side=tk.TOP,fill=tk.BOTH, expand=0)
        
        # create a toplevel menu
        menubar = tk.Menu(self)
        
        # create a pulldown menu, and add it to the menu bar
        filemenu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Client", menu=filemenu)
        filemenu.add_command(label="Ajouter un client", command=lambda : self.ajouterClient(cadreAffichage))
        filemenu.add_command(label="Modifier un client", command=lambda : self.modifierClient(cadreAffichage))
        filemenu.add_command(label="Supprimer un client", command=lambda : self.supprimerClient(cadreAffichage))
        
        filemenu1 = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Produit", menu=filemenu1)
        filemenu1.add_command(label="Ajouter un nouveau produit", command=lambda : self.creerProduit(cadreAffichage))
        filemenu1.add_command(label="Ajouter un produit existant", command=lambda : self.ajouterProduit(cadreAffichage))
        filemenu1.add_command(label="Modifier un produit", command=lambda : self.modifierProduit(cadreAffichage))
        filemenu1.add_command(label="Supprimer un produit", command=lambda : self.supprimerProduit(cadreAffichage))
        
        filemenu2 = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Commande", menu=filemenu2)
        filemenu2.add_command(label="Prendre une commande", command=lambda : self.selectionCommande(cadreAffichage))
        filemenu2.add_command(label="Afficher l'état des commandes", command=lambda : self.afficherCommande(cadreAffichage))
        filemenu2.add_command(label="Associer une commande à un client", command=lambda : self.associerCommandeClient(cadreAffichage))
        filemenu2.add_command(label="Annuler une commande", command=lambda : self.annulerCommande(cadreAffichage))
        
        filemenu3 = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Historique", menu=filemenu3)
        filemenu3.add_command(label="Afficher l'historique", command=lambda : self.historique(cadreAffichage))
        
        menubar.add_command(label="Quitter", command=self.destroy)
        
        #menubar.add_command(label="Enregistrer bien", command=lambda : self.enregistrerBien(cadreAffichage))
        
        # display the menu
        self.config(menu=menubar)
        
        largeurEcran = self.winfo_screenwidth()
        hauteurEcran = self.winfo_screenheight()
        
        
        # self.overrideredirect(1) # pour supprimer titre et menus
        self.geometry("%dx%d+0+0" % (largeurEcran, hauteurEcran))
        
        #root.focus_set()
        self.mainloop()
        

    def ajouterClient(self, frame):
        for child in frame.winfo_children():
                child.destroy()
        
        nom = tk.StringVar()
        prenom = tk.StringVar()
        adresse = tk.StringVar()
        accord_sub = tk.BooleanVar()
        telephone = tk.IntVar()
        adresse_mail = tk.StringVar()
        
        nom_entry = ttk.Entry(frame, width=10, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        prenom_entry = ttk.Entry(frame, width=10, textvariable=prenom)
        prenom_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        adresse_entry = ttk.Entry(frame, width=20, textvariable=adresse)
        adresse_entry.grid(column=3, row=2, sticky=(tk.W, tk.E), padx=2)
        C1 = Checkbutton(frame, text = "oui", variable = accord_sub, \
        onvalue = 't')
        C1.grid(column=4, row=2)
        C2 = Checkbutton(frame, text = "non", variable = accord_sub, \
        onvalue = 'f')
        C2.grid(column=5, row=2)
        telephone_entry = ttk.Entry(frame, width=10, textvariable=telephone)
        telephone_entry.grid(column=6, row=2, sticky=(tk.W, tk.E), padx=2)
        adresse_mail_entry = ttk.Entry(frame, width=20, textvariable=adresse_mail)
        adresse_mail_entry.grid(column=7, row=2, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Prénom").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Adresse").grid(column=3, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Accord").grid(column=4, row=1, sticky=tk.W, pady=2)
        ttk.Label(frame, text="substitution").grid(column=5, row=1, sticky=tk.W, pady=2)
        ttk.Label(frame, text="Téléphone").grid(column=6, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Adresse e-mail").grid(column=7, row=1, sticky=tk.W, padx=2, pady=2)
        
        
        ttk.Button(frame, text="Ajout", command=lambda : self.ajoutCliEffectif(frame, nom.get(), prenom.get(), adresse.get(),accord_sub.get(), telephone.get(), adresse_mail.get())).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.ajoutCliEffectif(frame, nom.get(), prenom.get(), adresse.get(),accord_sub.get(), telephone.get(), adresse_mail.get())) 
    
    def ajoutCliEffectif(self, frame, nom, prenom, adresse, accord_sub, telephone, adresse_mail):
        try:
            employe.Employe.ajoutClient(self, nom, prenom, adresse, accord_sub, telephone, adresse_mail)
            for child in frame.winfo_children():
                child.destroy()
            messConfirmation = tk.StringVar()
            ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
            messConfirmation.set("Le client %s a été ajouté." % (nom.upper(), ))
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le client n'a pu être ajouté", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le client n'a pu être ajouté", parent=self)
        frame.mainloop()
    
    def modifierClient(self,frame):
        for child in frame.winfo_children():
                child.destroy()
                      
        nom_ancien = tk.StringVar()
        prenom_ancien = tk.StringVar()
        nom_nouv = tk.StringVar()
        prenom_nouv = tk.StringVar()
        adresse_nouv = tk.StringVar()
        accord_sub_nouv = tk.BooleanVar()
        telephone_nouv = tk.IntVar()
        adresse_mail_nouv = tk.StringVar()
        
        nom_ancien_entry = ttk.Entry(frame, width=20, textvariable=nom_ancien)
        nom_ancien_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        prenom_ancien_entry = ttk.Entry(frame, width=20, textvariable=prenom_ancien)
        prenom_ancien_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        nom_nouv_entry = ttk.Entry(frame, width=10, textvariable=nom_nouv)
        nom_nouv_entry.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=2)
        prenom_nouv_entry = ttk.Entry(frame, width=10, textvariable=prenom_nouv)
        prenom_nouv_entry.grid(column=2, row=4, sticky=(tk.W, tk.E))
        adresse_nouv_entry = ttk.Entry(frame, width=20, textvariable=adresse_nouv)
        adresse_nouv_entry.grid(column=3, row=2, sticky=(tk.W, tk.E), padx=2)
        # Bouton binaire pour choisir l'option (booléen) de substitution de produit en cas de rupture de stock
        C1 = Checkbutton(frame, text = "oui", variable = accord_sub_nouv, \
        onvalue = 't')
        C1.grid(column=4, row=2)
        C2 = Checkbutton(frame, text = "non", variable = accord_sub_nouv, \
        onvalue = 'f')
        C2.grid(column=5, row=2)
        telephone_nouv_entry = ttk.Entry(frame, width=10, textvariable=telephone_nouv)
        telephone_nouv_entry.grid(column=6, row=2, sticky=(tk.W, tk.E), padx=2)
        adresse_mail_nouv_entry = ttk.Entry(frame, width=20, textvariable=adresse_mail_nouv)
        adresse_mail_nouv_entry.grid(column=7, row=2, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text="Ancien nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Ancien prénom").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Nouveau nom").grid(column=1, row=3, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Nouveau prénom").grid(column=2, row=3, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Adresse").grid(column=3, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Accord").grid(column=4, row=1, sticky=tk.W, pady=2)
        ttk.Label(frame, text="substitution").grid(column=5, row=1, sticky=tk.W, pady=2)
        ttk.Label(frame, text="Téléphone").grid(column=6, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Adresse e-mail").grid(column=7, row=1, sticky=tk.W, padx=2, pady=2)
        
        ttk.Button(frame, text="Modifier", command=lambda : self.modifCliEffectif(frame, nom_ancien.get(), prenom_ancien.get(), nom_nouv.get(), prenom_nouv.get(), \
            adresse_nouv.get(), accord_sub_nouv.get(), telephone_nouv.get(), adresse_mail_nouv.get())).grid(column=1, row=5, sticky=tk.W, padx=5, pady=2)
        
        nom_ancien_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.modifCliEffectif(frame, nom_ancien.get(), prenom_ancien.get(), nom_nouv.get(), prenom_nouv.get(), \
            adresse_nouv.get(), accord_sub_nouv.get(), telephone_nouv.get(), adresse_mail_nouv.get()))
    
    def modifCliEffectif(self, frame, nom_ancien, prenom_ancien, nom_nouv, prenom_nouv, adresse_nouv, accord_sub_nouv, telephone_nouv, adresse_mail_nouv):
        try:
            b=employe.Employe.modificationClient(self, nom_ancien, prenom_ancien, nom_nouv, prenom_nouv, adresse_nouv, accord_sub_nouv, telephone_nouv, adresse_mail_nouv)
            # La fonction modificationClient renvoie un booléen pour tester si les attributs entrés existent dans la base de donnée
            if b == True:
                for child in frame.winfo_children():
                    child.destroy()
                messConfirmation = tk.StringVar()
                ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                messConfirmation.set("Le client %s a été modifié." % (nom_ancien.upper(), ))
            else:
                # On affiche une InfoBox pour la cas où les attributs n'existent pas dans la base donnée pour indiquer à l'employé qu'il rentre des données erronées
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le client n'existe pas dans la base", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le client n'a pu être modifié", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le client n'a pu être modifié", parent=self)
        frame.mainloop()
        
    def supprimerClient(self,frame):
        for child in frame.winfo_children():
                child.destroy()
        
        nom = tk.StringVar()
        prenom = tk.StringVar()
        
        nom_entry = ttk.Entry(frame, width=10, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        prenom_entry = ttk.Entry(frame, width=10, textvariable=prenom)
        prenom_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Prénom").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        
        ttk.Button(frame, text="Supprimer", command=lambda : self.supprCliEffectif(frame, nom.get(), prenom.get())).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.supprCliEffectif(frame, nom.get(), prenom.get()))
        
    def supprCliEffectif(self, frame, nom, prenom):
        try:
            b=employe.Employe.suppressionClient(self, nom, prenom)
            if b == True:
                for child in frame.winfo_children():
                    child.destroy()
                messConfirmation = tk.StringVar()
                ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                messConfirmation.set("Le client %s a été supprimé." % (nom.upper(), ))
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le client n'existe pas dans la base", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le client n'a pu être supprimé", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le client n'a pu être supprimé", parent=self)
        frame.mainloop()
    
    def creerProduit(self,frame):
        for child in frame.winfo_children():
                child.destroy()
        
        nom = tk.StringVar()
        categorie = tk.StringVar()
        volume = tk.DoubleVar()
        poids = tk.DoubleVar()
        quantite = tk.IntVar()
        frais = tk.BooleanVar()
        
        nom_entry = ttk.Entry(frame, width=10, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        # On affiche un menu déroulant (Combobox) pour donner un choix restreint à l'employé parmi toutes les catégories de produit
        listeCombobox = ['viande_poisson','fruit_legume','boisson','laitier_fromage','epicerie_patisserie']
        combo = ttk.Combobox(frame, values = listeCombobox, state = 'readonly', background = 'white', textvariable = categorie)
        combo.grid(column=2, row=2)
        volume_entry = ttk.Entry(frame, width=5, textvariable=volume)
        volume_entry.grid(column=3, row=2, sticky=(tk.W, tk.E), padx=2)
        poids_entry = ttk.Entry(frame, width=5, textvariable=poids)
        poids_entry.grid(column=5, row=2, sticky=(tk.W, tk.E))
        quantite_entry = ttk.Entry(frame, width=5, textvariable=quantite)
        quantite_entry.grid(column=7, row=2, sticky=(tk.W, tk.E), padx=2)
        C1 = Checkbutton(frame, text = "oui", variable = frais, \
        onvalue = 't')
        C1.grid(column=8, row=2)
        C2 = Checkbutton(frame, text = "non", variable = frais, \
        onvalue = 'f')
        C2.grid(column=9, row=2)
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Catégorie").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Volume").grid(column=3, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="litres").grid(column=4, row=2, sticky=tk.W, pady=2)
        ttk.Label(frame, text="Poids").grid(column=5, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="grammes").grid(column=6, row=2, sticky=tk.W, pady=2)
        ttk.Label(frame, text="Quantité").grid(column=7, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Produit").grid(column=8, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="frais").grid(column=9, row=1, sticky=tk.W, padx=2, pady=2)

        ttk.Button(frame, text="Création", command=lambda : self.creerProdEffectif(frame, nom.get(), categorie.get(), volume.get(),poids.get(), quantite.get(), frais.get())).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.creerProdEffectif(frame, nom.get(), categorie.get(), volume.get(),poids.get(), quantite.get(), frais.get())) # le paramètre non utilisé est une instance de la classe Event
    
    def creerProdEffectif(self, frame, nom, categorie, volume, poids, quantite, frais):
        try:
            nom_emplacement=magasin.Emplacement.determinerEmplacement(self, categorie)
            test=magasin.Emplacement.verification_capacite(self, nom_emplacement,quantite)
            if test == True:
                b=employe.Employe.nouveauProduit(self, nom, categorie, volume, poids, quantite, frais)
                if b == True:
                    for child in frame.winfo_children():
                        child.destroy()
                    messConfirmation = tk.StringVar()
                    ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                    messConfirmation.set("Le produit %s a été créé." % (nom.upper(), ))
                else:
                    messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le produit existe déjà dans la base", parent=self)
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="Il n'y a plus de place pour ce produit", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le produit n'a pu être créé", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le produit n'a pu être créé", parent=self)
        frame.mainloop()    
        
    def ajouterProduit(self,frame):
        for child in frame.winfo_children():
                child.destroy()
        
        nom = tk.StringVar()
        categorie = tk.StringVar()
        quantite = tk.IntVar()
        
        nom_entry = ttk.Entry(frame, width=10, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        quantite_entry = ttk.Entry(frame, width=5, textvariable=quantite)
        quantite_entry.grid(column=3, row=2, sticky=(tk.W, tk.E))
        listeCombobox = ['viande_poisson','fruit_legume','boisson','laitier_fromage','epicerie_patisserie']
        combo = ttk.Combobox(frame, values = listeCombobox, state = 'readonly', background = 'white', textvariable = categorie)
        combo.grid(column=2, row=2, padx=2)
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Catégorie").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Quantité").grid(column=3, row=1, sticky=tk.W, padx=2, pady=2)
        
        ttk.Button(frame, text="Ajout", command=lambda : self.ajoutProdEffectif(frame, nom.get(), categorie.get(), quantite.get())).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.ajoutProdEffectif(frame, nom.get(), categorie.get(), quantite.get())) # le paramètre non utilisé est une instance de la classe Event
    
    def ajoutProdEffectif(self, frame, nom, categorie, quantite):
        try:
            nom_emplacement=magasin.Emplacement.determinerEmplacement(self, categorie)
            test=magasin.Emplacement.verification_capacite(self, nom_emplacement,quantite)
            if test == True:
                b=employe.Employe.ajoutProduit(self, nom, categorie, quantite)
                if b == True:
                    for child in frame.winfo_children():
                        child.destroy()
                    messConfirmation = tk.StringVar()
                    ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                    messConfirmation.set("Le produit %s a été ajouté." % (nom.upper(), ))
                else:
                    messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le produit n'existe pas dans la base", parent=self)
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="Il n'y a plus de place pour cet ajout", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le produit n'a pu être ajouté", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le produit n'a pu être ajouté", parent=self)
        frame.mainloop()

    def supprimerProduit(self, frame):
        for child in frame.winfo_children():
                child.destroy()
        
        nom = tk.StringVar()
        quantite = tk.IntVar()
        
        nom_entry = ttk.Entry(frame, width=10, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        quantite_entry = ttk.Entry(frame, width=5, textvariable=quantite)
        quantite_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Quantité").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        
        ttk.Label(frame, text="Entrer 0 pour supprimer le produit").grid(column=3, row=2, sticky=tk.W, padx=2)
        
        ttk.Button(frame, text="Supprimer", command=lambda : self.supprProdEffectif(frame, nom.get(), quantite.get())).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.supprProdEffectif(frame, nom.get(), quantite.get()))
        
    def supprProdEffectif(self, frame, nom, quantite):
        try:
            b=employe.Employe.enleverProduit(self, nom, quantite)
            if b[0] == True:
                if b[1] == True:
                    for child in frame.winfo_children():
                        child.destroy()
                    messConfirmation = tk.StringVar()
                    ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                    messConfirmation.set("Le produit %s a été supprimé." % (nom.upper(), ))
                else:
                    if b[2] == True:
                        for child in frame.winfo_children():
                            child.destroy()
                        messConfirmation = tk.StringVar()
                        ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                        messConfirmation.set("%s unités du produit %s ont été supprimées." % (quantite, nom.upper(), ))
                    else:
                        messagebox.showinfo(title="Champ(s) non conforme(s)", message="Impossible d'enlever autant de produits", parent=self)
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le produit n'existe pas dans la base", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le produit n'a pu être supprimé", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le produit n'a pu être supprimé", parent=self)
        frame.mainloop()
    
    def modifierProduit(self, frame):
        for child in frame.winfo_children():
                child.destroy()
                      
        nom_ancien = tk.StringVar()
        nom_nouv = tk.StringVar()
        categorie_nouv = tk.StringVar()
        volume_nouv = tk.DoubleVar()
        poids_nouv = tk.DoubleVar()
        stock_virtuel_nouv = tk.IntVar()
        stock_reel_nouv = tk.IntVar()
        frais_nouv = tk.BooleanVar()
        
        nom_ancien_entry = ttk.Entry(frame, width=10, textvariable=nom_ancien)
        nom_ancien_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        nom_nouv_entry = ttk.Entry(frame, width=10, textvariable=nom_nouv)
        nom_nouv_entry.grid(column=1, row=4, sticky=(tk.W, tk.E), padx=2)
        listeCombobox = ['viande_poisson','fruit_legume','boisson','laitier_fromage','epicerie_patisserie']
        combo = ttk.Combobox(frame, values = listeCombobox, state = 'readonly', background = 'white', textvariable = categorie_nouv)
        combo.grid(column=2, row=2)
        volume_nouv_entry = ttk.Entry(frame, width=5, textvariable=volume_nouv)
        volume_nouv_entry.grid(column=3, row=2, sticky=(tk.W, tk.E), padx=2)
        poids_nouv_entry = ttk.Entry(frame, width=5, textvariable=poids_nouv)
        poids_nouv_entry.grid(column=5, row=2, sticky=(tk.W, tk.E))
        stock_virtuel_nouv_entry = ttk.Entry(frame, width=5, textvariable=stock_virtuel_nouv)
        stock_virtuel_nouv_entry.grid(column=7, row=2, sticky=(tk.W, tk.E), padx=2)
        stock_reel_nouv_entry = ttk.Entry(frame, width=5, textvariable=stock_reel_nouv)
        stock_reel_nouv_entry.grid(column=8, row=2, sticky=(tk.W, tk.E))
        C1 = Checkbutton(frame, text = "oui", variable = frais_nouv, \
        onvalue = 't')
        C1.grid(column=9, row=2, padx=2)
        C2 = Checkbutton(frame, text = "non", variable = frais_nouv, \
        onvalue = 'f')
        C2.grid(column=10, row=2)
        
        ttk.Label(frame, text="Ancien nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Nouveau nom").grid(column=1, row=3, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Catégorie").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Volume").grid(column=3, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="litres").grid(column=4, row=2, sticky=tk.W, pady=2)
        ttk.Label(frame, text="Poids").grid(column=5, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="grammes").grid(column=6, row=2, sticky=tk.W, pady=2)
        ttk.Label(frame, text="Stock virtuel").grid(column=7, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Stock réel").grid(column=8, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Produit").grid(column=9, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="frais").grid(column=10, row=1, sticky=tk.W, pady=2)
        
        ttk.Button(frame, text="Modifier", command=lambda : self.modifProdEffectif(frame, nom_ancien.get(), nom_nouv.get(), categorie_nouv.get(), \
            volume_nouv.get(), poids_nouv.get(), stock_virtuel_nouv.get(), stock_reel_nouv.get(), frais_nouv.get())).grid(column=1, row=5, sticky=tk.W, padx=5, pady=2)
        
        nom_ancien_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.modifProdEffectif(frame, nom_ancien.get(), nom_nouv.get(), categorie_nouv.get(), \
            volume_nouv.get(), poids_nouv.get(), stock_virtuel_nouv.get(), stock_reel_nouv.get(), frais_nouv.get()))
        
    def modifProdEffectif(self, frame, nom_ancien, nom_nouv, categorie_nouv, volume_nouv, poids_nouv, stock_virtuel_nouv, stock_reel_nouv, frais_nouv):
        try:
            b=employe.Employe.modificationProduit(self, nom_ancien, nom_nouv, categorie_nouv, volume_nouv, poids_nouv, stock_virtuel_nouv, stock_reel_nouv, frais_nouv)
            if b == True:
                for child in frame.winfo_children():
                    child.destroy()
                messConfirmation = tk.StringVar()
                ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                messConfirmation.set("Le produit %s a été modifié." % (nom_ancien.upper(), ))
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le produit n'existe pas dans la base", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Le produit n'a pu être modifié", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="Le produit n'a pu être modifié", parent=self)
        frame.mainloop()

    def historique(self,frame):
        for child in frame.winfo_children():
            child.destroy()
        nom = tk.StringVar()
        prenom = tk.StringVar()
        
        nom_entry = ttk.Entry(frame, width=20, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        prenom_entry = ttk.Entry(frame, width=20, textvariable=prenom)
        prenom_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Prénom").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        
        ttk.Button(frame, text="Valider", command=lambda : self.afficherHistorique(frame ,nom.get(), prenom.get())).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.afficherHistorique(frame, nom.get(),prenom.get())) 

    def afficherHistorique(self,frame,nom,prenom):
        try:
            lst=commande.Commande.historique(nom,prenom)
            if lst!=[]:
                for child in frame.winfo_children():
                    child.destroy()
                
                listeCombobox = []
                
                # Affichage de l'historique sous la forme d'un tableau avec comme colonnes : l'ID, l'heure et l'heure de retrait de la commande, 
                # ainsi que leur état (en préparation, prête ou livrée)
                titre0 = Label(frame)
                titre0.grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
                titre0.configure(text = "Commandes de M. %s :" % (nom.upper(),), foreground="dark green")
                
                titre10 = Label(frame)
                titre10.grid(column=1, row=2, sticky=tk.W, padx=2, pady=2)
                titre10.configure(text = "ID")
                
                titre1 = Label(frame)
                titre1.grid(column=2, row=2, sticky=tk.W, padx=2, pady=2)
                titre1.configure(text = "Date de commande")
                    
                titre2 = Label(frame)
                titre2.grid(column=3, row=2, sticky=tk.W, padx=2, pady=2)
                titre2.configure(text = "Date de livraison")
                
                titre3 = Label(frame)
                titre3.grid(column=4, row=2, sticky=tk.W, padx=2, pady=2)
                titre3.configure(text = "En préparation")
                
                titre4 = Label(frame)
                titre4.grid(column=5, row=2, sticky=tk.W, padx=2, pady=2)
                titre4.configure(text = "Prête")
                
                titre5 = Label(frame)
                titre5.grid(column=6, row=2, sticky=tk.W, padx=2, pady=2)
                titre5.configure(text = "Livrée")
                
                for i in range(0,len(lst)):
                    col10=Label(frame)
                    col10.grid(row=i+3, column=1, sticky=tk.W, padx=2, pady=2)
                    col10.configure(text = lst[i][5])
                    
                    col1=Label(frame)
                    col1.grid(row=i+3, column=2, sticky=tk.W, padx=2, pady=2)
                    col1.configure(text = lst[i][0])
                    
                    col2=Label(frame)
                    col2.grid(row=i+3, column=3, sticky=tk.W, padx=2, pady=2)
                    col2.configure(text = lst[i][1])
                    
                    col3=Label(frame)
                    col3.grid(row=i+3, column=4, padx=2, pady=2)
                    if ( lst[i][2] == True ):
                        col3.configure(text = "Oui")
                    else:
                        col3.configure(text = "Non")
                        
                    col4=Label(frame)
                    col4.grid(row=i+3, column=5, padx=2, pady=2)
                    if ( lst[i][3] == True ):
                        col4.configure(text = "Oui")
                    else:
                        col4.configure(text = "Non")
                        
                    col5=Label(frame)
                    col5.grid(row=i+3, column=6, padx=2, pady=2)
                    if ( lst[i][4] == True ):
                        col5.configure(text = "Oui")
                    else:
                        col5.configure(text = "Non")
                        listeCombobox.append(lst[i][5])
                
                # L'employé peut marquer comme livrée une commande qu'il a donné au client en sélectionnant parmi les commandes marquées non livrées
                messProp = tk.StringVar()
                ttk.Label(frame, textvariable=messProp).grid(column=2, row=len(lst)+3, sticky=tk.W, padx=2)
                messProp.set("Marquer la commande n°")
                
                id_commande_prete = tk.IntVar()
                combo = ttk.Combobox(frame, values = listeCombobox, state = 'readonly', background = 'white', textvariable = id_commande_prete, width = 5)
                combo.grid(column=3, row=len(lst)+3, sticky=tk.W)
                
                ttk.Button(frame, text="livrée", command=lambda : commande.Commande.MarquerCommandeLivree(id_commande_prete.get())).grid(column=4, row=len(lst)+3, sticky=tk.W, padx=5, pady=10)
                ttk.Button(frame, text="Rafraîchir", command=lambda : FenetreAppli.afficherHistorique(self,frame,nom,prenom)).grid(column=7, row=len(lst)+3, sticky=tk.W, padx=5, pady=10)                
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le client n'existe pas dans la base", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="Vous avez pas rentrez de client", parent=self)
        frame.mainloop()
        
    def afficherCommande(self,frame):
        for child in frame.winfo_children():
            child.destroy()
            
        # Cette fonction affiche l'état de toutes les commandes passées au magasin
        coco=commande.Commande.AfficherCommande()
        
        titre1 = Label(frame)
        titre1.grid(column=1, row=1, sticky=tk.W, padx=5, pady=2)
        titre1.configure(text = "Date de commande")
        for i in range(0,len(coco)):
            col1=Label(frame)
            col1.grid(row=i+2, column=1, padx=5, pady=2)
            col1.configure(text = coco[i][0])
        
        titre2 = Label(frame)
        titre2.grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        titre2.configure(text = "Date de livraison")
        for i in range(0,len(coco)):
            col2=Label(frame)
            col2.grid(row=i+2, column=2, padx=2, pady=2)
            col2.configure(text = coco[i][1])
        
        titre3 = Label(frame)
        titre3.grid(column=3, row=1, sticky=tk.W, padx=2, pady=2)
        titre3.configure(text = "En préparation")
        for i in range(0,len(coco)):
            col3=Label(frame)
            col3.grid(row=i+2, column=3, padx=2, pady=2)
            if ( coco[i][2] == True ):
                col3.configure(text = "Oui")
            else:
                col3.configure(text = "Non")
        
        titre4 = Label(frame)
        titre4.grid(column=4, row=1, sticky=tk.W, padx=2, pady=2)
        titre4.configure(text = "Prête")
        for i in range(0,len(coco)):
            col4=Label(frame)
            col4.grid(row=i+2, column=4, padx=2, pady=2)
            if ( coco[i][3] == True ):
                col4.configure(text = "Oui")
            else:
                col4.configure(text = "Non")
        
        titre5 = Label(frame)
        titre5.grid(column=5, row=1, sticky=tk.W, padx=2, pady=2)
        titre5.configure(text = "Livrée")
        for i in range(0,len(coco)):
            col5=Label(frame)
            col5.grid(row=i+2, column=5, padx=2, pady=2)
            if ( coco[i][4] == True ):
                col5.configure(text = "Oui")
            else:
                col5.configure(text = "Non")
            
        frame.mainloop()
        
    def selectionCommande(self,frame):
        for child in frame.winfo_children():
            child.destroy()
            
        # On prend la première commande dans l'ordre (classées par date de commande)
        
        ttk.Button(frame, text="Prendre la commande suivante", command=lambda : self.afficherSelectionCommande(frame)).grid(column=1, row=2, sticky=tk.W, padx=5, pady=2)
        
        self.bind('<Return>', lambda paraNonUtilise: self.afficherSelectionCommande(frame)) 
        
    def afficherSelectionCommande(self,frame):
        
        # On affiche les détails de la commande et on marque la commande comme - en préparation -
        id_commande_prise=commande.Commande.SelectionCommande()
        if id_commande_prise != None:
            chaine_course=commande.Commande.selection_chaine_course(self,id_commande_prise)
            liste_course=commande.Commande.conversion_liste_course(self, chaine_course)
            existence=commande.Commande.verification_existence(self, liste_course, id_commande_prise)
            for child in frame.winfo_children():
                        child.destroy()
            if existence == True:
                quantite=commande.Commande.verification_quantite(self, liste_course, id_commande_prise)
                if quantite == True:
                    messConfirmation = tk.StringVar()
                    ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                    messConfirmation.set("La commande numéro %s a bien été sélectionnée." % (id_commande_prise,))
                    
                    poids=commande.Commande.calculPoids(self, liste_course)
                    volume=commande.Commande.calculVolume(self, liste_course)
                    poidsFrais=commande.Commande.calculPoidsFrais(self, liste_course)
                    volumeFrais=commande.Commande.calculVolumeFrais(self, liste_course)
                    ttk.Label(frame, text="La commande pèse %s grammes et fait %s litres, dont %s grammes et %s litres de produis frais." % (poids, volume, poidsFrais, volumeFrais)).grid(column=1, row=2, sticky=tk.W, padx=2, pady=2)
                    
                    ttk.Button(frame, text="Imprimer la feuille de route", command=lambda : self.afficherParcours(frame, liste_course, id_commande_prise)).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
                    self.bind('<Return>', lambda paraNonUtilise: self.afficherParcours(frame, liste_course, id_commande_prise))
                else:
                    messConfirmation = tk.StringVar()
                    ttk.Label(frame, textvariable=messConfirmation, foreground="red").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                    messConfirmation.set("Un ou plusieurs produits sont indisponibles.")
            else:
                messConfirmation = tk.StringVar()
                ttk.Label(frame, textvariable=messConfirmation, foreground="red").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                messConfirmation.set("La commande numéro %s n'est pas conforme." % (id_commande_prise,))
        else:
            messConfirmation = tk.StringVar()
            ttk.Label(frame, textvariable=messConfirmation, foreground="red").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
            messConfirmation.set("Il n'y a plus de commande à traiter.")
        frame.mainloop()
        
    def afficherParcours(self,frame,liste_course,id_commande_prise):
        for child in frame.winfo_children():
            child.destroy()
            
        # L'employé a la possibilité de marquer la commande prise comme - prête - une fois qu'il a rempli le cadis avec la liste de course
        ttk.Button(frame, text="Marquer la commande comme prête", command=lambda : commande.Commande.MarquerCommandePrete(id_commande_prise)).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        commande.Commande.retirerProduit(self, liste_course)
        
        liste_triee=commande.Commande.trierListeDeCourse(self, liste_course)
        
        # On affiche la liste de course au format d'une liste triée grace à trierListeDeCourse
        top = Tk()
        top.title('Liste des courses')
        Lbx_course = Listbox(top, height=20, width=50)
        for i in range(0,len(liste_triee)-1,2):
            if ( liste_triee[i] == 'Allez à la zone fruit-légume' ) or ( liste_triee[i] == 'Allez à la zone viande-poisson' ) \
            or ( liste_triee[i] == 'Allez à la zone laitier-fromage' ) or ( liste_triee[i] == 'Allez à la zone boisson' ) or (liste_triee[i] == 'Allez à la zone épicerie-pâtisserie'):
                Lbx_course.insert(i, "%s %s" % (liste_triee[i],liste_triee[i+1],))
            else:
                Lbx_course.insert(i, "Element : %s | Quantité : %s" % (liste_triee[i],liste_triee[i+1],))
        Lbx_course.pack()
        top.mainloop()
        frame.mainloop()
        
    def associerCommandeClient(self, frame):
        for child in frame.winfo_children():
                child.destroy()
        
        nom = tk.StringVar()
        prenom = tk.StringVar()
        id_commande = tk.IntVar()
        
        nom_entry = ttk.Entry(frame, width=20, textvariable=nom)
        nom_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        prenom_entry = ttk.Entry(frame, width=20, textvariable=prenom)
        prenom_entry.grid(column=2, row=2, sticky=(tk.W, tk.E))
        id_commande_entry = ttk.Entry(frame, width=10, textvariable=id_commande)
        id_commande_entry.grid(column=3, row=2, sticky=(tk.W, tk.E), padx=2)
        
        ttk.Label(frame, text="Nom").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="Prénom").grid(column=2, row=1, sticky=tk.W, padx=2, pady=2)
        ttk.Label(frame, text="ID commande").grid(column=3, row=1, sticky=tk.W, padx=2, pady=2)
        
        ttk.Button(frame, text="Associer", command=lambda : self.associerCCEffectif(frame, nom.get(), prenom.get(), id_commande.get())).grid(column=1, row=4, sticky=tk.W, padx=5, pady=2)
        
        nom_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.associerCCEffectif(frame, nom.get(), prenom.get(), id_commande.get()))
    
    def associerCCEffectif(self, frame, nom, prenom, id_commande):
        
        # L'employé peut associer un client à une commande en cas d'erreur
        try:
            b=employe.Employe.AssocierCommandeClient(nom, prenom, id_commande)
            if b[0] == True:
                if b[1] == True:
                    for child in frame.winfo_children():
                        child.destroy()
                    messConfirmation = tk.StringVar()
                    ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                    messConfirmation.set("La commande numéro %s a été associée au client M. %s." % (id_commande, nom.upper(),))
                else:
                    messagebox.showinfo(title="Champ(s) non conforme(s)", message="Le client n'existe pas dans la base", parent=self)
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="La commande n'existe pas dans la base", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="La commande n'a pas pu être associée", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="La commande n'a pas pu être associé", parent=self)
        frame.mainloop()
        
    def annulerCommande(self,frame):
        for child in frame.winfo_children():
                child.destroy()
        
        id_commande = tk.IntVar()
        
        id_commande_entry = ttk.Entry(frame, width=10, textvariable=id_commande)
        id_commande_entry.grid(column=1, row=2, sticky=(tk.W, tk.E), padx=2)
        
        ttk.Label(frame, text="ID commande").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
        
        ttk.Button(frame, text="Annuler", command=lambda : self.annulerCommandeEffectif(frame, id_commande.get())).grid(column=1, row=3, sticky=tk.W, padx=5, pady=2)
        
        id_commande_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.associerCCEffectif(frame, id_commande.get()))
        
    def annulerCommandeEffectif(self,frame,id_commande):
        
        # L'employé peut annuler une commande en cas d'erreur
        try:
            b=commande.Commande.annulerCommande(self, id_commande)
            if b == True:
                for child in frame.winfo_children():
                    child.destroy()
                messConfirmation = tk.StringVar()
                ttk.Label(frame, textvariable=messConfirmation, foreground="dark green").grid(column=1, row=1, sticky=tk.W, padx=2, pady=2)
                messConfirmation.set("La commande numéro %s a été supprimée" % (id_commande,))
            else:
                messagebox.showinfo(title="Champ(s) non conforme(s)", message="La commande n'existe pas dans la base", parent=self)
        except excpMetier.ExceptionEntreeVide:
            messagebox.showinfo(title="Champ(s) vide(s)", message="La commande n'a pas pu être associée", parent=self)
        except excpBdd.ExceptionFormatInadequat:
            messagebox.showinfo(title="Champ(s) trop long(s)", message="La commande n'a pas pu être associé", parent=self)
        frame.mainloop()
        

if __name__ == '__main__':
    fen = FenetreAppli(None)
    