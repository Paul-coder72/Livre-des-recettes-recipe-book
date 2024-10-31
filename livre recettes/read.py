import os

def Read():
    name = input("\n Quel est le nom de la recette à lire? ")
    if os.path.isfile(f"{name}.txt"):
        with open(f"{name}.txt", 'r') as file:
            print(f"\nVoici les informations de la recette '{name}':")
            print(f"  Nom : {file.readline().strip()}\n")
            print(f"  Ingredients : {file.readline().strip()}\n")
            print(f"  Description : {file.readline().strip()}\n")
            print(f"  Temps de cuisson : {file.readline().strip()}\n")
            file.close()