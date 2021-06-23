nevek = ["Albert", "Arany", "Árva", "Ázsok", "Balogh", "Cilei", "Csaba", 
"Dömsödi", "Endrei", "Érmelléki", "Fejes", "Fitos", "Göröcs", "Gyulai", 
"Hajnal", "Hence", "István", "Jakab", "Kajtos", "Kaszás", "Ligeti", 
"Makács", "Nagy", "Nyúl", "Orosz", "Ördög", "Ötvös", "Pálos", "Rajna", 
"Rozsom", "Sebes", "Szigeti", "Tisza", "Ujvári", "Vidák", "Zala", "Zsobó"]

nemek = ["L", "L", "L", "F", "F", "F", "F", "F", "L", "L", "F", "F", 
"L", "L", "L", "L", "F", "F", "L", "F", "F", "L", "L", "L", "F", "F", 
"L", "L", "L", "F", "F", "L", "L", "L", "L", "L", "F"]

forintok = [3362, 1175, 1754, 3504, 3908, 4195, 1013, 3139, 3628, 4524, 
1747, 3523, 4905, 2885, 3609, 3990, 2013, 1074, 3882, 2199, 2579, 3993, 
3321, 1375, 4332, 2825, 4768, 3471, 2698, 4314, 2263, 1653, 2488, 2701, 
3845, 3831, 1816]

def f1(label):
    print(label)
    cf=0
    for i in range(len(nevek)):
        if nemek[i]=="F":
            cf+=1
    txt="Fiúk létszáma: "+str(cf)
    print("\t",txt)
    txt="Lányok létszáma: "+str(len(nevek)-cf)
    print("\t",txt)
def f2(label):
    print(label)
    maxInd=0
    for i in range(len(nevek)):
        if forintok[i]>forintok[maxInd]:
           maxInd=i
    txt="A legtöbb osztálypénz: "+nevek[maxInd]+" "+str(forintok[maxInd])+" Ft" 
    print("\t",txt)
def f3(label):
    print(label)
    print("\tLétszám: "+str(len(nevek)))
def f4(label):
    print(label)
    print("\t4000 Ft-nál többet fizettek be: ")
    for i in range(len(nevek)):
        if forintok[i]>4000:
            print("\t"+nevek[i])
def f5(label):
    print(label)
    szum=0
    for i in range(len(nevek)):
        szum+=forintok[i]
    print("\tösszeg: "+str(szum))
def f6(label):
    print(label)
    i=0
    while nevek[i]!="Makács":
        i+=1
    print("\tMakács befizetése: "+str(forintok[i])+" Ft")
def f7(label):
    print(label)
    print("\t 2000-2500 Ft között hoztak be: ")
    c=0
    for i in range(len(nevek)):
        if forintok[i]>2000 and forintok[i]<2500:
            print("\t"+nevek[i])
            c+=1
    if c==0:
        print("Nincs ilyen tanuló")
    print("\t (TESZT)800-1000 Ft között hoztak be: ")
    c=0
    for i in range(len(nevek)):
        if forintok[i]>800 and forintok[i]<1000:
            print("\t"+nevek[i])
            c+=1
    if c==0:
        print("\tNincs ilyen tanuló")
def f8(label):
    print(label)
    i=0
    while i<len(nevek) and forintok[i]!=2000:
        i+=1
    if i<len(nevek):
        print("\tVan olyan tanuló, aki pontosan 2000 Ft-ot fizetett be")
    else:
        print("\tNincs ilyen tanuló")
    print("TESZT")
    i=0
    while i<len(nevek) and forintok[i]!=1175:
        i+=1
    if i<len(nevek):
        print("\tVan olyan tanuló, aki pontosan 1175 Ft-ot fizetett be")
    else:
        print("\tNincs ilyen tanuló")
def f9(label):
    print(label)
    l=0
    s=0
    for i in range(len(nevek)):
        if nemek[i]=="L":
            l+=1
            s+=forintok[i]
    print("\tLányok átlaga: "+str(round(s/l,1))+" Ft")
def f10(label):
    print(label)
    j=0
    while nemek[j]=="F":
        j+=1
    minInd=j
    for i in range(j,len(nemek)):
        if nemek[i]=="F" and forintok[i]<forintok[minInd]:
            minInd=i
    print("\t"+nevek[minInd]+" "+str(forintok[minInd])+" Ft")
f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5("5.feladat")
f6("6.feladat")
f7("7.feladat")
f8("8.feladat")
f9("9.feladat")
f10("10.feladat")