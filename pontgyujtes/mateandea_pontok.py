rec=[]
def f1(label):
    print(label)
    f=open("pontok.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(";")
        else:
            sor=sor.split(";")
        rec.append([sor[0],int(sor[1]),int(sor[2])])
    txt="A fájl beolvasása...kész!"
    print("\t"+txt)
    names=[]
    for i in range(len(rec)):
        if rec[i][0] not in names:
            names.append(rec[i][0])
    txt="A versenyben résztvettek: "
    print("\t"+txt)
    for _ in range(len(names)):
        txt=names[_]
        print("\t"+txt)
def f2(label):
    print(label)
    f=open("CsorbaEde.txt","w")
    for i in range(len(rec)):
        if rec[i][0]=="Csorba Ede":
            txt=str(rec[i][1])+": "+str(rec[i][2])
            f.write(txt+"\n")
    txt="A CsorbaEde.txt fájl kiírása...kész!"
    print("\t"+txt)
    count=0
    for i in range(len(rec)):
        if rec[i][0]=="Csorba Ede":
            count+=rec[i][2]
    txt="Csorba Ede "+str(count)+" pontot gyűjtött."
    print("\t"+txt)
def f3(label):
    print(label)
    names=[]
    for i in range(len(rec)):
        if rec[i][1]==2016 and rec[i][2]==14:
            if rec[i][0] not in names:
                names.append(rec[i][0])
    names.sort()
    for _ in range(len(names)):
        txt=names[_]
        print("\t"+txt)
def f4(label):
    print(label)
    year=int(input("Válasszon egy évszámot(2014, 2015, 2016): "))
    names=[]
    for i in range(len(rec)):
        if rec[i][0] not in names:
            names.append(rec[i][0])
    for j in range(len(names)):
        count=0
        for _ in range(len(rec)):
            if year==rec[_][1] and names[j]==rec[_][0]:
                count+=rec[_][2]
        txt=names[j]+": "+str(count)+" pont"
        print("\t"+txt)
def f5(label):
    print(label)
    names=[]
    for i in range(len(rec)):
        if rec[i][0] not in names:
            names.append(rec[i][0])
    for j in range(len(names)):
        count=0
        for _ in range(len(rec)):
            if names[j]==rec[_][0]:
                count+=rec[_][2]
        txt=names[j]+": "+str((count/2)*3000)+" Ft"
        print("\t"+txt)
f1("1. feladat")
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")
f5("5. feladat")