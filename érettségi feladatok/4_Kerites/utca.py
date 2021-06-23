import utca_class

rec=[]
paros=[]
paratlan=[]

def f1():
    f=open("kerites.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(" ")
        else:
            sor=sor.split(" ")
        rec.append(utca_class.Telek(int(sor[0]),int(sor[1]),sor[2]))

def f2(label):
    print(label)
    print("Az eladott telkek száma: "+str(len(rec)))

def f3(label):
    print(label)
    
    if rec[-1].oldal==0:
        txt="páros"
    else:
        txt="páratlan"
    for _ in range(len(rec)):
        if rec[_].oldal==0:
            paros.append(rec[_])
        else:
            paratlan.append(rec[_])
    if rec[-1] in paros:
        j=0
        while paros[j]!=rec[-1]:
            j+=1
        szam=(j+1)*2
    elif rec[-1] in paratlan:
        j=0
        while paratlan[j]!=rec[-1]:
            j+=1
        szam=(j+1)*2-1
    print("A "+txt+" oldalon adták el az utolsó telket.")
    print("Az utolsó telek házszáma: "+str(szam))

def f4(label):
    print(label)
    for j in range(len(paratlan)-1):
        if paratlan[j].kerites!=":" and paratlan[j].kerites!="#":
            if paratlan[j].kerites==paratlan[j+1].kerites:
                print("A szomszédossal megegyezik a kerítés színe: "+str((j+1)*2-1))

def f5(label):
    print(label)
    szinek=[]
    for i in range(len(rec)):
        if rec[i].kerites not in szinek and rec[i].kerites!="#" and rec[i].kerites!=":":
            szinek.append(rec[i].kerites)
    szam=int(input("Adjon meg egy házszámot! "))
    if szam%2==1:
        i=int((szam+1)/2-1)
        szin=paratlan[i].kerites
        for _ in range(len(szinek)):
            if szinek[_]!=paratlan[i].kerites and szinek[_]!=paratlan[i+1].kerites and szinek[_]!=paratlan[i-1].kerites:
                lehet=szinek[_]
    else:
        i=int(szam/2-1)
        szin=paros[i].kerites
        for _ in range(len(szinek)):
            if szinek[_]!=paros[i].kerites and szinek[_]!=paros[i+1].kerites and szinek[_]!=paros[i-1].kerites:
                lehet=szinek[_]
    print("A kerítés színe / állapota: "+szin)
    print("Egy lehetséges festési szín: "+lehet)

def f6():
    f=open("utcakep.txt","w")
    for i in range(len(paratlan)):
        f.write(paratlan[i].szeles*paratlan[i].kerites)
    f.write("\n")
    for _ in range(len(paratlan)):
        szam=(_+1)*2-1
        if szam<10:
            f.write(str(szam)+(paratlan[_].szeles-1)*" ")
        elif szam>10 and szam<=99:
            f.write(str(szam)+(paratlan[_].szeles-2)*" ")
        else:
            f.write(str(szam)+(paratlan[_].szeles-3)*" ")


f1()
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
#f5("5.feladat")
f6()