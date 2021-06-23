rec=[]

def f1():
    f=open("ip.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
        rec.append(sor)

def f2(label):
    print(label)
    print("Az állományban",len(rec),"darab adatsor van.")

def f3(label):
    print(label)
    print("A legalacsonyabb tárolt IP-cím:\n",min(rec))

def f4(label):
    print(label)
    doku=0
    glob=0
    helyi=0
    for i in range(len(rec)):
        if rec[i][:9]=="2001:0db8":
            doku+=1
        elif rec[i][:7]=="2001:0e":
            glob+=1
        elif rec[i][:2]=="fc" or rec[i][:2]=="fd":
            helyi+=1
    print("Dokumentációs cím:",doku,"darab")
    print("Globális egyedi cím:", glob, "darab")
    print("Helyi egyedi cím:", helyi, "darab")

def f5():
    f=open("sok.txt","w")
    for i in range(len(rec)):
        c=0
        for j in range(len(rec[i])):
            if rec[i][j]=="0":
                c+=1
        if c>=18:
            f.write(str(i+1)+" "+rec[i]+"\n")

def f6(label):
    print(label)
    sorsz=int(input("Kérek egy sorszámot: "))
    print(rec[sorsz-1])
    cim=rec[sorsz-1].split(":")
    cim2=cim[0]
    for i in range(1,len(cim)):
        if cim[i]=="0000":
            cim2+=":0"
        else:
            cim2+=":"
            boo=True
            for j in range(len(cim[i])):
                if cim[i][j]=="0" and boo:
                    pass
                else:
                    boo=False
                    cim2+=cim[i][j]
    print(cim2)
    return cim2

def f7(label,cim):
    print(label)
    ind=0
    hossz=0
    max_h=0
    max_i=0
    cim=cim.split(":")
    for i in range(len(cim)):
        if cim[i]=="0" and hossz==0:
            hossz+=1
            ind=i
        elif cim[i]=="0":
            hossz+=1
        else:
            if hossz>max_h:
                max_h=hossz
                max_i=ind
                hossz=0
            else:
                hossz=0
    if hossz > max_h:
        max_h = hossz
        max_i = ind
        hossz = 0
    if max_h==0:
        print("Nem rövidíthető tovább.")
    else:
        cim2=cim[0]
        for i in range(1,len(cim)):
            if i<max_i:
                cim2+=":"+cim[i]
            elif i==max_i:
                cim2+=":"
            elif i>=max_i+max_h:
                cim2+=":"+cim[i]
        print(cim2)

f1()
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5()
cim3=f6("6.feladat")
f7("7. feladat",cim3)