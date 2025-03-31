### partie du code charger de la recuperation des element de la pour la gerance de stokck de notre fameux restorant
import json

class gustopro:
    def __init__(self,resto):
        self.resto = resto
        print("restorant",{resto})
    def nsertion(self):
        add_nom = input("entree le nom du produit: ")
        nombre = input("quantite: ")
        types ={"boisson","episse","viende","legume","fruit","resette"}
        for i in types:
            print(i)


        e = input("entre le type du produit : ")

        print(e_check)
       
        while e not in e_check:
            print("type nos pris encharge")
            e = input("entre le type du produit : ")
            

        produit_list = {
            "mon":add_nom,
            "types":e,
            "quantite":nombre
        }

b0njour = gustopro("bonjor")
b0njour.nsertion()
