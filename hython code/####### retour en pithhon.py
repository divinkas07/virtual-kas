###### salut mon  et divin kas et la dans cette exercise nous allons ensemble faire uun programmme en python
# notre porgramme cosiste a enregistrer les eleve dans une base de donne pui le recuperer pui le verifier pour l'autantifivcation::
# we are creat any progrramme for consliting and checking a id for pupils
# hti a composition for howe programme structure of python
# declaration of global variables:

username = input("Nom complet de l'élève : ")
agepepol = int(input("Âge de l'élève : "))

if agepepol <= 23 and agepepol > 10: 
    print("Vous êtes mieux placé pour bosser !!!")
    
    degree = ["fest", "second", "third", "lastdegree"]  # Voici la liste de degrés
    
    # Afficher les options de degré
    print("Choisissez le degré de l'élève :")
    for i, deg in enumerate(degree, 1):
        print(f"{i}. {deg}")
    
    # Demander à l'utilisateur de choisir
    while True:
        choice = input("Entrez le numéro correspondant au degré (1-4) : ")
        if choice.isdigit() and 1 <= int(choice) <= len(degree):
            pepoldegree = degree[int(choice) - 1]
            print(f"Degré choisi : {pepoldegree}")
            break
    
        else:
            print("Choix invalide. Veuillez entrer un numéro entre 1 et 4.")
else:
    print("L'âge de l'élève doit être compris entre 11 et 23 ans.")


for nombreprpol in range(1,1): 
    print(username+" vous etez l'eleve numeo: "+ str(nombreprpol))

###
day = int(input("jour :"))
#year = int((""))
insmonth = ["novembre","decembre","jenvier"]
for e, month in enumerate(insmonth,1):
    print(f"{e}.{month}")

mothchose = input("veille indiquer votre moi d'inscription(1-3) :")
if mothchose.isdigit() and 1 <= int(mothchose) <= len(insmonth):
   moi_ins = insmonth[int(mothchose) -1]
   print(f"vous vous etez inscrit en :{moi_ins}") 
if day < 1  or  day >= 25:
    print("cela ne pas une date d'ouverture")  
else:
  print("l'eleve "+username+" est bien enregistre le "+str(day) +"/"+ moi_ins +"/2025")
useerclass = input("inserer votre scolarclass ")
while scolar_class  >= 1000 :
   scolar_class = useerclass * 1.5
   print("calcul scolar class quivaux a "+str(scolar_class)+" et votre scolarclass ")

class scolar:
 def __init__(self,nom,degtt)
    