message_chiffree= """
ILAPU AVCUZ XBIPP WJLZI FC2IF FIPCQ QCVZL CUSRA UCUJA VZUCS APUCP IEHEP
CZQCU EPCKE CZEIJ IVSCP IUXIV ULCUZ IFCUE VFCES AQQCL CVWJC IEXCX WHHWS
ELZXC UZFXC SCSAE PUXIW LLCEP UWLYI SAQNW CVXCZ FFAEP SCSAE PU
"""

cle_possible_a = [2,3,5,7,11,13,17,19,23]
cle_possible_b = range(26)

def pgcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, n):
    return pow(a, -1, n)

def dechiffrement_affine(message, a, b):
    resultat = ""
    m = 26
    inverse_a = mod_inverse(a, m)
    if inverse_a is None:
        return None
    
    for lettre in message:
        if lettre.isalpha():
            x = ord(lettre) - ord('A')
            nouvelle_lettre = (inverse_a * (x - b)) % m
            resultat += chr(nouvelle_lettre + ord('A'))
        else:
            resultat += lettre
    return resultat

for a in cle_possible_a:
    if pgcd(a, 26) == 1:
        for b in cle_possible_b:
            message_dechiffree = dechiffrement_affine(message_chiffree, a, b)
            print(f"a={a} et b={b}: {message_dechiffree}")
