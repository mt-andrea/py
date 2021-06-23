#Máté Andrea
rec=[]
def inpFile(file,lista):
    f=open(file,"r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor = sor[:-1].split(";")
        else:
            sor = sor.split(";")
        lista.append([str(sor[0]),int(sor[1]),int(sor[2]),int(sor[3])])
    f.close()
def sum_mp(i):
    s=0
    for j in range(1,len(rec[i])):
        s+=rec[i][j]
    return s
def avg(j):
    s=0
    for i in range(len(rec)):
        s+=rec[i][j]
    a=round(s/len(rec),1)
    return a
def printRec(i):
    txt=rec[i][0]+":\t"+str(sum_mp(i))+" mp"
    print("\t"+txt)
def exchange(i,j,km):
    km_h=round((((km*1000)/rec[i][j])*3.6),1)
    return km_h
def convert(i):
    h=sum_mp(i)//3600
    mm=(sum_mp(i)%3600)//60
    ss=(sum_mp(i)%3600)%60
    if h<10:
        h="0"+str(h)
    time=str(h)+":"+str(mm)+":"+str(ss)
    return time
def printTime(name):
    i=0
    while rec[i][0]!=name:
        i+=1
    txt=rec[i][0]+" "+convert(i)
    print("\t"+txt)
def e1(label):
    print(label)
    inpFile("triatlon.txt",rec)
    print("Reading records...Done.")
def e2(label):
    print(label)
    txt="A versenyen "+str(len(rec))+" fő vett részt."
    print("\t"+txt)
def e3(label):
    print(label)
    print("\tNév \t\tVersenyidő")
    for i in range(len(rec)):
        printRec(i)
def e4(label):
    print(label)
    print("Alapos vállveregetés jár nekik:")
    for i in range(len(rec)):
        if sum_mp(i)<9270:
            printRec(i)
def e5(label):
    print(label)
    print("Szemte Lenke őket előzte meg:")
    i=0
    while rec[i][0]!="Szemte Lenke":
        i+=1
    lenke_t=sum_mp(i)
    for i in range(len(rec)):
        if sum_mp(i)>lenke_t:
            printRec(i)
def e6(label):
    print(label)
    minInd=0
    for i in range(len(rec)):
        if sum_mp(i)<sum_mp(minInd):
            minInd=i
    printRec(minInd)
def e7(label):
    print(label)
    txt="A futások átlag ideje: "+str(avg(3))+" pm"
    print("\t"+txt)
def e8(label):
    print(label)
    minInd=0
    for i in range(len(rec)):
        if rec[i][2] <rec[minInd][2]:
            minInd=i
    txt="A leggyorsabb kerékpáros átlag sebessége 40 km-en:"+str(exchange(minInd,2,40))
    print("\t"+txt)
def e9(label):
    print(label)
    printTime("Bármi Áron")
    printTime("Pum Pál")
e1("1. feladat")
e2("2. feladat")
e3("3. feladat")
e4("4. feladat")
e5("5. feladat")
e6("6. feladat")
e7("7. feladat")
e8("8. feladat")
e9("9. feladat")