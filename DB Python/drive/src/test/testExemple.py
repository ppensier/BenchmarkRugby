'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

# -*- coding: Latin-1 -*-

import unittest

import bdd.gestionBdd

import metier.employe as employe
import bdd.exceptions as excpBdd
import metier.exceptions as excpMetier

class Test(unittest.TestCase):
    
    @classmethod
    def tearDownClass(cls):
        bdd.gestionBdd.suppression()
    @classmethod
    def setUpClass(cls):
        bdd.gestionBdd.creation()

    def testAjoutClient(self):
        employe.Employe.ajoutClient(self, 'Dus', 'Jean-Claude', '221 bis Beckerstreet Londres', True, '0798745341', 'jcdu29@laposte.net')
    
    def testEnregistrerBien(self):
        nom = "Banane"
        quantite = 10
        employe.Employe.enleverProduit(self, nom, quantite)
        self.assertRaises(excpMetier.ExceptionEntreeVide,employe.Employe.enleverProduit, "", quantite)
        # Entrée vide
        self.assertRaises(excpBdd.ExceptionContrainte,employe.Employe.enleverProduit, nom, 70)
        # Il y a 50 bananes dans la base de donnée, on ne peut donc pas en supprimer 70
        self.assertRaises(excpBdd.ExceptionFormatInadequat,employe.Employe.enleverProduit, "Banane", "20")
        # La quantité à supprimer est un nombre et non une chaîne de caractères

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAjoutClient']
    unittest.main()
    