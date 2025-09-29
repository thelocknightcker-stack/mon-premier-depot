import random
import math
# Historique des calculs
historique = []

# Fonctions de base
#Addition
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Erreur : Impossible de diviser par zéro."
    return a / b

# Fonctions avancées
def puissance(a, b):
    return a ** b

def racine_carre(a):
    if a < 0:
        return "Erreur : Impossible de calculer la racine carrée d'un nombre négatif."
    return math.sqrt(a)

def modulo(a, b):
    return a % b

# Mode scientifique
def sinus(x):
    return math.sin(math.radians(x))

def cosinus(x):
    return math.cos(math.radians(x))

def tangente(x):
    return math.tan(math.radians(x))

# Génération de nombres aléatoires
def nombre_aleatoire():
    return random.randint(1, 100)

# Demande à l'utilisateur s'il veut utiliser la calculatrice
def demander_utilisation():
    reponse = input("Bonjour, voulez-vous utiliser notre calculatrice ? (oui/non) : ").lower()
    if reponse != "oui":
        print("Merci de votre réponse, passez une bonne journée.")
        exit()

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Programme principal
demander_utilisation()

while True:
    print("\n----- Calculatrice -----")
    print("1. Addition (+)")
    print("2. Soustraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Puissance (^)")
    print("6. Racine carrée (√)")
    print("7. Modulo (%)")
    print("8. Mode Scientifique (sin, cos, tan)")
    print("9. Calculer une expression complète")
    print("10. Nombre aléatoire")
    print("11. Afficher l'historique")
    print("12. Quitter")
    
    choix = input("Choisissez une option : ")
    
    if choix == "1":
        a, b = get_number("Entrez le premier nombre : "), get_number("Entrez le deuxième nombre : ")
        resultat = addition(a, b)
    elif choix == "2":
        a, b = get_number("Entrez le premier nombre : "), get_number("Entrez le deuxième nombre : ")
        resultat = soustraction(a, b)
    elif choix == "3":
        a, b = get_number("Entrez le premier nombre : "), get_number("Entrez le deuxième nombre : ")
        resultat = multiplication(a, b)
    elif choix == "4":
        a, b = get_number("Entrez le premier nombre : "), get_number("Entrez le deuxième nombre : ")
        resultat = division(a, b)
    elif choix == "5":
        a, b = get_number("Entrez le nombre : "), get_number("Entrez l'exposant : ")
        resultat = puissance(a, b)
    elif choix == "6":
        a = get_number("Entrez un nombre : ")
        resultat = racine_carre(a)
    elif choix == "7":
        a, b = get_number("Entrez le premier nombre : "), get_number("Entrez le deuxième nombre : ")
        resultat = modulo(a, b)
    elif choix == "8":
        angle = get_number("Entrez un angle en degrés : ")
        print("Sinus :", sinus(angle))
        print("Cosinus :", cosinus(angle))
        print("Tangente :", tangente(angle))
        continue
    elif choix == "9":
        expression = input("Entrez une expression mathématique : ")
        try:
            resultat = eval(expression)
        except Exception as e:
            resultat = "Erreur dans l'expression !"
    elif choix == "10":
        resultat = nombre_aleatoire()
    elif choix == "11":
        print("\nHistorique des calculs :")
        for calcul in historique:
            print(calcul)
        continue
    elif choix == "12":
        print("Au revoir !")
        break
    else:
        print("Option invalide, veuillez réessayer.")
        continue
    #impréssion du résultat
    print("Résultat :", resultat)
    historique.append(f"{resultat}")



    print("test reussie")

