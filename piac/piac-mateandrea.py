rec=[]
def f1(label):
    print(label)
    f=open("piac.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(";")
        else:
            sor=sor.split(";")
        rec.append([sor[0],int(sor[1]),sor[2]])
    txt="A fájl belolvasása...kész!"
    txt2="A lista hossza: "+str(len(rec))
    print("\t"+txt)
    print("\t"+txt2)
def f2(label):
    print(label)
    txt="\tKérek egy hús nevet (tarja, karaj, comb, lapocka):"
    hus=input(txt)
    for i in range(len(rec)):
        if rec[i][0]==hus:
            txt=rec[i][2]
            print("\t"+txt)
def f3(label):
    print(label)
    c=0
    f=open("tarja.txt","w")
    for i in range(len(rec)):
        if rec[i][0]=="tarja":
            c+=rec[i][1]*1800
            f.write(rec[i][0]+";"+str(rec[i][1])+";"+rec[i][2]+"\n")
    txt="Gizike tarjára "+str(c)+" Ft-ot költött."
    print("\t"+txt)
    txt="A fájl kiírása... Kész!"
    print("\t"+txt)
f1("1. feladat")
f2("2. feladat")
f3("3. feladat")