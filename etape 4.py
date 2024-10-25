mdp = "ULAV"

message = """
La fin est proche. Ce n’est pas le moment d’abandonner.
"""

def grille(mdp):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVXYZ' # 'W' est remplace par 'V'
    carre = list(mdp)  # le mot de passe est au debut de la grille
    
    # ajouter les lettres restantes de l'alphabet
    for lettre in alphabet:
        if lettre not in carre:
            carre.append(lettre)
    # je convertit pour avoir la grille de 25 cases (5x5)
    grille = [carre[i:i+5] for i in range(0, 25, 5)]

    return grille

def polybe(message, grille):
    message = message.upper().replace(' ', '') # enleve les espaces et passe en majuscule
    message_chiffree = ''
    
    for lettre in message:
        # recherche des coordonnee de la lettre dans la grille
        for ligne in range(5): # parcours les lignes de la grille
            if lettre in grille[ligne]:
                colone = grille[ligne].index(lettre)
                message_chiffree += str(ligne + 1) + str(colone + 1) # les indices commencent a zero donc on fait +1
                break

    return message_chiffree

def frequence(message_chiffre):
    frequence = {}
    for chiffre in message_chiffre:
        if chiffre in frequence: # le chiffre est apparu donc on met +1 a sa valeur
            frequence[chiffre] += 1
        else:
            frequence[chiffre] = 1
            
    # on trouve le chiffre le plus frequent
    chiffre_apparu_le_plus = max(frequence, key=frequence.get)

    return chiffre_apparu_le_plus

grille_polybe = grille(mdp)
message_chiffre = polybe(message, grille_polybe)
chiffre_le_plus_frequent = frequence(message_chiffre)
print("Le message chiffre :", message_chiffre)
print("Le chiffre le plus frequent est :", chiffre_le_plus_frequent)
