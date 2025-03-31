import os
import random

if os.path.exists("foods.txt"):
    with open("foods.txt","r+") as menudispo:
        print(menudispo.readline())
    menudispo.close()