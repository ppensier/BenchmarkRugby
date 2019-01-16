'''
@author: Sibawaih Er-razki, Cédric Menut et Jean-françois Villeforceix
'''


import configparser
import tkinter
import tkinter.ttk as ttk
import keyring


def abandon():
    exit()
    
def configurer(host,port,user,passwd,dbname):
    conf = configparser.ConfigParser()
    conf['serveur'] = {'Host': host,'Port': port}
    conf['utilisateur'] = {'User': user}
    conf['base'] = {'DBname': dbname}
    keyring.set_password(host+"_"+dbname, user, passwd)
    # pour supprimer ce mot de passe :
    # keyring.delete_password(host+"_"+dbname, user)
    
    # with open('../ventes2000.conf', 'w') as configfile: # tests
    with open('./ventes2000.conf', 'w') as configfile: # déploiement
        conf.write(configfile)
        
    configfile.close()
    exit()

fenetre = tkinter.Tk()

fenetre.title("Configuration")

mainframe = ttk.Frame(fenetre) 
mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

host = tkinter.StringVar()
port = tkinter.StringVar()

user = tkinter.StringVar()
passwd = tkinter.StringVar()

dbname = tkinter.StringVar()

host_entry = ttk.Entry(mainframe, width=7, textvariable=host)
host_entry.grid(column=2, row=1, sticky=(tkinter.W, tkinter.E))

port_entry = ttk.Entry(mainframe, width=7, textvariable=port)
port_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))

user_entry = ttk.Entry(mainframe, width=7, textvariable=user)
user_entry.grid(column=2, row=3, sticky=(tkinter.W, tkinter.E))

passwd_entry = ttk.Entry(mainframe, width=7, textvariable=passwd, show="•")
passwd_entry.grid(column=2, row=4, sticky=(tkinter.W, tkinter.E))

dbname_entry = ttk.Entry(mainframe, width=7, textvariable=dbname)
dbname_entry.grid(column=2, row=5, sticky=(tkinter.W, tkinter.E))

ttk.Button(mainframe, text="Configurer", command=lambda: configurer(host.get(),port.get(),user.get(),passwd.get(),dbname.get())).grid(column=2, row=6, sticky=tkinter.W)
ttk.Button(mainframe, text="Abandonner", command=abandon).grid(column=1, row=6, sticky=tkinter.W)

ttk.Label(mainframe, text="Serveur").grid(column=1, row=1, sticky=tkinter.W)
ttk.Label(mainframe, text="Port").grid(column=1, row=2, sticky=tkinter.W)
ttk.Label(mainframe, text="Utilisateur").grid(column=1, row=3, sticky=tkinter.W)
ttk.Label(mainframe, text="Mot de passe").grid(column=1, row=4, sticky=tkinter.W)
ttk.Label(mainframe, text="Base de données").grid(column=1, row=5, sticky=tkinter.W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

host_entry.focus()
fenetre.bind('<Return>', lambda paraNonUtilise: configurer(host,port)) # le paramètre non utilisé est une instance de la classe Event

fenetre.mainloop()

