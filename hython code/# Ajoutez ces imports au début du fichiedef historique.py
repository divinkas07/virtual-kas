import customtkinter as ctk

# Initialisation de CustomTkinter
ctk.set_appearance_mode("light")  # Mode clair
ctk.set_default_color_theme("blue")  # Thème bleu

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configuration de la fenêtre principale
        self.title("Gestion des Pages")
        self.geometry("500x400")

        # Conteneur principal pour les pages
        self.container = ctk.CTkFrame(self, width=1050, height=800)
        self.container.pack(fill="both", expand=True)

        # Dictionnaire pour stocker les pages
        self.pages = {}

        # Ajouter les pages au conteneur
        self.add_page("Accueil", PageAccueil)
        self.add_page("Page 1", Page1)
        self.add_page("Page 2", Page2)

        # Afficher la page d'accueil
        self.show_page("Accueil")

    def add_page(self, name, page_class):
        """Ajoute une page au conteneur."""
        page = page_class(self.container, self)
        self.pages[name] = page
        page.grid(row=0, column=0, sticky="nsew")

    def show_page(self, name):
        """Affiche la page spécifiée."""
        page = self.pages.get(name)
        if page:
            page.tkraise()


# Page d'accueil
class PageAccueil(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Bienvenue sur l'accueil", font=("Arial", 20))
        label.pack(pady=20)

        button1 = ctk.CTkButton(self, text="Aller à la Page 1", command=lambda: controller.show_page("Page 1"))
        button1.pack(pady=10)

        button2 = ctk.CTkButton(self, text="Aller à la Page 2", command=lambda: controller.show_page("Page 2"))
        button2.pack(pady=10)


# Page 1
class Page1(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Page 1", font=("Arial", 20))
        label.pack(pady=20)

        button = ctk.CTkButton(self, text="Retour à l'accueil", command=lambda: controller.show_page("Accueil"))
        button.pack(pady=10)


# Page 2
class Page2(ctk.CTkFrame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        label = ctk.CTkLabel(self, text="Page 2", font=("Arial", 20))
        label.pack(pady=20)

        button = ctk.CTkButton(self, text="Retour à l'accueil", command=lambda: controller.show_page("Accueil"))
        button.pack(pady=10)


# Lancer l'application
if __name__ == "__main__":
    pp = App()
    
app.mainloop()















