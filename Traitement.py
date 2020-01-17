# On importe les fonctions dans le script
from Fonctions import *

class Traitement():
    def __init__(self, deb,fin,lieu,dom):
        self.deb=deb
        self.fin=fin
        self.lieu=lieu
        self.dom=dom

    # Lance les fonctions de recherche selon les champs remplis
    def search(self):
        recherche_integrale(self.deb,self.fin,self.lieu,self.dom)

    # Elements affichés dans la console avec la recherche. Plus tard tout sera dans un msg Box
    def test_cont(self,test):
        if test=="":
            return str("Critère non communiqué")
        else:
            return str(test)

    # Elements retournés lorsque l'on lance la recherche
    def __str__(self):
        return "Voici vos critères de recherche | Date de début : "+self.test_cont(self.deb)+" | Date de fin : "\
               +self.test_cont(self.fin)+" | Localisation : "+self.test_cont(self.lieu)+" | Domaine(s) : "\
               +self.test_cont(self.dom)
