from datetime import datetime

# Fonction pour compter le nombre d'éléments (pas forcément utlisée mais peut servir pour des tests) 
def compter_nb_elements(csvfichier):
    # On part de -1 pour ne pas compter la première qui sert pour les catégories
    elements = -1
    # On compte le nombre de lignes présentes dans le fichier csv
    for ligne in csvfichier:
        elements+=1
    return elements

# Fonction permettant de vérifier le format de la date mais pas utilisée & pas propre mais prend en compte totues les possibilités
def verif_date(d):
    if len(d) == 10:
        vd=datetime.now()
        dt=vd.strftime('%Y-%m-%d')
        print(dt)
        part=d[0]+d[1]+d[2]+d[3]
        partd=dt[0]+dt[1]+dt[2]+dt[3]
        if part.isdigit()==True and int(part)<int(partd):
            if d[4]=="-":
                part=d[5]+d[6]
                if int(part)<=12:
                    if part.isdigit()==True:
                        if d[7]=="-":
                            part=d[8]+d[9]
                            if part.isdigit()==True:
                                print(d+" est bien une date ")
                                return True
                            print("Format date incorrecte")
                            return False
                        print("Format date incorrect")
                        return False
                    print("Format date incorrect")
                    return False
                print("Format date incorrect")
                return False
            print("Format date incorrect")
            return False
        elif part.isdigit()==True and int(part)==int(partd):
            if d[4] == "-":
                part = d[5] + d[6]
                partd=d[5] + d[6]
                if int(part)<partd and part.isdigit()==True:
                    if d[7] == "-":
                        part = d[8] + d[9]
                        if part.isdigit() == True:
                            return True
                elif int(part)==partd and part.isdigit()==True:
                    if d[7] == "-":
                        part = d[8] + d[9]
                        partd=d[8] + d[9]
                        if part.isdigit()==True and int(part)<=partd:
                            return True

# Fonction vérifiant qu'un champ a du contenu
def remplissage(test):
    if test!="":
        return 1
    else:
        return 0
        
# Fonction permettant d'ouvrir un fichier csv et retourne deux valeurs         
def open_csv():
    import csv
    # csvfichier permet d'ouvrir le fichier csv /!\ il est souvent nécessaire d'utiliser le reader pour exploiter son contenu
    csvfichier = open(r'C:\Users\PTWV699\Documents\Python\Open Data Festival\panorama-des-festivals.csv',
                      encoding='utf-8', newline="")
    # Le reader nous permet d'avoir une liste sur plusieurs ligne comme dans un tableur. Elle permettra de faire des recherches dans le fichier CSV
    reader = csv.reader(csvfichier, delimiter=";")
    return csvfichier,reader

# Va retourner 1 au lieu de True venant de la fonction (autrement dit ne sert pas à grand chose) verif_fromtat_date
def verif_fromat_date(debut):
    if verif_date(debut) == True:
            return 1

# Vérifie le format du domaine pour savoir s'il y en a un ou deux
def verif_domaine(dom):
    dom1 = dom
    dom2 = ""
    if "-" in dom:
        chain=""
        critere = 2
        caract = len(dom)
        for i in range(0, caract):
            if dom[i] == "-":
                dom1 = chain
                chain = ""
            else:
                chain += dom[i]
        dom2 = chain
    else:
        critere=1
    return dom1,dom2,critere
