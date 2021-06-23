rec=[]

def f1():
    f=open("verseny.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        rec.append(sor)

def f2(label):
    print(label)
    txt="Az egymást követően többször találó versenyzők: "
    for i in range(len(rec)):
        for j in range(len(rec[i])-1):
            if rec[i][j]+rec[i][j+1]=="++":
                txt+=str(i)+" "
                break
    print(txt)

def f3(label):
    print(label)
    txt="A legtöbb lövést leadó versenyző trajtszáma: "
    maxi=0
    for i in range(len(rec)):
        if len(rec[i])>len(rec[maxi]):
            maxi=i
    print(txt,maxi)

def loertek(sor):
    aktpont=20
    ertek=0
    for i in range(len(sor)):
        if aktpont>0 and sor[i]=="-":
            aktpont-=1
        else:
            ertek+=aktpont
    return ertek

def f5(label):
    print(label)
    rajtsz=int(input("Adjon meg egy rajtszámot! "))
    txt=""
    c=0
    max_h=0
    h=0
    for i in range(len(rec[rajtsz])):
        if rec[rajtsz][i]=="+":
            txt+=str(i+1)+" "
            c+=1
            h+=1
        else:
            if h>max_h:
                max_h=h
                h=0
            else:
                h=0
    print("5a. feladat: Céltérő lövések: "+txt)
    print("5b. feladat: Az eltalált korongok száma:",c)
    print("5c. feladat: A leghosszabb hibátlan sorozat hossza:",max_h)
    print("5d. feladat: A versenyző pontszáma:",loertek(rec[rajtsz]))

def f6():
    f=open("sorrend.txt","w")
    pontok=[]
    for i in range(1,len(rec)):
        pontok.append([i,loertek(rec[i])])
    pontok.sort(key=lambda x:x[1],reverse=True)
    print(pontok)
    f.write("1\t"+str(pontok[0][0])+"\t"+str(pontok[0][1])+"\n")
    helyezes=1
    for i in range(1,len(pontok)):
        if pontok[i][1]==pontok[i-1][1]:
            f.write(str(helyezes)+"\t"+str(pontok[i][0])+"\t"+str(pontok[i][1])+"\n")
        else:
            helyezes=i+1
            f.write(str(helyezes)+"\t"+str(pontok[i][0])+"\t"+str(pontok[i][1])+"\n")
f1()
f2("2.feladat:")
f3("3.feladat:")
#f5("5.feladat:")
f6()
