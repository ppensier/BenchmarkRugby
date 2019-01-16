'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''

import psycopg2
import configparser
import keyring

import bdd.exceptions as excpBdd

conf = configparser.ConfigParser()
import os
print(os.getcwd())
#conf.read('./ventes2000.conf') # déploiement
# conf.read('../../ventes2000.conf') # tests
host="valilab.ensg.eu"
port="5432"
dbname="db_menut"
user="cmenut"
password="Cedric"


def ouvrirConnexion():
    """
    Connexion à une base de données
    """
    conn = psycopg2.connect("host=%s port=%s dbname=%s user=%s password=%s" % (host,port,dbname,user,password))
    # création d'un curseur pour accéder à cette base
    cur = conn.cursor()
    return (cur, conn)
    
def executerReq(cur, req, variables=None):
    """ 
    Requête à la base de données
    """
    try:
        cur.execute(req, variables)
    except psycopg2.DataError as de:
        raise excpBdd.ExceptionFormatInadequat() from de
    except psycopg2.IntegrityError as ie:
        raise excpBdd.ExceptionContrainte() from ie
    
def validerModifs(conn):
    conn.commit()
    
    
def fermerConnexion(cur, conn):
    """
    Fermeture de la connexion
    """
    cur.close()
    conn.close()

