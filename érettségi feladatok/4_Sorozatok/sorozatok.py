import sorozatok_class
rec=[]
def f1():
    f=open("lista.txt", "r", encoding="utf-8")
    data=[]
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        data.append(sor)
    for i in range(0,len(data),5):
        rec.append(sorozatok_class.Sorozatok(data[i],data[i+1],data[i+2],int(data[i+3]),int(data[i+4])))
    
def f2(label):
    print(label)
    c=0
    for i in range(len(rec)):
        if rec[i].datum!="NI":
            c+=1
    print("A listában "+str(c)+" db vetívési dátummal rendelkező epizód van.\n")

def f3(label):
    print(label)
    c=0
    for i in range(len(rec)):
        if rec[i].nezve==1:
            c+=1
    print("A listában lévő epizópok "+str(round((c/len(rec))*100,2))+"%-át látta.\n")

def f4(label):
    print(label)
    t=0
    for i in range(len(rec)):
        if rec[i].nezve==1:
            t+=rec[i].hossz
    print("Sorozatnézéssel "+str(t//1440)+" napot "+str((t%1440)//60)+" órát és "+str((t%1440)%60)+" percet töltött.\n")

def f5(label):
    print(label)
    date=input("Adjon meg egy dátumot! Dátum= ")
    date=int(date[:4]+date[5:7]+date[8:])
    for i in range(len(rec)):
        if rec[i].datum!="NI":
            date2=int(rec[i].datum[:4]+rec[i].datum[5:7]+rec[i].datum[8:])
            if date>=date2:
                if rec[i].nezve==0:
                    print(rec[i].epizod+"\t"+rec[i].cim)
    print("\n")

def Hetnapja(ev,ho,nap):
    napok=["v","h","k","sze","cs","p","szo"]
    honapok=[0,3,2,5,0,3,5,1,4,6,2,4]
    if ho<3:
        ev-=1
    hetnapja=napok[(ev+ev//4-ev//100+ev//400+honapok[ho-1]+nap)%7]
    return hetnapja

def f7(label):
    print(label)
    day=input("Adja meg a hét egy napját (például cs)! Nap= ")
    sorik=[]
    for i in range(len(rec)):
        if rec[i].datum!="NI":
            ev=int(rec[i].datum[:4])
            ho=int(rec[i].datum[5:7])
            nap=int(rec[i].datum[8:])
            if Hetnapja(ev,ho,nap)==day:
                if rec[i].cim not in sorik:
                    sorik.append(rec[i].cim)
    if sorik!=[]:
        for i in range(len(sorik)):
            print(sorik[i])
    else:
        print("Az adott napon nem kerül adásba sorozat.")

def sori(cim):
    c=0
    t=0
    for i in range(len(rec)):
        if cim==rec[i].cim:
            c+=1
            t+=rec[i].hossz
    txt=cim+" "+str(t)+" "+str(c)+"\n"
    return txt

def f8():
    sorik=[]
    for i in range(len(rec)):
        if rec[i].cim not in sorik:
            sorik.append(rec[i].cim)
    f=open("summa.txt","w")
    for i in range(len(sorik)):
        f.write(sori(sorik[i]))

f1()
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")
f5("5. feladat")
f7("7. feladat")
f8()