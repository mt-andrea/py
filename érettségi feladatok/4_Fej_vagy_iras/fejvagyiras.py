import random
def dob():
    dobas = random.randint(0, 1)
    if dobas == 0:
        eredmeny = "F"
    else:
        eredmeny = "I"
    return eredmeny

def f1(label):
    print(label)
    print("A pénzfeldobás eredménye:",dob())

def f2(label):
    print(label)
    tip=input("Tippeljen! (F/I)= ")
    dobas=dob()
    print("A tipp",tip+", a dobás eredménye",dobas,"volt.")
    if tip==dobas:
        txt="Ön eltalálta."
    else:txt="Ön nem találta el."
    print(txt)

def f3(label):
    print(label)
    f=open("kiserlet.txt","r")
    c=0
    for sor in f:
        if sor!="\n":
            c+=1
    print("A kísérlet",c,"dobásból állt.")
    f.close()
    return c

def f4(label,c):
    print(label)
    f = open("kiserlet.txt", "r")
    fej=0
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        if sor=="F":
            fej+=1
    print("A kísérlet során a fej relatív gyakorisága "+str(round((fej/c)*100,2))+"% volt.")
    f.close()

def f5(label):
    print(label)
    f = open("kiserlet.txt", "r")
    szamlalo=0
    c=0
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        if sor=="F":
            c+=1
        elif sor=="I" and c==2:
            szamlalo+=1
            c=0
        elif sor=="I":
            c=0
    print("A kísérlet során",szamlalo,"alkalommal dobtak pontosan két fejet egymás után.")
    f.close()

def f6(label):
    print(label)
    f = open("kiserlet.txt", "r")
    leg_db=0
    leg_elso=0
    elso=0
    db=0
    aktualis=0
    for sor in f:
        aktualis+=1
        if sor[-1]=="\n":
            sor=sor[:-1]
        if sor=="F":
            db+=1
            if db==1:
                elso=aktualis
        elif sor=="I":
            if db>leg_db:
                leg_db=db
                leg_elso=elso
            db=0
    if db>leg_db:
        leg_db=db
        leg_elso=elso
    print("A leghosszabb tisztafej sorozat",leg_db,"tagból áll, kezdete a(z)",str(leg_elso)+". dobáas.")

def f7():
    rec=[]
    f=open("dobasok.txt","w")
    for i in range(1000):
        txt=""
        for j in range(4):
            txt+=dob()
        rec.append(txt)
    c_FFFF=0
    c_FFFI=0
    for i in range(len(rec)):
        if "FFFF" in rec[i]:
            c_FFFF+=1
        elif "FFFI" in rec[i]:
            c_FFFI+=1
    f.write("FFFF: "+str(c_FFFF)+", FFFI: "+str(c_FFFI)+"\n")
    for i in range(len(rec)):
        f.write(rec[i]+" ")


f1("1.feradat")
#f2("2.feradat")
szam=f3("3.feladat")
f4("4.feladat",szam)
f5("5.feradat")
f6("6.feradat")
f7()