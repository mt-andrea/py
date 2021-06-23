alma=[]
megye=[]
listP=[]
p=0
def inputFile(file,lista,isInt):
    f=open(file,"r",encoding="utf-8") 
    for sor in f: 
        if sor[-1]=="\n":
            sor = sor[:-1]
        if isInt:
            sor = int(sor)
        lista.append(sor)
    f.close()
def countP(ind):
    s=0
    for i in range(len(alma)):
        s+=alma[i]
    p=round((alma[ind]/s)*100, 2)
    return p
def printRecord(i):
    txt=megye[i]+" "+str(alma[i])+" t ->"+str(listP[i])+" %"
    print("\t"+txt)
def f1(label):
    print(label)
    inputFile("alma.txt",alma,True)
    inputFile("megye.txt",megye,False)
    for i in range(len(alma)):
        listP.append(countP(i))
    print("\tA beolvasás...kész!")
def f2(label):
    print(label)
    for i in range(len(alma)):
        if megye[i]=="Pest":
           printRecord(i)
        if megye[i]=="Zala":
           printRecord(i)
def f3(label):
    print(label)
    indZ=0
    for i in range(len(alma)):
        if megye[i]=="Zala":
            indZ=i
    for i in range(len(alma)):
        if alma[i]>alma[indZ]:
            printRecord(i)
def f4(label):
    print(label)
    indB=0
    indN=0
    counter=0
    for i in range(len(alma)):
        if megye[i]=="Baranya":
            indB=i
        if megye[i]=="Nógrád":
            indN=i
    if alma[indB]>alma[indN]:
        alma[indB],alma[indN]=alma[indN],alma[indB]
    for i in range(len(alma)):
        if alma[i]>alma[indB] and alma[i]<alma[indN]:
            printRecord(i)
            counter+=1
    if counter==0:
        print("\tNincs ilyen megye")
    print("TEST")
    indT=0
    indF=0
    counter=0
    for i in range(len(alma)):
        if megye[i]=="Tolna":
            indT=i
        if megye[i]=="Fejér":
            indF=i
    if alma[indT]>alma[indF]:
        indT,indF=indF,indT
    for i in range(len(alma)):
        if alma[i]>alma[indT] and alma[i]<alma[indF]:
            printRecord(i)
            counter+=1
    if counter==0:
        print("\tNincs ilyen megye")
f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")