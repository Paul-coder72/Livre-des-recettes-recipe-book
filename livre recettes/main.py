import os

from new import New
from print import Print
from modify import Modify
from read import Read

print("\nBienvenue sur votre livre de recettes \n 1. Ajouter une nouvelle recette  \n 2. Afficher la liste des recettes \n 3. Modifier une recette existante \n 4. Lire une recette ")

boucle = True
while boucle:

    rep1 = input("Que voulez-vous faire ? ")

    if rep1 == "1":
        New()

    elif rep1 == "2":
        Print()

    elif rep1 == "3":
        Modify()
                
    elif rep1 == "4":
        Read()


    print("")
    print("\n 1. Continuer \n 2. Quitter ")
    rep_boucle = input("\nVoulez-vous continuer? ")

    if rep_boucle == "1":
        boucle = True

    elif rep_boucle == "2":
        boucle = False
        print("\nAu revoir!")

input("\n")
