import os

def Print():
    print("\nVoici la liste des recettes : \n")
    for file in os.listdir():
        if file.endswith(".txt"):
            with open(file, 'r') as f:
                print(f.readline().strip())
                f.close()