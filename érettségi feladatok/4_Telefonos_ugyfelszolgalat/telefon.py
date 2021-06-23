rec=[]
def mpbe(o,p,mp):
    o*=3600
    p*=60
    mp=o+p+mp
    return mp

def f2():
    f=open("hivas.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(" ")
        else:
            sor=sor.split(" ")
        rec.append([[int(sor[0]),int(sor[1]),int(sor[2])],[int(sor[3]),int(sor[4]),int(sor[5])]])
    f.close()

def f3(label):
    print(label)
    o=rec[0][0][0]
    c=0
    i=0
    while i!=len(rec)-1:
        while i!=len(rec)-1 and o==rec[i][0][0]:
            c+=1
            i+=1
        print(o,"óra",c,"hívás")
        o=rec[i][0][0]
        c=0

def f4(label):
    print(label)
    hossz=[]
    for i in range(len(rec)):
        h=mpbe(rec[i][1][0],rec[i][1][1],rec[i][1][2])-mpbe(rec[i][0][0],rec[i][0][1],rec[i][0][2])
        hossz.append(h)
    maxi=hossz.index(max(hossz))
    print("leghosszabb hívás sorszáma:",maxi+1,"\nhossza:",max(hossz))

def f5(label):
    print(label)
    idopont=input("időpont (h min sec): ").split(" ")
    idopont=mpbe(int(idopont[0]),int(idopont[1]),int(idopont[2]))
    sorsz=0
    besz_k=mpbe(rec[sorsz][0][0],rec[sorsz][0][1],rec[sorsz][0][2])
    besz_v=mpbe(rec[sorsz][1][0],rec[sorsz][1][1],rec[sorsz][1][2])
    besz=True
    for i in range(len(rec)):
        kezd=mpbe(rec[i][0][0],rec[i][0][1],rec[i][0][2])
        veg=mpbe(rec[i][1][0],rec[i][1][1],rec[i][1][2])
        if kezd<idopont<veg:
            sorsz=i
            besz = True
            break
        else:
            besz=False
    if besz:
        c=0
        for j in range(len(rec)):
            kezd = mpbe(rec[j][0][0], rec[j][0][1], rec[j][0][2])
            if besz_k<kezd<besz_v:
                c+=1
        print("vár:",c,"\nbeszél: "+str(sorsz+1)+". hívó")
    else:
        print("Nemvolt beszélő.")

def f6(label):
    print(label)
    siker=[]
    munk_v=mpbe(12,0,0)
    munk_k=mpbe(8,0,0)
    sorsz=0
    s=0
    for i in range(len(rec)):
        veg_e = mpbe(rec[s][1][0], rec[s][1][1], rec[s][1][2])
        kezd = mpbe(rec[i][0][0], rec[i][0][1], rec[i][0][2])
        veg = mpbe(rec[i][1][0], rec[i][1][1], rec[i][1][2])
        if veg>munk_k and veg>veg_e and kezd<munk_v:
            s=i
            siker.append(rec[i])
    while siker[-1]!=rec[sorsz]:
        sorsz+=1
    vart=mpbe(siker[-2][1][0], siker[-2][1][1], siker[-2][1][2])-mpbe(rec[sorsz][0][0], rec[sorsz][0][1], rec[sorsz][0][2])
    print("Az utolsó telefonáló: "+str(sorsz+1)+". hívó \nVárt:",vart,"másodpercet")
    return siker

def f7(lista):
    f=open("sikeres.txt","w")
    for i in range(len(lista)):
        for j in range(len(rec)):
            if lista[i]==rec[j] and i==0:
                txt = str(j + 1) + " 8 0 0 "  + str(lista[i][1][0]) + " " + str(lista[i][1][1]) + " " + str(lista[i][1][2])
                f.write(txt + "\n")
            elif lista[i]==rec[j]:
                txt=str(j+1)+" "+str(lista[i-1][1][0])+" "+str(lista[i-1][1][1])+" "+str(lista[i-1][1][2])+" "+str(lista[i][1][0])+" "+str(lista[i][1][1])+" "+str(lista[i][1][2])
                f.write(txt+"\n")
    f.close()

f2()
f3("3.feladat")
f4("4.feladat")
#f5("5.feladat")
sikeres=f6("6.feladat")
f7(sikeres)