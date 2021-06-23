a=[]
b=[]
t=[]
ado=0
listAdo=[]
def inputFile(file,lista):
    f=open(file,"r") 
    for sor in f: 
        sor = sor[:-1]
        lista.append(int(sor))
    f.close()
def countAdo(i):
    if t[i]>4000:
        ado=t[i]*4
    else:
        ado=t[i]*3
    return ado
def printRecord(i):
    txt=str(a[i])+"m * "+str(b[i])+"m = "+str(t[i])+"m2 -> "+str(countAdo(i))+" Ft"
    print("\t"+txt)
def writeRecord(file,lista):
    f=open(file, "w+")
    for i in range(len(lista)):
        f.write(str(lista[i])+"\n")
    f.close()
def f1(label):
    print(label)
    inputFile("b.txt",b)
    inputFile("a.txt",a)
    for i in range(len(a)):
        t.append(a[i]*b[i])
    print("\tA beolvasás...kész!")
def f2(label):
    print(label)
    for i in range(len(a)-3,len(a)):
        printRecord(i)
def f3(label):
    print(label)
    maxInd=0
    for i in range(len(a)):
        if(t[i]>t[maxInd]):
           maxInd=i
    for i in range(len(a)):
        if t[i]==t[maxInd]:
            printRecord(i)
def f4(label):
    print(label)
    c=0
    for i in range(len(a)):
        if a[i]==b[i]:
            c+=1
    txt=str(c)+" négyzet alakú telek van."
    print("\t"+txt)
def f5(label):
    print(label)
    writeRecord("t.txt",t)
    print("\tA területek rögzítése... Kész.")
def f6(label):
    print(label)
    for i in range(len(t)):
        listAdo.append(countAdo(i))
    writeRecord("ado.txt",listAdo)
    print("\tFizetendő adó rögrítése... Kész.")
def f7(label):
    print(label)
    minInd=0
    for i in range(len(a)):
        if(t[i]<t[minInd]):
           minInd=i
    for i in range(len(a)):
        if t[i]==t[minInd]:
            printRecord(i)

f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5("5.feladat")
f6("6.feladat")
f7("7.feladat")