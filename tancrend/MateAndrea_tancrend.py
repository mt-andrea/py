rec=[]
def f1(label):
    print(label)
    f=open("tancrend.txt","r")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(";")
        else:
            sor=sor.split(";")
        rec.append([sor[0],sor[1],sor[2]])
    txt="A fájl beolvasása...kész!"
    print("\t"+txt)
    txt=rec[0][0]
    print("\t"+txt)
    txt=rec[-1][0]
    print("\t"+txt)
def f2(label):
    print(label)
    c=0
    for i in range(len(rec)):
        if rec[i][0]=="samba":
            c+=1
            txt=rec[i][1]+", "+rec[i][2]
            print("\t"+txt)
    txt=str(c)+" pár mutatta be a sambát."
    print("\t"+txt)
def f3(label):
    print(label)
    for i in range(len(rec)):
        if rec[i][1]=="Vilma":
            txt=rec[i][0]
            print("\t"+txt)
def f4(label):
    print(label)
    txt="Kérek egy táncot (cha-cha, salsa, rumba, samba, jive, tango, bachata): "
    tanc=input(txt)
    par=[]
    for i in range(len(rec)):
        if rec[i][0]==tanc and rec[i][1]=="Vilma":
            par.append(rec[i][2])
            txt="A "+tanc+" bemutatóján Vilma párja "+par[0]+" volt."
        elif par==[]:
            txt="Vilma nem táncolt "+tanc+"-t."
    print("\t"+txt)
def f5(label):
    print(label)
    girls=[]
    boys=[]
    nevek=[]
    f=open("szereplok.txt","w")
    for i in range(len(rec)):
        nevek.append(rec[i][1])
        girls=sorted(set(nevek))
    txt="Lányok: "
    for _ in range(len(girls)):
        txt=txt+girls[_]+", "
    print("\t"+txt[:-2])
    f.write(txt[:-2]+"\n")
    nevek=[]
    for i in range(len(rec)):
        nevek.append(rec[i][2])
        boys=sorted(set(nevek))
    txt="Fiúk: "
    for _ in range(len(boys)):
        txt=txt+boys[_]+", "
    print("\t"+txt[:-2])
    f.write(txt[:-2])
    txt="A szereplok.txt fájl kiírása...kész!"
    print("\t"+txt)
f1("1. feladat")
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")
f5("5. feladat")