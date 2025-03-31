### creatio d'un fichier avec python and python
# ok let go
import os
import random
food = ["foufou","poisson","pome de terre","viende","salade","poulet"]
with open("foods.txt","w") as repas:
    for Fooding in food:
        repas.write(Fooding+"\n")
    repas.close()

if os.path.exists("foods.txt"):
    with open("foods.txt","+r") as menudispo:
     resmenu = menudispo.readlines()
     choix =  random.choice(resmenu)
    menudispo.close()
    print("hiai vous prpose le ",choix," pour votre bonne nutrition")
else : 
    print("ce fichier est introuvable")