message = "JAMAIS DEUX SANS TROIS HAHAX"

matrice_cle = [
    [3, 7],
    [6, 3]
]

# trouve l'indice qui correspond aux lettres
def indice_lettres(lettre):
    return ord(lettre) - ord('A')

# trouve les lettres qui correspondent aux indices
def lettres_indice(indice):
    return chr(indice + ord('A'))

def message_prepare(message):
    message = message.replace(" ", "")  # enleve les espaces
    indices = [indice_lettres(lettre) for lettre in message]
    
    return indices

def hill(message, matrice_cle):
    message_chiffree = []
    #je coupe le message en block de 2 (pour pouvoir calculer les matrices)
    for i in range(0, len(message), 2):
        block = message[i:i+2]
        # somme des produit de la mtrice clé et de chque block
        chiffre1 = (matrice_cle[0][0] * block[0] + matrice_cle[0][1] * block[1]) % 26
        chiffre2 = (matrice_cle[1][0] * block[0] + matrice_cle[1][1] * block[1]) % 26
        message_chiffree.append(chiffre1)
        message_chiffree.append(chiffre2)

    return message_chiffree

message_prepare = message_prepare(message)
indices_chiffres = hill(message_prepare, matrice_cle)
message_chiffre = ''.join(lettres_indice(indice) for indice in indices_chiffres)
print("Message chiffre :", message_chiffre)