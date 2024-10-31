def New():
    name = input("\n Quel est le nom de la recette ? ")
    ingredients = input(" Quels ingredients sont nécéssaires ? (indiquer les quantités et séparer d'un '/') : ")
    description = input(" Fabrication : ")
    cuisson = input(" Temps de cuisson : ")

    with open(f"{name}.txt", 'w+') as file:
        file.write(name)
        file.write(f"\n{ingredients}")
        file.write(f"\n{description}")
        file.write(f"\n{cuisson}")
        print(f"\nVotre recette '{name}' a été ajoutée avec succès.")
        file.close()