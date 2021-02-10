#coding:utf-8

from random import randint
SIGNES=["+","-","","//"]

def verifier(signe,a,b):
    if signe=="//":
        if b==1 or a%b!=0 :
            return False
        else:
            return True
    elif signe=="":
        if b==1:
            return False
        else:
            return True
    elif signe=="-":
        if a-b<=0:
            return False
        else:
            return True
    else:
        return True

def calculer(op,a,b):
    return eval(str("a"+op+"b"))

#print(calculer("+",4,5))

def choisir_operateur(a,b):
    r=randint(0,3)
    while verifier(SIGNES[r],a,b)!=True:
        r=randint(0,3)
    return SIGNES[r]

def essayer_calcul(liste_num,but):
    etapes=""
    copie_num=liste_num[:]
    for nb in range(5,1,-1):
        i=randint(0,nb)
        a=copie_num.pop(i)
        i=randint(0,nb-1)
        b=copie_num.pop(i)
        signe=choisir_operateur(a,b)
        print(a , " " , b)
        calcul=calculer(signe,a,b)
        etapes=etapes+str(a)+signe+str(b)+"="+str(calcul)+";"
        copie_num.append(calcul)
        print("bb")
        if (calcul==but):
            return calcul, etapes
    return False,False

def lancer_essais(liste_num,but,nb_essai):
    for i in range(nb_essai):
        essai,etapes=essayer_calcul(liste_num,but)
        if essai!=False:
            return essai
        else:
            if i==0:
                best=essai
            elif abs(but-essai) < best:
                best=abs(but-essai)
    return "Je n'ai pas trouvé la solution. Le meilleur résultat est", best

lancer_essais([6,2,4,3,7,9],56,50)