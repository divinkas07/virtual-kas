"""
 try to import the log 
 """
import os
def hikas_Mark():
    if os.path.exists("Arduino 328/HIKASHIKAS log.txt"):
        with open("Arduino 328/HIKASHIKAS log.txt",'r') as log:
            i = log.read()
        log.close()  
    else: 
        i = ("erreur du chargement du hikas...") 
        print(">>...lecture du ficher terminer ")
    print(i)

hikas_Mark()
