rec=[]
def f1():
    f=open("fogado.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(" ")
        else:
            sor=sor.split(" ")
        rec.append([sor[0],sor[1],sor[2],sor[3]])

def f2(label):
    print(label)
    print("Foglalások száma: "+str(len(rec)))

def f3(label):
    print(label)
    nev=input("Adjon meg egy nevet: ")
    c=0
    for i in range(len(rec)):
        if nev==rec[i][0]+" "+rec[i][1]:
            c+=1
    if c==0:
        print("A megadott néven nincs időpontfoglalás.")
    else:
        print(nev+" néven "+str(c)+" időpontfoglalás van.")

def f4(label):
    print(label)
    nevek=[]
    ido=input("Adjon meg egy érvényes időpontot (pl. 17:10):")
    txt=ido[:2]+ido[3:]
    f=open(txt,"w")
    for i in range(len(rec)):
        if rec[i][2]==ido:
            nev=rec[i][0]+" "+rec[i][1]
            nevek.append(nev)
    nevek.sort()
    for i in range(len(nevek)):
        print(nevek[i])
        f.write(nevek[i] + "\n")

def f5(label):
    nev=input("Tanár neve:")
    mini=0
    for i in range(len(rec)):
        if nev==rec[i][0]+" "+rec[i][1] and int(rec[i][2][:2])<int(rec[mini][2][:2]) and int(rec[i][2][3:])<int(rec[mini][2][3:]):
            mini=i
    print("Foglalt időpont: "+rec[mini][2])
    print("Foglalás ideje: "+rec[mini][3])

def f6(label):
    print(label)
    o="16"
    mins="00"
    fogl=[]
    for i in range(len(rec)):
        if rec[i][0]+" "+rec[i][1]=="Barna Eszter":
            fogl.append(rec[i][2])
    for j in range(12):
        if o+":"+mins not in fogl:
            print(o+":"+mins)
        if mins=="50":
            o="17"
            mins="00"
        else:
            mins=str(int(mins)+10)
    fogl.sort()
    print("Barna Eszter legkorábban távozhat: "+fogl[-1][:2]+":"+str(int(fogl[-1][3:])+10))

f1()
#f2("2.feladat")
#f3("3.feladat")
#f4("4.feladat")
#f5("5.feladat")
f6("6.feladat")