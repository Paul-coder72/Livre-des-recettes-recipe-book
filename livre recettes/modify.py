import os

def Modify():
    name = input("\n Quel est le nom de la recette à modifier? ")
    if os.path.isfile(f"{name}.txt"):
        with open(f"{name}.txt", 'r') as file:
            name = file.readline().strip()
            ingredients = file.readline().strip()
            description = file.readline().strip()
            cuisson = file.readline().strip()
            print(f"\nVoici les informations de la recette '{name}':")
            print(f"  [1] Nom : {name}")
            print(f"  [2] Ingredients : {ingredients}")
            print(f"  [3] Description : {description}")
            print(f"  [4] Temps de cuisson : {cuisson}")
            rep2 = input("\nQue voulez-vous modifier? (1/2/3/4) ")

            if rep2 == "1":
                new_name = input("Nouveau nom : ")
                with open(f"{name}.txt", 'w+') as f:
                    f.write(f"{new_name}")
                    f.write(ingredients)
                    f.write(description)
                    f.write(cuisson)
                    print(f"\nLe nom a bien été modifié")
                    f.close()

            elif rep2 == "2":
                new_ingredients = input("Nouveaux ingredients : ")
                with open(f"{name}.txt", 'w+') as f:
                    f.write(name)
                    f.write(f"{new_ingredients}")
                    f.write(description)
                    f.write(cuisson)
                    print(f"\nLes ingredients de la recette '{name}' ont été modifiés avec succès.")
                    f.close()

            elif rep2 == "3":
                new_description = input("Nouvelle description : ")
                with open(f"{name}.txt", 'w+') as f:
                    f.write(name)
                    f.write(ingredients)
                    f.write(f"{new_description}")
                    f.write(cuisson)
                    print(f"\nLa description de la recette '{name}' a été modifiée avec succès.")
                    f.close()

            elif rep2 == "4":
                new_cuisson = input("Nouveau temps de cuisson : ")
                with open(f"{name}.txt", 'w+') as f:
                    f.write(name)
                    f.write(ingredients)
                    f.write(description)
                    f.write(f"{new_cuisson}")
                    print(f"\nLe temps de cuisson de la recette '{name}' a été modifié avec succès.")