##### progrmmme de getion d'un restorant 
#### getion d'un resto
import json
from tkinter import *
import customtkinter as ctk

class restorant():
    def __init__(self,nomrest,etoile):
        self.nomrest = nomrest
        self.etoile = int(etoile)

        if etoile <= 0 :
            print("veille mettre votre vrai reputatio")
        
    def insr_infomation(self):
        while True:
            try:
                nom = self.nomrest
                ville = input("entre la ville : ")
                quartier = input("entre le quartier : ")
                rue = int(input("entre la rue : "))
                reputation = ((f"{self.etoile} etoiles"))
                profile = input("veille entre le profile de restorant : " )
                information = {"nom du restoran": nom+"\n",
                                "ville residanciele ":ville+"\n",
                                "au quartier ":quartier+"\n",
                                "Rue ": f"{rue}\n",
                                "reputation ": (reputation)+"\n",
                                "profile ":profile}
                def saveinfo():
                        with open("Resinfo.json","w") as resinfo_jsn:
                            json.dump(information, resinfo_jsn)
               
                saveinfo() 
                break  
            except ValueError:
                print("erreur veiller bien verifier vos information !")
           
    def get_information(self):
        valeur = open("Resinfo.json","r")
        info = json.load(valeur)
        print(info)


        ctk.set_appearance_mode("system")
        ctk.set_default_color_theme("dark-blue")
#graficale
class window_apps(ctk.CTk):        
      def __init__(self):

        self.title("Hi-GustoPro")
        self.geometry("1000x700")
# constuiction du container
        self.container = ctk.CTkFrame(self, width=1000,height=700)
        self.container.pack(fill="both",expand=True)
       
       #diction d'hebergement des pages
        self.pages_base ={}
       #creation de page
        self.add_page("start_page",start_page)
        self.add_page("page1",page1)
        self.add_page("page2",page2)
        self.add_page("page3",page3)

        self.show_page("acceuille")

      self.show_page("start_page")

     def add_page(self,nom,conteiner):
        page =conteiner(self.container,self)
        self.pages[name] = page
        page.grid(row=0,colum=0,sticky="nsew")
           


window_apps()
window_apps.mainloop()