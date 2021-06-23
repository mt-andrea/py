def f1(label):
    print(label)
    txt="kérek egy egész számot: "
    x=int(input("\t"+txt))
    c=0
    y=x
    while(y%2==0 and x!=0):
        y//=2
        c+=1
    txt=str(x)+"="+c*"2*"+str(y)
    print("\t"+txt)
def f2(label):
    print(label)
    x=1
    s=0
    while x!=0:
        txt="kérek egy egész számot: "
        x=int(input("\t"+txt))
        s+=x
    tx="összeg:"+str(s)
    print("\t"+tx)
def f3(label):
    print(label)
    i=0
    s=0
    print("\t",end="")
    while s+i+1<100:
        i+=1
        if i%2!=0:
            print(i,end=" ")
            s+=i
    txt="összeg: "+str(s)
    print("\n\t"+txt)
f1("1. feladat")
f2("2. feladat")
f3("3. feladat")