fog=[]
kat=[]
def f1():
    f=open("foglaltsag.txt","r",encoding="utf-8")
    f2=open("kategoria.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        fog.append(sor)
    for sor in f2:
        if sor[-1]=="\n":
            sor=sor[:-1]
        kat.append(sor)

def f2(label):
    print(label)
    sor=int(input("adja meg egy sor számát: "))
    szek=int(input("adja meg egy szék számát: "))
    if fog[sor-1][szek-1]=="x":
        print("a szék már foglalt")
    else:
        print("a szék szabad")

def f3(label):
    print(label)
    oss=0
    c=0
    for i in range(len(fog)):
       for j in range(len(fog[i])):
           if fog[i][j]=="x":
               c+=1
           oss+=1
    print("Az előadásra",c,"jegyet adtak el, ez a nézőtér",str(round(c/oss*100,0))+"%-a.")

def f4(label):
    print(label)
    kate=[0,0,0,0,0]
    for i in range(len(fog)):
        for j in range(len(fog[i])):
            if fog[i][j]=="x":
                kate[int(kat[i][j])-1]+=1
    print("A legtöbb jegyet a(z) "+str(kate.index(max(kate))+1)+". kategóriában értékesítették.")
    return kate

def f5(label,lista):
    print(label)
    bev=lista[0]*5000+lista[1]*4000+lista[2]*3000+lista[3]*2000+lista[4]*1500
    print(bev,"Ft bevétele lenne.")

def f6(label):
    print(label)
    c=0
    for i in range(len(fog)):
        for j in range(1,len(fog[i])-1):
            if fog[i][j]=="o":
                if fog[i][j-1]=="x" and fog[i][j+1]=="x":
                    c+=1
        if (fog[i][0]=="o" and fog[i][1]=="x") or (fog[i][-1]=="o" and fog[i][-2]=="x"):
            c+=1
    print(c,"egyedülálló hely van")

def f7():
    f=open("szabad.txt","w")
    for i in range(len(fog)):
        txt=""
        for j in range(len(fog[i])):
            if fog[i][j]=="x":
                txt+=fog[i][j]
            else:
                txt+=kat[i][j]
        f.write(txt+"\n")
f1()
#f2("2.feladat")
f3("3.feladat")
kateg=f4("4.feladat")
f5("5.feladat",kateg)
f6("6.feladat")
f7()