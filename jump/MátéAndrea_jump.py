rec=[]
def inpFile(file,lista):
    f=open(file,"r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor = sor[:-1].split(";")
        else:
            sor = sor.split(";")
        lista.append([str(sor[0]),str(sor[1]),int(sor[2]),int(sor[3]),int(sor[4]),int(sor[5]),int(sor[6]),int(sor[7]),int(sor[8])])
    txt="A fájl beolvasása...Kész!"
    print("\t"+txt)
def legjobb(i):
    maxInd=3
    for j in range(3,len(rec[i])):
        if rec[i][j]>rec[i][maxInd]:
            maxInd=j
    return rec[i][maxInd]
def writeFile(file):
    f=open(file,"w")
    for i in range(len(rec)):
        txt=rec[i][0]+": "+str(legjobb(i))+" cm\n"
        f.write(txt)
    txt="A fájl kiírása...Kész!"
    print("\t"+txt)
def hanyadik_ugras(name):
    i=0
    while rec[i][0]!=name:
        i+=1
    j=0
    while legjobb(i)!=rec[i][j]:
        j+=1
    txt=name+" legjobb ugrása "+str(j+1)+". ugrása."
    print("\t"+txt)
def csapat_pont(name):
    pont=0
    for i in range(len(rec)):
        if rec[i][1]==name:
            pont+=legjobb(i)
    txt=name+" "+str(pont)+" pontot szerzett."
    print("\t"+txt)
def f1(label):
    print(label)
    inpFile("adatok.txt",rec)
def f2(label):
    print(label)
    txt=str(len(rec))+" rekord van az adatbázizban."
    print("\t"+txt)
def f3(label):
    print(label)
    writeFile("lebjobbak.txt")
def f4(label):
    print(label)
    hanyadik_ugras("Libert Roland")
def f5(label):
    print(label)
    txt="Egyéni csúcsot utrottak: "
    print("\t"+txt)
    for i in range(len(rec)):
        if rec[i][2]<legjobb(i):
            txt=rec[i][0]
            print("\t"+txt)
def f6(label):
    print(label)
    csapat_pont("Baranya")
def f7(label):
    print(label)
    c=0
    for i in range(len(rec)):
        for j in range(len(rec[i])):
            if rec[i][j]==0:
                c+=1
    txt="A versenyen "+str(c)+" érvénytelen ugrás volt."
    print("\t"+txt)
f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5("5.feladat")
f6("6.feladat")
f7("7.feladat")