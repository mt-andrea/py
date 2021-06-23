d=[1, -2, 45, 7, -18, 63, -45, 5, 70]
def f1(label):
    print(label)
    a=10000
    h=0
    while(a<100000):
        a*=1.2
        h+=1
    txt=str(h)+" hónap múlva "+str(int(a))+"Ft"
    print("\t"+txt)
def f2(label):
    print(label)
    txt="kérek egy pozitív egész számot: "
    x=int(input("\t"+txt))
    c=0
    while(x!=0):
        x//=10
        c+=1
    txt=str(c)+" jegyű a szám"
    print("\t"+txt)
def f3(label):
    print(label)
    i=0
    while(i<len(d)and not(d[i]>0 and d[i]%2==0)):
        i+=1
    if(i<len(d)):
        txt="az első pozitív páros szám: "+str(d[i])
    else:
        txt="nincs ilyen érték"
    print("\t"+txt)
def f4(label):
    print(label)
    s=0
    i=0
    while((i+1)<len(d)):
        s+=(d[i]-d[i+1])
        i+=1
    txt="a szomszédos elemek különbségének összege (while): "+str(s)
    print("\t"+txt)
    su=0
    for i in range(len(d)-1):
        su+=d[i]-d[i+1]
    t="a szomszédos elemek különbségének összege (for): "+str(su)
    print("\t"+t)

f1("1. feladat")
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")