#coding:utf-8

def conversionBinaire(nbre): #fonction repris d'un exercice avant
    """convertie decimal en binaire
    entrées: nbre du type int
    sortie: nbreBin du type string"""
    nbreBin = ''
    while nbre != 0:
        nbreBin = str(nbre % 2) + nbreBin
        nbre = nbre // 2
    if len(nbreBin) != 8:
        for i in range(8 - len(nbreBin)):
            nbreBin = "0" + nbreBin
    return nbreBin

def bitPoidsFort(nbre):
    nbreBin = conversionBinaire(nbre)
    return nbreBin[:4] + "0000"



def decale(nbreBin):
    return "0000" + nbreBin[:4]

def sommeBin(binA, binB,bit=8):
    """fait la somme de deux nombre binaire
    entrée: binA et binB de type str et bit de type int
    sortie: result de type str"""
    retenue = 0
    add = 0
    result = ''
    for i in range(bit):
        add = int(binA[(bit - 1)- i]) + int(binB[(bit - 1)- i]) + retenue
        if add == 0:
            result = '0' + result
            retenue = 0
        elif add == 1:
            result = '1' + result
            retenue = 0
        elif add == 2:
            result = '0' + result
            retenue = 1
        elif add == 3:   
            result = '1' + result
            retenue = 1
        else:
            print("oula, gros probleme x)")
    return result

def conversionDecimal(nbreBin):
    nbreFinal = 0
    i = len(nbreBin) - 1
    for bit in nbreBin:
        nbreFinal += int(bit) * (2**i)
        i -= 1
    return nbreFinal

def echangeBitFortFaible(nbreFort,nbreFaible):
    return conversionDecimal(sommeBin(bitPoidsFort(nbreFort),decale(bitPoidsFort(nbreFaible))))

def reconstitutionImage(nbre):
    nbre = conversionBinaire(nbre)
    nbre = nbre[4:] + "0000"
    nbre = conversionDecimal(nbre)
    return nbre

if __name__ == "__main__":
    print(conversionDecimal("11110000"))
    print(reconstitutionImage(15))