# Modules qu'on importe pour le programme. Celui-ci comprend aussi les scripts que l'on a créé
from tkinter import *
from Fonctions import * # Pas utilisé pour le moment
from Traitement import *


class IHM(Frame):
    # Les widgets seront stockés ici en tant qu'attributs de cette fenêtre

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=200, **kwargs)
        self.pack()

        Frame1 = Frame(fenetre)
        Frame1.pack(side=TOP, padx=10, pady=10)
        Frame2 = Frame(fenetre)
        Frame2.pack(side=BOTTOM, padx=10, pady=10)

        # Widgets
        # Date de début
        self.labsearchde = Label(Frame1,text="Date début (ex : 2019-09-24)")
        self.labsearchde.pack()
        self.searchd = Entry(Frame1)
        self.searchd.pack(pady=10)
        # Date de fin
        self.labsearchf = Label(Frame1,text="Date Fin (ex : 2019-09-24)")
        self.labsearchf.pack()
        self.searchf = Entry(Frame1)
        self.searchf.pack(pady=10)
        # Localisation
        self.labsearchl = Label(Frame1,text="Localisation ")
        self.labsearchl.pack()
        self.searchl = Entry(Frame1)
        self.searchl.pack(pady=10)
        # Domaine(s)
        self.labsearchdo = Label(Frame1, text="Domaine(s) ")
        self.labsearchdo.pack()
        self.labsearchdo_info=Label(Frame1,text="(Si plusieurs domaines, les séparer par un '-')")
        self.labsearchdo_info.pack()
        self.searchdo = Entry(Frame1)
        self.searchdo.pack(pady=10)

        # Boutton "quitter"
        self.button_quit = Button(Frame1, text="Quit", command=self.quit)
        self.button_quit.pack(side=RIGHT,pady=20)
        # Boutton "sauvegarder"
        self.button_save = Button(Frame1,text="Save",command=self.button_save)
        self.button_save.pack(side=RIGHT,padx=5)
        # Boutton "rechercher"
        self.button_search = Button(Frame1,text="Search",command=self.button_search)
        self.button_search.pack(side=LEFT)

    def button_save(self):
        print("Boutton Sauvegarder")

    def button_search(self):
        print("Boutton Rechercher")
        g = Traitement(self.searchd.get(), self.searchf.get(), self.searchl.get(), self.searchdo.get())
        print(g)
        g.search()
