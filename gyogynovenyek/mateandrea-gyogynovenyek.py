#Máté Andrea
rec=[]
def inpFile(file,lista):
    f=open(file,"r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor = sor[:-1].split("\t")
        else:
            sor = sor.split("\t")
        lista.append([str(sor[0]),str(sor[1]),int(sor[2]),int(sor[3])])
    f.close()
def printRec(i):
    txt=rec[i][0]+"\t"+rec[i][1]+"\t"+str(rec[i][2])+"\t"+str(rec[i][3])
    print("\t"+txt)
def printName(name):
    i=0
    while rec[i][0]!=name:
        i+=1
    printRec(i)
def count_collectable(part):
    c=0
    for i in range(len(rec)):
        if rec[i][1]==part:
            c+=1
    txt=str(c)+" növénynek gyűjtjük ezt a részét: "+part
    print("\t"+txt)
def start_collect(month):
    months=["","január","február","március","április","május","június","július","augusztus","szeptember","október","november","december"]
    txt="Ezeknek a gyógynövényeknek kezdődik a gyűjtése ebben a hónapban: "+months[month]
    print("\t"+txt)
    for i in range(len(rec)):
        if rec[i][2]==month:
            printRec(i)
def first_last_plant(isFirst):
    if isFirst:
        minInd=0
        for i in range(len(rec)):
            if rec[i][2]<rec[minInd][2]:
                minInd=i
        txt="Az első gyógynövény gyűjtését egy adott év "+str(rec[minInd][2])+". hónapjában lehet kezdeni."
    else:
        maxInd=0
        for i in range(len(rec)):
            if rec[i][2]>rec[maxInd][2]:
                maxInd=i
        txt="Az utolsó gyógynövény gyűjtését egy adott év "+str(rec[maxInd][2])+". hónapjában lehet kezdeni."
    print("\t"+txt)
def time_collectable(i):
    if rec[i][3]<rec[i][2]:
        t=13-rec[i][2]+rec[i][3]
    else:
        t=rec[i][3]-rec[i][2]+1
    return str(t)
def from_till(name1,name2):
    i=0
    while rec[i][0]!=name1:
        i+=1
    while rec[i][0]!=name2:
        txt=rec[i][0]+": "+time_collectable(i)
        print("\t"+txt)
        i+=1
def f1(label):
    print(label)
    inpFile("adatok.txt",rec)
    txt="Az adatok beolvasása... Kész!"
    print("\t"+txt)
def f2(label):
    print(label)
    txt=str(len(rec))+" növény adatait tároljuk."
    print("\t"+txt)
def f3(label):
    print(label)
    printName("Csombormenta")
def f4(label):
    print(label)
    count_collectable("levél")
def f5(label):
    print(label)
    start_collect(8)
def f6(label):
    print(label)
    first_last_plant(True)
def f7(label):
    print(label)
    from_till("Csillagpázsit","Fekete áfonya")
f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5("5.feladat")
f6("6.feladat")
f7("7.feladat")