nevek=["Dima Sabrina","Guttmann Beatrix","Borsodi Zámor","Dima Katalin",
       "Kiss Mira","Horváth Zselyke","Leitner Ferenc","Csongor Juvenál",
       "Moser Hanna","Kocsis Szófia","Karácsonyi Rebeka", "Veress Kira",
       "Kótai Hanna"]
sorrend = [4,1,9,6,3,13,10,5,2,7,12,11,8]

def f1(label):
    print(label)
    print("\t"+str(len(nevek)))
def f2(label):
    print(label)
    sorszam=len(nevek)
    i=0
    while sorrend[i]!=sorszam:
        i+=1
    print("\t"+nevek[i])
def f3(label):
    print(label)
    i=0
    while nevek[i]!="Kiss Mira":
        i+=1
    sorszam=sorrend[i]+1
    i=0
    while sorrend[i]!=sorszam:
        i+=1
    print("\t"+nevek[i])
def f4(label):
    print(label)
    i=0
    while nevek[i]!="Kótai Hanna":
        i+=1
    print("\t"+str(sorrend[i]-1))
def f5(label):
    print(label)
    for i in range(1,4):
        j=0
        while sorrend[j]!=i:
            j+=1
        print("\t"+nevek[j])
#Kiss Mira és Kocsis Szófia között kik szerepelnek
def f6(label):
    print(label)
    ind1=nevek.index("Kiss Mira")
    ind2=nevek.index("Kocsis Szófia")
    indexek=[]
    if sorrend[ind2]<sorrend[ind1]:
            ind1,ind2=ind2,ind1
    for i in range(len(nevek)):
        if sorrend[ind1]<sorrend[i]<sorrend[ind2]:
            indexek.append(i)
    for i in indexek: 
        print("\t"+nevek[i])

f1("1. feladat")
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")
f5("5. feladat")
f6("6. feladat")
