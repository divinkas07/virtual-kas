### Simulation d'une ville virtuelle
# Une classe mère appelée Batiment et les autres classes enfants

class Ville:  # Renommé en majuscule pour suivre la convention PEP 8
    def __init__(self, nom, population, superficie):
        self.nom = nom
        self.population = population
        self.superficie = superficie

class Batiment:  # Retiré l'héritage de Ville car un bâtiment n'est pas une ville
    def __init__(self, nom, adresse, etage):
        self.nom = nom
        self.adresse = adresse
        self.etage = etage

    def visiter(self):
        print(f"Je visite {self.nom} à l'adresse {self.adresse} en étant sur l'étage {self.etage}")

class Banque(Batiment):  # Renommé en français et majuscule
    def __init__(self, nom, adresse, etage):
        super().__init__(nom, adresse, etage)
        self.nombre_clients = 0

    def aclient(self):
        return super().visiter()

class Supermarche(Batiment):  # Fusionné supermarche1 et supermarche2
    def __init__(self, nom, adresse, etage):
        super().__init__(nom, adresse, etage)
        self.produits = {}

    def visiter(self):
        return super().visiter()

class Hotel(Batiment):  # Renommé au singulier
    def __init__(self, nom, adresse, etage, etoile):
        super().__init__(nom, adresse, etage)
        self.etoile = etoile

    def visiter(self):
        return super().visiter()

    def __str__(self):  # Ajouté une méthode __str__ pour l'affichage
        return f"Hôtel {self.nom}, {self.etoile} étoiles, à l'adresse {self.adresse}"

# Test du code
kalemie = Ville("Kalemie", 1000, 5000)
tcham_hotel = Hotel("Tcham Hotel", "2000 Rue Principale", 3, 4)
tcham_hotel.visiter(    )
#rint(tcham_hotel.visiter())
kalemie= Batiment(nom, adresse, etage)visiter()

