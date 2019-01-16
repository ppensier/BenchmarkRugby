'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

import tkinter
import tkinter.ttk as ttk
import tkinter.messagebox as messagebox

import metier.employe as employe
import ihm.fenetreAppli as fenetreAppli
import metier.exceptions as excpMetier

class Authentification(tkinter.Tk):
    '''
    Définition d'une fenêtre d'authentification.
    '''
    def __init__(self, parent):
        '''
        Constructeur à partir de la fenêtre parente.
        '''
        super().__init__()
        self.parent = parent
        self.affiche()

    def connexion(self, login, passwd):
        print("connexion")
        ident = login.get()
        mdp = passwd.get()
        try:
            employe.Employe.authentification(ident, mdp)
            self.destroy()
            fenetreAppli.FenetreAppli(self)
        except excpMetier.ExceptionAuthentification:
            messagebox.showinfo(title="Échec", message="Identifiant ou mot de passe incorrect", parent=self)


    def abandon(self):
        print("abandon")
        exit()

    def affiche(self):
        self.title("Authentification")
        
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        mainframe.columnconfigure(0, weight=1)
        mainframe.rowconfigure(0, weight=1)
        
        login = tkinter.StringVar()
        passwd = tkinter.StringVar()
        
        login_entry = ttk.Entry(mainframe, width=7, textvariable=login)
        login_entry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))
        
        passwd_entry = ttk.Entry(mainframe, width=7, textvariable=passwd, show="•")
        passwd_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))
        
        ttk.Button(mainframe, text="Se connecter", command=lambda: self.connexion(login, passwd)).grid(column=2, row=3, sticky=tkinter.W)
        ttk.Button(mainframe, text="Abandonner", command=self.abandon).grid(column=1, row=3, sticky=tkinter.W)
        
        ttk.Label(mainframe, text="Identifiant").grid(column=1, row=1, sticky=tkinter.W)
        ttk.Label(mainframe, text="Mot de passe").grid(column=1, row=2, sticky=tkinter.W)
        
        for child in mainframe.winfo_children(): 
            child.grid_configure(padx=5, pady=5)
        
        login_entry.focus()
        self.bind('<Return>', lambda paraNonUtilise: self.connexion(login, passwd)) # le paramètre non utilisé est une instance de la classe Event
        
        largeurEcran = self.winfo_screenwidth()
        hauteurEcran = self.winfo_screenheight()
        
        largeurFenetre = 220
        hauteurFenetre = 100
 
        self.geometry("%dx%d+%d+%d" % (largeurFenetre,hauteurFenetre,(largeurEcran - largeurFenetre)/2, (hauteurEcran - hauteurFenetre)/2))
        self.mainloop()
        
        
if __name__ == '__main__':
    auth = Authentification(None)
        