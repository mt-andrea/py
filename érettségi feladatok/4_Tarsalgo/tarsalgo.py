rec=[]
azok=[]
def f1():
    f=open("ajto.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(" ")
        else:
            sor=sor.split(" ")
        rec.append([int(sor[0]),int(sor[1]),(sor[2]),sor[3]])

def f2(label):
    print(label)
    print("Az első belépő: "+str(rec[0][2]))
    ki=[]
    for i in range(len(rec)):
        if rec[i][3]=='ki':
            ki.append(rec[i][2])
    print("Az utolsó kilépő: "+str(ki[-1]))

def f3():
    f=open("athaladas.txt","w")
    for i in range(len(rec)):
        if rec[i][2] not in azok:
            azok.append(rec[i][2])
    azok.sort()
    for i in range(len(azok)):
        c=0
        for j in range(len(rec)):
            if rec[j][2]==azok[i]:
                c+=1
        f.write(str(azok[i])+" "+str(c)+"\n")

def f4(label):
    print(label)
    bent=[]
    for i in range(len(rec)):
        if rec[i][3]=="be":
            bent.append(rec[i][2])
        else:
            bent.remove(rec[i][2])
    bent.sort()
    txt=""
    for i in range(len(bent)):
        txt+=(str(bent[i])+" ")
    print("A végén a társalgóban voltak: "+txt)

def f5(label):
    print(label)
    time=[]
    for i in range(len(rec)):
        if rec[i][0]<10:
            o="0"+str(rec[i][0])
        else:
            o=str(rec[i][0])
        if rec[i][1]<10:
            p = "0" + str(rec[i][1])
        else:
            p = str(rec[i][1])
        txt=o+":"+p
        time.append(txt)
    t=[]
    for i in range(len(time)):
        if time[i] not in t:
            t.append(time[i])
    fo=[]
    c = 0
    for i in range(len(t)):
        for j in range(len(rec)):
            if int(t[i][:2])==rec[j][0] and int(t[i][3:])==rec[j][1] and rec[j][3]=="be":
                c+=1
            elif int(t[i][:2])==rec[j][0] and int(t[i][3:])==rec[j][1] and rec[j][3]=="ki":
                c-=1
        fo.append([t[i],c])
    maxi=0
    for i in range(len(fo)):
        if fo[i][1]>fo[maxi][1]:
            maxi=i
    print("Például "+fo[maxi][0]+"-kor voltak a legtöbben a társalgóban.")

def f6(label):
    print(label)
    az=input("Adja meg a személy azonosítóját! ")
    return az

def f7(label):
    print(label)
    for i in range(len(rec)):
        if rec[i][2]==az and rec[i][3]=="be":
            if rec[i][0] < 10:
                o = "0" + str(rec[i][0])
            else:
                o = str(rec[i][0])
            if rec[i][1] < 10:
                p = "0" + str(rec[i][1])
            else:
                p = str(rec[i][1])
            txt = o + ":" + p+"-"
            print(txt,end="")
        if rec[i][2] == az and rec[i][3] == "ki":
            if rec[i][0] < 10:
                o = "0" + str(rec[i][0])
            else:
                o = str(rec[i][0])
            if rec[i][1] < 10:
                p = "0" + str(rec[i][1])
            else:
                p = str(rec[i][1])
            txt = o + ":" + p
            print(txt)
    print("\n")

def f8(label):
    print(label)
    ki=[]
    be=[]
    for i in range(len(rec)):
        if rec[i][3]=="be" and rec[i][2]==az:
            t=int(rec[i][0])*60+int(rec[i][1])
            be.append(t)
        elif rec[i][3]=="ki" and rec[i][2]==az:
            t=int(rec[i][0]) * 60 + int(rec[i][1])
            ki.append(t)
    c=0
    if len(be)!=len(ki):
        ki.append(900)
        for j in range(len(ki)):
            c += (ki[j] - be[j])
        txt="A(z) "+az+". személy összesen "+str(c)+" percet volt bent, a megfigyelés végén a társalgóban volt."
    else:
        for j in range(len(ki)):
            c += (ki[j] - be[j])
        txt = "A(z) " + az + ". személy összesen " + str(c) + " percet volt bent, a megfigyelés végén nem volt a társalgóban."
    print(txt)

f1()
f2("2.feladat")
f3()
f4("4.feladat")
f5("5.feladat")
az=f6("6.feladat")
f7("7.feladat")
f8("8.feladat")