vetel=[]
uzenet=[]
napok=[]
def f1():
    f=open("veetel.txt","r", encoding="utf-8")
    paratlan=True
    for sor in f:
        if paratlan:
            if sor[-1] == "\n":
                sor = sor[:-1].split(" ")
            else:
                sor = sor.split(" ")
            vetel.append([sor[0], sor[1]])
            paratlan=False
        else:
            if sor[-1] == "\n":
                sor = sor[:-1]
            uzenet.append(sor)
            paratlan=True

def f2(label):
    print(label)
    print("Az első üzenet rőgzítője: "+vetel[0][1])
    print("Az utolsó üzenet rögzítője: "+vetel[-1][1])

def f3(label):
    print(label)
    for i in range(len(uzenet)):
        if "farkas" in uzenet[i]:
            print(vetel[i][0]+". nap "+vetel[i][1]+". rádióamatőr")

def f4(label):
    print(label)

    for i in range(len(vetel)):
        if int(vetel[i][0]) not in napok:
            napok.append(int(vetel[i][0]))
    napok.sort()
    for j in range(len(napok)):
        c = 0
        for k in range(len(vetel)):
            if napok[j]==int(vetel[k][0]):
                c+=1
        print(str(napok[j])+". nap: "+str(c)+" rádióamatőr")

def f5():
    f=open("adaas.txt","w")
    for i in range(len(napok)):
        uz =""
        for j in range(len(vetel)):
            if str(napok[i])==vetel[j][0]:
                if uz=="":
                    uz=uzenet[j]
                else:
                    for k in range(len(uz)):
                        if uz[k]=="#":
                            uz=uz[:k]+uzenet[j][k]+uz[k+1:]
        f.write(uz+"\n")

def szame(szo):
    valasz=True
    for i in range(len(szo)):
        if szo[i]<'0' or szo[i]>'9':
            valasz=False
    return valasz

def f7(label):
    print(label)
    nap=input("Adja meg a nap sor számát! ")
    ama=input("Adja meg egy rádióamatőr sorszám! ")
    let=False
    for i in range(len(vetel)):
        if vetel[i][0]==nap and vetel[i][1]==ama:
            szo=uzenet[i].split(" ")[0]
            let=True
            if "/" in szo:
                szo=szo.split("/")
                if szame(szo[0]) and szame(szo[1]):
                    print("A megfigyelt egyedek száma: "+str(int(szo[0])+int(szo[1])))
                else:
                    print("Nincs információ")
            else:
                print("Nincs információ")
    if not let:
        print("Nincs ilyen feljegyzés")

f1()
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")
f5()
f7("7. feladat")