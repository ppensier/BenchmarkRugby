'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

# -*- coding: Latin-1 -*-

# La base de donnée contient 7 tables : Employe, Client, Commande, Emplacement, Magasin, Produit et Lien client-commande.
# Lancer la page pour créer la base de donnée sur le serveur.

import bdd.accesBdd as bdd
from pbkdf2 import crypt

def creation():
    cur, conn = bdd.ouvrirConnexion()
    
    # Employe 
    bdd.executerReq(cur, "CREATE TABLE employe(nom VARCHAR(20), prenom VARCHAR(20),login VARCHAR(20) PRIMARY KEY, mdp VARCHAR(50));")
    bdd.executerReq(cur,"INSERT INTO employe(nom,prenom,login,mdp) VALUES (%s, %s,%s,%s);",("durand","pierre","pdurand", crypt("Pierre")))
    bdd.executerReq(cur,"INSERT INTO employe(nom,prenom,login,mdp) VALUES (%s, %s,%s,%s);",("coty","rene","rcoty", crypt("Rene")))
    
    # Client
    bdd.executerReq(cur, "CREATE TABLE client(idc SERIAL PRIMARY KEY,nom VARCHAR(20) ,prenom VARCHAR(20) , adresse VARCHAR(200),accord_sub BOOL ,telephone VARCHAR(10) , adresse_mail VARCHAR(30) );")
    bdd.executerReq(cur,"INSERT INTO client(nom,prenom,adresse,accord_sub,telephone,adresse_mail) VALUES('Thiers','Adolphe','5 rue de la paix Paris' ,TRUE,'0789456123','toto.titi@gmail.com');")
    bdd.executerReq(cur,"INSERT INTO client(nom,prenom,adresse,accord_sub,telephone,adresse_mail) VALUES('Pompidou','Georges','50 avenue Wargame Paris',FALSE,'0312456789','mimi.ma@hotmail.fr');")
    bdd.executerReq(cur,"INSERT INTO client(nom,prenom,adresse,accord_sub,telephone,adresse_mail) VALUES('mali','malo','5 rue des orangers',TRUE,'0123456789','mali.molo@gmail.com');")
    
    # Commande
    bdd.executerReq(cur, "CREATE TABLE commande(idc SERIAL PRIMARY KEY,date_de_commande TIMESTAMP,date_de_livrasion TIMESTAMP, \
    faisabilite BOOL,chaine_de_course VARCHAR(500), en_preparation BOOL, prete BOOL, livree BOOL );")
    bdd.executerReq(cur, "INSERT INTO commande(date_de_commande, date_de_livrasion, faisabilite, chaine_de_course, en_preparation, prete, livree) VALUES ( \
    '2004-10-19 10:23:54', \
    '2004-10-25 16:20:00', \
    TRUE, \
    'Pain_de_campagne 3 Pain_au_lait 4 Confiture 2 Huile 1 Haricot 3 Poireau 2 Crabe 4 Rosbif 1 Champagne 2 Bière 4 Liégeois 5 Livarot 1', \
    FALSE,FALSE,FALSE);")
    bdd.executerReq(cur, "INSERT INTO commande(date_de_commande,date_de_livrasion,faisabilite,chaine_de_course,en_preparation, prete, livree) VALUES ( \
    '2004-10-22 10:23:54', \
    '2004-10-30 17:10:00', \
    TRUE, \
    'Toast 15 Biscuit 10 Moutarde 1 Prune 6 Betterave 2 Groseille 6 Maquereau 1 Côte_du_Rhône 6 Camembert 1 Fourme_d_Ambert 1', \
    FALSE,FALSE,FALSE);")
    bdd.executerReq(cur, "INSERT INTO commande(date_de_commande,date_de_livrasion,faisabilite,chaine_de_course,en_preparation, prete, livree) VALUES ( \
    '2004-10-25 10:23:54', \
    '2004-11-15 19:10:00', \
    TRUE, \
    'Crêpe 6 Miel 1 Rillettes 2 Noisette 10 Cabillaud 2 Roquefort 1 Soda 6 Tomme 1 Saucisse 3', \
    FALSE,FALSE,FALSE);")
    bdd.executerReq(cur, "INSERT INTO commande(date_de_commande,date_de_livrasion,faisabilite,chaine_de_course,en_preparation, prete, livree) VALUES ( \
    '2004-10-29 10:23:54', \
    '2004-10-30 16:20:00', \
    TRUE, \
    'Brioche 1 Ravioli 2 Farine 1 Cornichons 1 Colin 1 Jus_de_fruit 3 Cerise 15 Beurre 1 Gruyère 1', \
    FALSE,FALSE,FALSE);")
    bdd.executerReq(cur, "INSERT INTO commande(date_de_commande,date_de_livrasion,faisabilite,chaine_de_course,en_preparation, prete, livree) VALUES ( \
    '2004-11-02 10:23:54', \
    '2004-11-30 17:10:00', \
    TRUE, \
    'Chausson_aux_pommes 2 Terrine_de_campagne 1 Banane 6 Radis 10 Sirop 1 Munster 1 Chips 6 Madeleine 10', \
    FALSE,FALSE,FALSE);")
    # On trie les fonctions pour traiter en premier les commandes ayant ete effectue en premier
    bdd.executerReq(cur, "SELECT * FROM commande ORDER BY date_de_commande ASC;") 
    
    # Lien client-commande
    bdd.executerReq(cur,"CREATE TABLE lien_client_commande(idcl INT, idco INT)") 
    bdd.executerReq(cur,"INSERT INTO lien_client_commande(idcl,idco) VALUES (1,1)")
    bdd.executerReq(cur,"INSERT INTO lien_client_commande(idcl,idco) VALUES (1,2)")
    bdd.executerReq(cur,"INSERT INTO lien_client_commande(idcl,idco) VALUES (3,3)")
    bdd.executerReq(cur,"INSERT INTO lien_client_commande(idcl,idco) VALUES (2,4)")
    bdd.executerReq(cur,"INSERT INTO lien_client_commande(idcl,idco) VALUES (1,5)")
    
    # Magasin
    bdd.executerReq(cur,"CREATE TABLE magasin(idm SERIAL PRIMARY KEY,nom VARCHAR(20), role VARCHAR(20));")
    bdd.executerReq(cur, "INSERT INTO magasin(nom,role) VALUES ('Super_Drive','entrepot');")
    bdd.executerReq(cur, "INSERT INTO magasin(nom,role) VALUES ('Super_Drive','magasin_public');")
    
    # Emplacement
    bdd.executerReq(cur,"CREATE TABLE emplacement(ide SERIAL PRIMARY KEY, geographie VARCHAR(30),nom VARCHAR(30),categorie VARCHAR(30),capacite INT);")
    bdd.executerReq(cur, "INSERT INTO emplacement(geographie,nom,categorie,capacite) VALUES ('Nord-Ouest','zone_A','fruit_legume',2000);")
    bdd.executerReq(cur, "INSERT INTO emplacement(geographie,nom,categorie,capacite) VALUES ('Nord-Est','zone_B','viande_poisson',2500);")
    bdd.executerReq(cur, "INSERT INTO emplacement(geographie,nom,categorie,capacite) VALUES ('Sud-Ouest','zone_C','boisson',1000);")
    bdd.executerReq(cur, "INSERT INTO emplacement(geographie,nom,categorie,capacite) VALUES ('Sud-Est','zone_D','depot_commande',400);")
    bdd.executerReq(cur, "INSERT INTO emplacement(geographie,nom,categorie,capacite) VALUES ('Sud','zone_E','epicerie_patisserie',3000);")
    bdd.executerReq(cur, "INSERT INTO emplacement(geographie,nom,categorie,capacite) VALUES ('Nord','zone_F','laitier_fromage',2000);")
    
    # Produit
    bdd.executerReq(cur,"CREATE TABLE produit(idp SERIAL PRIMARY KEY, nom varchar(30), categorie varchar(20),volume INT,poids INT,stock_virtuel INT ,stock_reel INT,frais BOOL);")
    #epicerie_patisserie
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_de_campagne','epicerie_patisserie', 1 , 400 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_de_mie','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_à_sandwich','epicerie_patisserie', 1 , 330 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Baguette','epicerie_patisserie', 1 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_brioché','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_complet','epicerie_patisserie', 1 , 300 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_aux_céréales','epicerie_patisserie', 1 , 350 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Biscotte','epicerie_patisserie', 1 , 400 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Toast','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_au_lait','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Crêpe','epicerie_patisserie', 0.2 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Gaufre','epicerie_patisserie', 0.5 , 350 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_au_chocolat','epicerie_patisserie', 0.5 , 300 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Brownie','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Brioche','epicerie_patisserie', 1 , 600 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Muffin','epicerie_patisserie', 0.5 , 300 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Croissant','epicerie_patisserie', 0.5 , 400 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pain_au_raisin','epicerie_patisserie', 0.5 , 400 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Chausson_aux_pommes','epicerie_patisserie', 0.5 , 400 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Beignet','epicerie_patisserie', 0.5 , 400 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Tablette_de_chocolat','epicerie_patisserie', 0.2 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Barre_chocolatée','epicerie_patisserie', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Café','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Thé','epicerie_patisserie', 0.5 , 40 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pâte à tartiner','epicerie_patisserie', 1 , 600 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Miel','epicerie_patisserie', 0.5 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Confiture','epicerie_patisserie', 0.5 , 350 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Céréale','epicerie_patisserie', 1 , 450 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Biscuit','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Madeleine','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pâte_de_fruit','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Cake','epicerie_patisserie', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Sucre','epicerie_patisserie', 0.5 , 1000 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Compote','epicerie_patisserie', 1 , 500 , 50 , 55 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Farine','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Crème_dessert','epicerie_patisserie', 0.5 , 250 , 50 , 55 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Lentille','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pâtes','epicerie_patisserie', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Ravioli','epicerie_patisserie', 0.5 , 1000 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pizza','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Chips','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Riz','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Cassoulet','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Sauce_tomate','epicerie_patisserie', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Champignon','epicerie_patisserie', 0.5 , 1000 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Terrine_de_campagne','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Rillettes','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Soupe','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Sel','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Poivre','epicerie_patisserie', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Moutarde','epicerie_patisserie', 0.5 , 300 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Ketchup','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Huile','epicerie_patisserie', 1 , 500 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Cornichons','epicerie_patisserie', 0.5 , 250 , 50 , 55 , FALSE);")
    #fruit_legume
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Orange','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Abricot','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pêche','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pomme','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Banane','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Ananas','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Prune','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Raisin','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Cerise','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Fraise','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Framboise','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Kiwi','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pamplemousse','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Noisette','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Figue','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Noix','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Tomate','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pomme_de_terre','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Betterave','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Choux','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Endive','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Salade','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Radis','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Haricot','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Artichaut','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Poivron','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Courgette','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Poireau','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Poire','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Fenouille','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Cacahuète','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Groseille','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Petit_pois','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Carotte','fruit_legume', 0.5 , 200 , 50 , 55 , FALSE);")
    #viande_poisson
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Dorade','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Cabillaud','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Sole','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Lotte','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Sardine','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Crabe','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Carrelet','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Langouste','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Crevette','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Gambas','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Poulpe','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Saint-Pierre','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Merlan','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Huître','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Moule','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Limande','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Bar','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Thon','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Truite','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Saumon','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Oursin','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Maquereau','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Espadon','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Caviar','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Colin','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Raie','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Bifteck','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Poulet','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Canard','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Dinde','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Jambon','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Saucisson','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Saucisse','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Pâté','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Escaloppe_de_veau','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Côte_de_boeuf','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Rosbif','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Entrecôte','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Steak_hâché','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Paupiette','viande_poisson', 0.3 , 150 , 50 , 50 , TRUE);")
    #boisson
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Vin_de_Bordeaux','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Champagne','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Beaujolais','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Côte_du_Rhône','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Rosé_de_Provence','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Eau_minérale','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Soda','boisson', 0.5 , 750 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Jus_de_fruit','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Sirop','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Eau_pétillante','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Bière','boisson', 0.75 , 1000 , 50 , 50 , FALSE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Alcool','boisson', 1.5 , 2000 , 50 , 50 , FALSE);")
    #laitier_fromage
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Camembert','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Brie','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Coulommiers','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Roquefort','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Saint-Nectaire','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Gruyère','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Comté','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Beaufort','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Emmental','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Tomme','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Chèvre','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Crème_fraîche','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Livarot','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Munster','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Maroilles','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Bleu_d_Auvergne','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Cantal','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Fourme_d_Ambert','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Mimolette','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Gouda','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Mozzarella','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Mascarpone','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Reblochon','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Beurre','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Lait','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Oeuf','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Margarine','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Yaourt_nature','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Glace','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Liégeois','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Yaourt_aux_fruits','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Mousse_au_chocolat','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    bdd.executerReq(cur,"INSERT INTO produit(nom,categorie,volume,poids,stock_virtuel,stock_reel,frais) VALUES('Parmesan','laitier_fromage', 0.3 , 150 , 50 , 50 , TRUE);")
    
    bdd.validerModifs(conn)
    bdd.fermerConnexion(cur, conn)
    
    
    
def suppression():
    cur, conn = bdd.ouvrirConnexion()
    
    # Employe
    bdd.executerReq(cur, "DROP TABLE employe;")
    # Client
    bdd.executerReq(cur, "DROP TABLE client;")
    # Commande
    bdd.executerReq(cur, "DROP TABLE commande;")
    # Emplacement
    bdd.executerReq(cur, "DROP TABLE emplacement;")
    # Magasin
    bdd.executerReq(cur, "DROP TABLE magasin;")
    # Produit
    bdd.executerReq(cur, "DROP TABLE produit;")
    # Lien client-commande
    bdd.executerReq(cur, "DROP TABLE lien_client_commande;")
    
    bdd.validerModifs(conn)
    bdd.fermerConnexion(cur, conn)
    
suppression()
creation()