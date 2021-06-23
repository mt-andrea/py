rec=[]
def f1(label):
    print(label)
    f=open("palyak.txt", "r", encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(";")
        else:
            sor=sor.split(";")
        rec.append([sor[0],int(sor[1]),int(sor[2]),sor[3]])
    txt="A fájl beolvasása...kész!"
    print("\t"+txt)
    for i in range(len(rec)-5,len(rec)):
        txt=rec[i][0]
        print("\t"+txt)
def f2(label):
    print(label)
    f=open("betonos.txt","w",encoding="utf-8")
    c=0
    for i in range(len(rec)):
        if rec[i][3]=="beton":
            txt=rec[i][0]+"\t"+str(rec[i][1])+"\t"+str(rec[i][2])+"\n"
            f.write(txt)
            c+=1
    txt="A betonos.txt fájl kiírása...kész!"
    print("\t"+txt)
    txt="rekordszám: "+str(c)
    print("\t"+txt)
def f3(label):
    print(label)
    txt="Kérek egy 17 és 501 közé eső egész számot: "
    width=int(input(txt))
    f=open("betonos.txt","r",encoding="utf-8")
    bet=[]
    for sor in f:
        sor=sor[:-1].split("\t")
        bet.append([sor[0],int(sor[1]),int(sor[2])])
    c=0
    for i in range(len(bet)):
        if bet[i][2]>width:
            txt=bet[i][0]+"\t"+str(bet[i][1])+"\t"+str(bet[i][2])
            print("\t"+txt)
            c+=1
    if c==0:
        txt="Nincs ilyen leszállóhely."
        print("\t"+txt)
def f4(label):
    print(label)
    i=0
    while rec[i][0]!="Mezõkövesd":
        i+=1
    for _ in range(len(rec)):
        if rec[_][1]>=rec[i][1]*4:
            txt=rec[_][0]+": "+str(rec[_][1])+" m"
            print("\t"+txt)
def f5(label):
    print(label)
    maxInd=0
    for i in range(len(rec)):
            if rec[i][1]*rec[i][2]>rec[maxInd][1]*rec[maxInd][2] and rec[i][3]=="fû":
                maxInd=i
    txt=rec[maxInd][0]+" "+str(rec[maxInd][1]*rec[maxInd][2])+" m2 "+str(int(((rec[maxInd][1]*rec[maxInd][2])/10)*2))+" Ft"
    print("\t"+txt)
f1("1. feladat")
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")
f5("5. feladat")