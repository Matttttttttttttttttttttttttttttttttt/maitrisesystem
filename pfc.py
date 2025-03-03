#!/bin/python3
import random
choix = input("que choisissez-vous ? (pierre :1, feuille :2, ciseaux :3)")
choix_ordi = random.randint(1, 3)
print(choix_ordi)

if choix == 1 and choix_ordi == 2 or choix == 2 and choix_ordi == 3 or choix == 3 and choix_ordi == 1:
    print("perdu")
elif choix == choix_ordi:
    print("égalité")
else:
    print("gagné")
