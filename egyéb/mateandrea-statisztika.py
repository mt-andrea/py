nevek=[]; kg=[]; cm=[]
def inputFile(file,lista):
    f=open(file,"r")
    for sor in f:
        sor=sor[:-1]
        lista.append(sor)
    f.close()
def printRecord(i):
    txt=nevek[i]+"\t"+cm[i]+" cm\t"+kg[i]+" kg"
    print("\t"+txt)
def f1(label):
    print(label)
    inputFile("nevek.txt",nevek)
    inputFile("kg.txt",kg)
    inputFile("cm.txt",cm)
    print("\tA beolvasás... kész!")
def f2(label):
    print(label)
    for i in range(0,8):
        printRecord(i)
def f3(label):
    print(label)
    maxInd=0
    for i in range(len(nevek)):
        if int(cm[i])>int(cm[maxInd]):
            maxInd=i
    printRecord(maxInd)
def f4(label):
    print(label)
    i=0
    while nevek[i]!="Szigeti":
        i+=1
    szigeti_kg=int(kg[i])
    for i in range(len(nevek)):
        if int(kg[i])>szigeti_kg:
            printRecord(i)
def f5(label):
    print(label)
    minInd=0
    for i in range(len(nevek)):
        if int(cm[i])<int(cm[minInd]):
            minInd=i
    min_cm=int(cm[minInd])
    for i in range(len(nevek)):
        if int(cm[i])==min_cm:
            printRecord(i)
def f6(label):
    print(label)
    for i in range(len(nevek)):
        tti=int(kg[i])/((int(cm[i])/100)**2)
        if tti<18:
            printRecord(i)
def f7(label):
    print(label)
    for i in range(len(nevek)):
        if (int(cm[i])<180 and int(cm[i])>160) and (int(kg[i])>105 or int(kg[i])<65):
            printRecord(i)
f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5("5.feladat")
f6("6.feladat")
f7("7.feladat")
