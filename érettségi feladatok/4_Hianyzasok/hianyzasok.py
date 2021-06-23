rec=[]
naplo={}
def f1_2():
    f = open("naplo.txt", "r", encoding="utf-8")
    datum=""
    hianyzok={}
    for sor in f:
        if sor[-1] == "\n":
            sor = sor[:-1]
        if datum!="" and sor[0]=="#":
            naplo[datum]=hianyzok
            datum=sor[2:]
            hianyzok={}
        elif sor[0]=="#":
            datum=sor[2:]
        else:
            bej=sor.split(" ")
            nev=bej[0]+" "+bej[1]
            hianyzok[nev]=bej[2]
    naplo[datum] = hianyzok
    print(naplo)



def f1():
    f=open("naplo.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        rec.append(sor)

def f2(label):
    print(label)
    c=0
    for i in range(len(rec)):
        if rec[i][0]!="#":
            c+=1
    print("a naplóban "+str(c)+" bejegyzés van.")

def f3(label):
    print(label)
    x=0
    i=0
    for j in range(len(rec)):
        if rec[j][0]!="#":
            for k in range(-7,0):
                if rec[j][k]=="X":
                    x+=1
                elif rec[j][k]== "I":
                    i+=1
    print("Az igazolt hiányzások száma "+str(x)+", az igazolatlanoké "+str(i)+" óra.")

def hetnapja(h,n):
    nap=["vasárnap", "hétfő", "kedd", "szerda", "csütörtök","péntek", "szombat"]
    napsz=[0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    naps=(napsz[h-1]+n)%7
    return nap[naps]

def f5(label):
    print(label)
    h=int(input("hónap sorszáma = "))
    n=int(input("nap sorszáma = "))
    print("Azon a napon "+hetnapja(h,n)+" volt")

def f6(label):
    print(label)
    nap=input("nap neve: ")
    ora=int(input("óra sorsáma: "))
    c=0
    for i in range(len(rec)):
        if rec[i][0]=="#" and hetnapja(int(rec[i][2:4]),int(rec[i][5:7]))==nap:
            i+=1
            while rec[i][0]!="#":
                if rec[i][-8+ora]=="I" or rec[i][-8+ora]=="X":
                    c+=1
                i+=1
    print("Ekkor összesen "+str(c)+" óra hiányzás történt.")

def f7(label):
    print(label)
    nevek=[]
    hianyzasok=[]
    for i in range(len(rec)):
        if rec[i][0]!="#" and rec[i][:-8] not in nevek:
            nevek.append(rec[i][:-8])
    for j in range(len(nevek)):
        c=0
        for k in range(len(rec)):
            if rec[k][0] != "#" and rec[k][:-8]==nevek[j]:
                    for l in range(-7,0):
                        if rec[k][l] == "I" or rec[k][l] == "X":
                            c += 1
        hianyzasok.append(c)
    txt="A legtöbbet hiányzó tanulók: "
    for i in range(len(nevek)):
        if hianyzasok[i]==max(hianyzasok):
            txt+=nevek[i]+" "
    print(txt)


#f1()
#f2("2.feladat")
#f3("3.feladat")
#f5("5.feladat")
#f6("6.feladat")
#f7("7. feladat")

f1_2()