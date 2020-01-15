# On importe les fonctions dans le script
from Fonctions import *

class Traitement():
    def __init__(self, deb,fin,lieu,dom):
        self.deb=deb
        self.fin=fin
        self.lieu=lieu
        self.dom=dom

    # Définit les états possibles des champs sous une forme de binaire
    def calcul_binaire(self):
        binaire=0
        if remplissage(self.deb)==1:
            binaire+=1000
        if remplissage(self.fin)==1:
            binaire+=100
        if remplissage(self.lieu)==1:
            binaire+=10
        if remplissage(self.dom)==1:
            binaire+=1
        return binaire

    # Fait la recherche en fonction des dates uniquement (pas encore utilisée et à déplacer dans Fonctions)
    def recherche_dates(self):
        debut = ""
        finn = ""

        for row in open_csv()[1]:
            if verif_fromat_date(self.deb) == 1:
                if row[12] == self.deb:
                    debut = self.deb
            else:
                print("Format de date incorrect")
            if verif_fromat_date(self.fin) == 1:
                if row[13] == self.fin:
                    finn = self.fin
            else:
                print("Format de date incorrect")

        return debut + " " + finn

    # Lance les fonctions de recherche selon les champs remplis
    def search(self):
        binaire=int(self.calcul_binaire())

        if binaire==1111:
            print(recherche_integrale(self.deb,self.fin,self.lieu,self.dom))

        # elif binaire==1110:
        #     return self.recherche_dates_lieu()
        # elif binaire==1101:
        #     return self.recherche_dates_domaine()
        # elif binaire==1100:
        #     return self.recherche_dates()
        # elif binaire==1011:
        #     return self.recherche_debut_lieu_domaine()
        # elif binaire==1010:
        #     return self.recherche_debut_lieu()
        # elif binaire==1001:
        #     return self.recherche_debut_domaine()
        # elif binaire==1000:
        #     return self.recherche_debut()
        # elif binaire==111:
        #     return self.recherche_fin_lieu_domaine()
        # elif binaire==110:
        #     return self.recherche_fin_lieu()
        # elif binaire==101:
        #     return self.recherche_fin_dom()
        # elif binaire==100:
        #     return self.recherche_fin()
        # elif binaire==11:
        #     return self.recherche_lieu_domaine()
        # elif binaire==10:
        #     return self.recherche_lieu()
        # elif binaire==1:
        #     return self.recherche_domaine()
        elif binaire==0:
            return self.recherche_vide()

    # Elements affichés dans la console avec la recherche. Plus tard tout sera dans un msg Box
    def test_cont(self,test):
        if test=="":
            return str("Critère non communiqué")
        else:
            return str(test)

    # Elements retournés lorsque l'on lance la recherche
    def __str__(self):
        return "Voici vos critères de recherche | Date de début : "+self.test_cont(self.deb)+" | Date de fin : "+self.test_cont(self.fin)+" | Localisation : "+self.test_cont(self.lieu)+" | Domaine(s) : "+self.test_cont(self.dom)
