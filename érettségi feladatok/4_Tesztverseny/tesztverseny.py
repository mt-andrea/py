
rec=[]
def f1(label):
    print(label,": Az adatok beoldasása")
    f=open("valaszok.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1]
            if len(sor)==14:
                helyes=sor
            else:
                sor=sor.split(" ")
                rec.append(sor)
    return helyes

def f2(label):
    print(label,": A vetélkedőn ",len(rec)," versenyző indult.")

def f3(label):
    print(label, end=": ")
    az=input("A versenyző azonosítója= ")
    i=0
    while rec[i][0]!=az:
        i+=1
    print("A versenyző válaszai:",rec[i][1])
    return az

def f4(label,az):
    print(label+":")
    print(helyes)
    i = 0
    while rec[i][0] != az:
        i += 1
    valasz=rec[i][1]

    for j in range(len(helyes)):
        if helyes[j]==valasz[j]:
            print("+",end="")
        else:
            print(" ",end="")
    print()

def f5(label):
    print(label, end=":")
    sorsz=int(input("A feladat sorszáma = "))
    fo=0
    for i in range(len(rec)):
        if rec[i][1][sorsz-1]==helyes[sorsz-1]:
            fo+=1
    szazalek=round((fo/(len(rec)))*100,2)
    print("A feladatra",fo,"fő, a versenyzők",szazalek,"%-a adott helyes választ.")

def f6():
    pontok=[3,4,5,6]
    eredmenyek=[]
    f=open("pontok.txt","w+")
    for i in range(len(rec)):
        p=0
        for j in range(len(helyes)):
            if rec[i][1][j]==helyes[j]:
                if 0<=j<=4:
                    p+=pontok[0]
                elif 5<=j<=9:
                    p+=pontok[1]
                elif 10<=j<=12:
                    p+=pontok[2]
                else:
                    p+=pontok[3]
        eredmenyek.append([rec[i][0],p])
        f.write(rec[i][0]+" "+str(p))
    f.close()
    return eredmenyek

def f7(label):
    print(label,": A verseny legjobbjai: ")
    eredmenyek.sort(key=lambda x: x[1], reverse=True)
    maxpont=eredmenyek[0][1]
    helyzes=1
    for i in range(len(eredmenyek)):
        if maxpont==eredmenyek[i][1]:
            print(str(helyzes)+". díj ("+str(eredmenyek[i][1])+" pont): "+eredmenyek[i][0])
        else:
            helyzes+=1
            if helyzes>3:
                break
            maxpont=eredmenyek[i][1]
            print(str(helyzes) + ". díj (" + str(eredmenyek[i][1]) + " pont): " + eredmenyek[i][0])

helyes = f1("1.feladat")
#f2("2.feladat")
#az=f3("3.feladat")
#f4("4.feladat",az)
#f5("5.feladat")
eredmenyek=f6()
f7("7.feladat")