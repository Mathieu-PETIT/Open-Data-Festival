# Import les fonctions de date
from datetime import datetime
import os
from Manifestation import *
from Domaine import *
from tkinter import messagebox


# Fonction pour compter le nombre d'éléments (pas forcément utlisée mais peut servir pour des tests)
def compter_nb_elements(csvfichier):
    # On part de -1 pour ne pas compter la première qui sert pour les catégories
    elements = -1
    # On compte le nombre de lignes présentes dans le fichier csv
    for ligne in csvfichier:
        elements+=1
    return elements

# Fonction permettant de vérifier le format de la date mais pas utilisée & pas propre mais prend en compte totues
# les possibilités
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

def create_bin(deb,fin,lieu,dom):
    b=0
    if remplissage(deb)==1:
       b+=1000
    if remplissage(fin)==1:
        b+=100
    if remplissage(lieu):
        b+=10
    if remplissage(dom):
        b+=1
    return b

# Fonction permettant d'ouvrir un fichier csv et retourne deux valeurs
def open_csv():
    import csv
    # csvfichier permet d'ouvrir le fichier csv /!\ il est souvent nécessaire d'utiliser le reader pour exploiter son
    # contenu
    csvfichier = open(r'C:\Users\PTWV699\Documents\Python\Open Data Festival\panorama-des-festivals.csv',
                      encoding='utf-8', newline="")
    # Le reader nous permet d'avoir une liste sur plusieurs ligne comme dans un tableur. Elle permettra de faire des
    # recherches dans le fichier CSV
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

# Fonctions qui va set les éléments dans la fonction et ajouter à un fichier texte le résultat de la recherche
def set_elements(ele):
    d=Domaine()
    g=Manifestation()
    d.set_dom1(ele[2]) # Ajoute le premier domaine à la classe Domaine
    d.set_dom2(ele[3]) # Ajoute le second domaine à la classe Domaine
    g.set_nom(ele[0]) # Ajoute le nom à la classe Manifestation
    g.set_site(ele[7]) # Ajoute le site à la classe Manifestation
    g.set_date_d(ele[12])  # Ajoute la date de début à la classe Manifestation
    g.set_date_f(ele[13])  # Ajoute la date de fin à la classe Manifestation
    g.set_com(ele[9]) # Ajoute la commune à la classe Manifestation
    g.set_com(d.dom1+" "+d.dom2)
    g.set_code(ele[23]) # Ajoute le code postal à la classe Manifestation
    ajoute_entree(g.get_nom()+" "+g.get_code()+" "+g.get_site()+" "+g.get_date_d()+" "+g.get_date_f()+" "+g.get_com()+" "+g.get_dom())
    print(g.get_nom()+" "+g.get_code()+" "+g.get_site()+" "+g.get_date_d()+" "+g.get_date_f()+" "+g.get_com()+" "+g.get_dom())

# Les fonctions traitements 0000 à 1111 correspondent aux différents cas possibles
def traitement_0000():
    print("Aucun critère sélectionné donc retourne tous les éléments du fichier")
    for row in open_csv()[1]:
        set_elements(row)

