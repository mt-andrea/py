rec=[]
def f1(label):
    print(label)
    f=open("adatok.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(";")
        else:
            sor=sor.split(";")
        rec.append([sor[0],sor[1],int(sor[2]),int(sor[3])])
    txt="A fájl beolvasása...Kész."
    txt2="A dolgozók létszáma: "+str(len(rec))
    print("\t"+txt)
    print("\t"+txt2)
def f2(label):
    print(label)
    name=str(input("Kérek egy nevet: "))
    if name in [x[0] for x in rec]:
        i=0
        while rec[i][0]!=name:
            i+=1
        txt=rec[i][0]+" "+str(2020-rec[i][3])+" éve dolgozik a cégnél."        
    else:
        txt="Nincs ilyen nevű dolgozó."
    print("\t"+txt)
def f3(label):
    print(label)
    for i in range(len(rec)):
        if rec[i][2]<180000:
            txt=rec[i][0]+": "+str(rec[i][2])+" Ft"
            print("\t"+txt)
            f=open("emeles.txt","w")
            f.write(txt+"\n")
    txt="A fájl kiírása...kész!"
    print("\t"+txt)
def f4(label):
    print(label)
    for i in range(len(rec)):
        if rec[i][1]=="Abony" and rec[i][3]<2000:
            txt=rec[i][0]
            print("\t"+txt)
f1("1. feladat")
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")