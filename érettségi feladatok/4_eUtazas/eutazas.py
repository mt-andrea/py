
rec=[]
def inp_file (file,lista):
    f=open(file,"r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor = sor[:-1].split(" ")
        else:
            sor = sor.split(" ")
        lista.append([int(sor[0]),int(sor[1][:-5]),int(sor[2]),str(sor[3]),int(sor[4])])
    f.close()
def f1(label):
    print(label)
    inp_file("utasadat.txt",rec)
    txt="Az adatok beolvasása... Kész!"
    print("\t"+txt)
def f2(label):
    print(label)
    txt="A buszra "+str(len(rec))+" utas akart felszállni."
    print("\t"+txt)
def f3(label):
    print(label)
    c=0
    for i in range(len(rec)):
        if rec[i][1]>rec[i][4] and rec[i][3]!="JGY":
            c+=1
        elif rec[i][4]==0 and rec[i][3]=="JGY":
            c+=1
    txt="A buszra "+str(c)+" utas nem szállhatott fel."
    print("\t"+txt)
def f4(label):
    print(label)
    maxforg=0
    maxmegallo=0
    utasforg={}
    for i in range(len(rec)):
        if rec[i][0] not in utasforg.keys():
            utasforg.update({rec[i][0]:1})
        else:
            utasforg[rec[i][0]]+=1
    for k in utasforg.keys():
        if utasforg[k]>maxforg:
            maxforg=utasforg[k]
            maxmegallo=k
    txt="A legtöbb utas ("+str(maxforg)+" fő) a "+str(maxmegallo)+". megállóban próbált felszállni."
    print("\t"+txt)
def f5(label):
    print(label)
    discount=0
    free=0
    discounts=["TAB","NYB"]
    frees=["GYK","NYP","RVS"]
    for i in range(len(rec)):
        if rec[i][1]<=rec[i][4]:
            if rec[i][3] in discounts:
                discount+=1
            elif rec[i][3] in frees:
                free+=1
    txt="Ingyenesen utazók száma: "+str(free)+" fő\n\tA kedvezményesen utazók száma: "+str(discount)+" fő"
    print("\t"+txt)
def napokszama(e1,h1,n1,e2,h2,n2):
	h1=(h1+9)%12
	e1=e1-h1//10
	d1= 365*e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1*306 + 5) // 10 + n1 - 1
	h2 = (h2 + 9) % 12
	e2 = e2 - h2 // 10
	d2= 365*e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2*306 + 5) // 10 + n2 - 1
	return d2-d1
def f7(label):
    f=open("figyelmeztetes.txt","w+")
    for i in range(len(rec)):
        if rec[i][3]!="JGY":
            e1=int(str(rec[i][1])[:4])
            h1=int(str(rec[i][1])[4:6])
            n1=int(str(rec[i][1])[6:])
            e2=int(str(rec[i][4])[:4])
            h2=int(str(rec[i][4])[4:6])
            n2=int(str(rec[i][4])[6:])
            if napokszama(e1,h1,n1,e2,h2,n2)<=3:
                if h2<10:
                    h2="0"+str(h2)
                if n2<10:
                    n2="0"+str(n2)
                f.write(str(rec[i][2])+" "+ str(e2)+"-"+str(h2)+"-"+str(n2)+"\n")
f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5("5.feladat")
#f6("6.feladat")
f7("7.feladat")