def traitement_0001(critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[2] == dom1 :
                set_elements(row)
        critere = 1

def traitement_0010(lieu):
    for row in open_csv()[1]:
        if row[1] == lieu :
            set_elements(row)

def traitement_0011(lieu,critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[1] == lieu and row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[1] == lieu and row[2] == dom1 :
                set_elements(row)
        critere = 1

def traitement_0100(fin):
    for row in open_csv()[1]:
        if row[13] == fin:
            set_elements(row)

def traitement_0101(fin,critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[13] == fin and row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[13] == fin and row[2] == dom1 :
                set_elements(row)
        critere = 1

def traitement_0111(fin,lieu,critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[13] == fin and row[1] == lieu and row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[13] == fin and row[1] == lieu and row[2] == dom1 :
                set_elements(row)
        critere = 1

def traitement_1000(deb):
    for row in open_csv()[1]:
        if row[12] == deb:
            set_elements(row)

def traitement_1001(deb,critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[12] == deb and row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[12] == deb and row[2] == dom1 :
                set_elements(row)
        critere = 1

def traitement_1010(deb,lieu):
    for row in open_csv()[1]:
        if row[12] == deb and row[1] == lieu:
            set_elements(row)

def traitement_1011(deb,lieu,critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[12] == deb and row[1] == lieu and row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[12] == deb and row[1] == lieu and row[2] == dom1 :
                set_elements(row)
        critere = 1

def traitement_1100(deb,fin):
    for row in open_csv()[1]:
        if row[12] == deb and row[13] == fin:
            set_elements(row)

def traitement_1101(deb,fin,critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[12] == deb and row[13] == fin and row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[12] == deb and row[13] == fin and row[2] == dom1 :
                set_elements(row)
        critere = 1

def traitement_1110(deb,fin,lieu):
    for row in open_csv()[1]:
        if row[12] == deb and row[13] == fin and row[1] == lieu:
                set_elements(row)

def traitement_1111(deb,fin,lieu,critere,dom1,dom2):
    for row in open_csv()[1]:
        if critere == 2:
            if row[12] == deb and row[13] == fin and row[1] == lieu and row[2] == dom1 and row[3] == dom2:
                set_elements(row)
        elif critere == 1:
            if row[12] == deb and row[13] == fin and row[1] == lieu and row[2] == dom1 :
                set_elements(row)
        critere = 1

def crea_fichier_txt():
    base = "search.txt"
    if os.path.isfile(base) == True:
        os.remove(base)
    fichier = open("search.txt", "x")

# Définit les différents cas possibles et exécute le cript associé
def recherche_integrale(deb,fin,lieu,dom):
    # Va chercher les informations
    dom1 = verif_domaine(dom)[0]
    dom2 = verif_domaine(dom)[1]
    critere = verif_domaine(dom)[2]
    binaire=create_bin(deb,fin,lieu,dom)

    crea_fichier_txt()

    # Vérifie le contenu des différents champs et exécute le script celui qui correspond
    if binaire==0:
        traitement_0000()
    elif binaire==1:
        traitement_0001(critere,dom1,dom2)
    elif binaire==10:
        traitement_0010(lieu)
    elif binaire==11:
        traitement_0011(lieu,critere,dom1,dom2)
    elif binaire==100:
        traitement_0100(fin)
    elif binaire== 101:
        traitement_0101(fin,critere,dom1,dom2)
    elif binaire==111:
        traitement_0111(fin,lieu,critere,dom1,dom2)
    elif binaire==1000:
        traitement_1000(deb)
    elif binaire==1001:
        traitement_1001(deb,critere,dom1,dom2)
    elif binaire==1010:
        traitement_1010(deb,lieu)
    elif binaire==1011:
        traitement_1011(deb,lieu,critere,dom1,dom2)
    elif binaire==1100:
        traitement_1100(deb,fin)
    elif binaire==1101:
        traitement_1111(deb,fin,critere,dom1,dom2)
    elif binaire==1110:
        traitement_1111(deb,fin,lieu)
    elif binaire==1111:
        traitement_1111(deb,fin,lieu,critere,dom1,dom2)

def nom():
    date = datetime.now()
    base = "Save"+(date.strftime('%d-%m-%Y')) + ".html"
    return base

def ajoute_entree(entree):
    fichier = open("search.txt", "a")
    fichier.write("\n"+entree)

def lecture_txt():
    fichier=open("search.txt","r")
    fichier.read()

def save_html():
    if os.path.isfile(nom())==True:
        os.remove(nom())
    if os.path.isfile('search.txt')==True:
        base=open(nom(),"a")
        liste=['search.txt']
        base.write("<html>")
        base.write("\n<p>")
        for ele in liste:
            with open(ele) as element:
                for ligne in element:
                    base.write(ligne)
        base.write("\n</p>")
        base.write("\n</html>")
        messagebox.showinfo("Sauvegarde", "Le fichier " + nom() + " a été créé dans le répertoire courant")
    else:
        messagebox.showinfo("Erreur", "Vous devez effectuer une recherche avant de lancer la sauvegarde")

def save_pdf():
    print("Test")

def delete_txt():
    if os.path.isfile("search.txt") == True:
        os.remove("search.txt")
