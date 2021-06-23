rec=[]
def f1():
    f=open("penztar.txt","r",encoding="utf-8")
    #{doboz:1}
    #{colostok:2,kefe:1,..}
    #"colostok" in rec[i].keys()

    vas={}
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        if sor=="F":
            rec.append(vas)
            vas={}
        else:
            if sor in vas.keys():
                vas[sor]+=1
            else:
                vas[sor]=1
    #print(rec)

    # darab = 0
    # for i in range(len(rec)):
    #   if "doboz" in rec[i].keys:
    #       darab+=1

def f2(label):
    print(label)
    print(str(len(rec))+"-szer fizettek a pénztárnál.")

def f3(label):
    print(label)

    print("Az első vásárlónak",sum(rec[0].values()),"db árúcikk volt a kosarában.")

def f4(label):
    print(label)
    sorsz=int(input("Vásárlás szorszáma: "))
    aru=input("Árucikk neve: ")
    db=int(input("Darabszám: "))
    return sorsz , aru , db

def f5(label):
    print(label)
    elso=0
    utolso=0
    elof=0
    eloszor=True
    for i in range(len(rec)):
        if aru in rec[i].keys():
            if eloszor:
                elso=i+1
                utolso=i+1
                eloszor=False
            else:
                utolso=i+1
            elof+=1
    print(str(elso)+". vásárláskor vettek először, és\n"+str(utolso)+". utoljára\nösszesen",elof,"alkalommal.")

def ertek(darab):
    if darab==1:
        return 500
    elif darab==2:
        return 500+450
    else:
        return 950+(darab-2)*400

def f6(label):
    print(label)
    print(str(db)+" darab: "+str(ertek(db))+" Ft")

def f7(label):
    print(label)
    for kulcs in rec[sorsz-1].keys():
        print(rec[sorsz-1][kulcs],kulcs)

def f8():
    f=open("osszeg.txt","w")
    for i in range(len(rec)):
        ossz=0
        for kulcs in rec[i].keys():
            ossz+=ertek(rec[i][kulcs])
        f.write(str(i+1)+": "+str(ossz)+"\n")

f1()
f2("2.feladat")
f3("3.feladat")
#sorsz , aru , db = f4("4.feladat")
#f5("5.feladat")
#f6("6.feladat")
#f7("7.feladat")
f8()