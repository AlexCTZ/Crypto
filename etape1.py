
alphabet=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

message_chiffree = """
YVCCF FLSFE AFLIA VEVJR ZJGRJ JZKLG RICVJ REXCR ZJFLW IRERZ JDRZJ TVHLV AVJRZ
JTVJK HLVKL MVLOF SKVEZ ILEVS FEEVE FKVGF LITVK IRMRZ CGIRK ZHLVC VJEFK VJJFE
KZDGF IKREK VJTVI KVJDR ZJTVE VJKGR JTVHL ZTFDG KVCVG CLJCV JJVEK ZVCTV JKUVG
IVEUI VGCRZ JZITV HLVKL WRZJR CFIJG IVEUJ LEVXI REUVZ EJGZI RKZFE TRIKL VERLI
RJSVJ FZEGF LIUTY ZWWIV ICVGI FTYRZ EDVJJ RXV
"""

def dechifrement_decalage(message):
    for decalage in range(1, 26):
        resultat = ""
        for lettre in message:
            if lettre.isalpha():
                index = alphabet.index(lettre)  
                nouvelle_lettre = alphabet[(index - decalage) % 26]
                resultat += nouvelle_lettre
            else:
                resultat += lettre

        print(f"cle de {decalage} : {resultat}\n")

dechifrement_decalage(message_chiffree)
