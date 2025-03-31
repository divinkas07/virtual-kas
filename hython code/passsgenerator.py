# generateur de mot de passe avec python in grafical interface
# importation du modile tkiter
import string
from tkinter import* 
from random import randint ,choice
import pyperclip 
import os
import tkinter as tk
# autre modile pour le backend

def generator():
     passMax = 14
     passMin = 8
     caracteur = string.ascii_letters + string.punctuation + string.digits
     codegen = "".join(choice(caracteur) for x in range(randint(passMin,passMax))) # generation du pass
     inputtext.delete(0,END) # type: ignore
     inputtext.insert(0,codegen)
     return codegen
#la fonction pour copie le code  et le sauvegarde
def copy(): 
    try:
         Ccodegen = inputtext.get()
         codecheck = len(Ccodegen)
         if codecheck > 0:
           pyperclip.copy(Ccodegen)
           messlabel.config(text="code bien copier",fg="white",)
           print("le mot de passe est bien copie")
    except Exception as e: 
         messlabel.config(text="une erreur s'est produit:{e}",fg="red")
         print("une erreur est survenu")

def savepass():
    Sadegene = inputtext.get()
    savcheck = len(Sadegene)
    if Sadegene == inputtext.get() and savcheck > 0:
       save = open("Code history.txt","a+")
       save.write(f"le code est :{Sadegene}\n")
       save.close()
       messlabel.config(text ="code bien enregistre",fg="white")
       print("code enregistre")

    else:
       messlabel.config(text ="une erreur est survenu",fg="Red")
       print("une erreur est survenu")
 
### affichage des information de l'historique 
def historique():
    if os.path.exists("Code history.txt"): 
        with open("Code history.txt", "r") as savepassOn:
            donner = savepassOn.readlines()
        
        if not donner:
            print("Votre historique est vide")
        else:
            Wnhistorique = Toplevel(S_window)
            Wnhistorique.title("Historique des mots de passe")
            Wnhistorique.geometry("400x300")
            
            for index, sadegene in enumerate(donner, start=1):
                Label(Wnhistorique, text=f"Le code {index} est: {sadegene.strip()}", 
                      anchor="w", padx=10, pady=5).pack(fill=X)
    else: 
        print("Malheureusement, l'historique est indisponible")


#######################################3#############################################3
###################################################################################3##
#########################################################################################
######################################################################################
#creation de la premier feneter avec tk

S_window = tk. Tk()
BT1 = Frame(S_window)
BT1.pack(expand=YES)
BT1.config(background="#022e01")
S_window.geometry("600x400")
S_window.minsize(600,500)
S_window.title("Hi-passgenerator")
S_window.config(background="#022e01")
S_window.iconbitmap("hikas python/pngtree_reset_password_vector_png_image_7104484_Ek9_icon.ico")

BT2 = Frame(BT1,bg="black")
BT2.config(background="#022e01")

wth = 300
heigh = 300
img = PhotoImage(file="hikas python/pngtree-reset-password-vector-png-image_7104484.png").zoom(8).subsample(12)
Canva = Canvas(BT2,width=wth,height=heigh, bg="#022e01", bd = 0, highlightthickness= 0 )
Canva.create_image(wth/2,heigh/2 , image = img)
Canva.pack()

titre = Label(BT2, text="Password generator",font=("lucida",16),bg="#022e01",fg="white" )
titre.pack()

#input text
inputtext = Entry(BT2,font=("lucida",16),bg="black",fg="#04e900" )
inputtext.pack()
#boite de boutton
BT3 = Frame(BT2,bg="#022e01")
BT3.pack()
#boutton generateur
buttonC = Button(BT3, text="copier le code", bg="black",fg = "#04e900",command=copy)
buttonC.grid(row=0,column=1,pady=(10,20),padx=(10))
messlabel = Label(BT2,text="",font=("lucida",12),bg="#022e01",fg="white")
messlabel.pack()
## bouton du copier
buttonG = Button(BT3, text="generer un code", bg="black",fg = "#04e900",command = generator)
buttonG.grid(row=0,column=2,pady=(10,20), padx=(10))
#///
buttonS = Button(BT3, text="enregistre ce code", bg="black",fg = "#04e900",command = savepass)
buttonS.grid(row=0,column=3,pady=(10,20), padx=(10))
## insertion d'une image
BT2.grid(row=1,column=1, sticky=E)

Option = Menu(S_window)
barre_mani = Menu(Option, tearoff=0)
barre_mani.add_command(label="nouveau",command=generator)
histor = barre_mani.add_command(label="historique",command=historique)
barre_mani.add_command(label="quiter",command=S_window.quit)
Option.add_cascade(label="option" ,menu = barre_mani,background="#000d00",font=("monospace",16))

### fichier


S_window.config(menu=Option)

S_window.mainloop()
