rec=[]

def imp_file(file,lista):
    f=open(file,"r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor = sor[:-1].split(";")
        else:
            sor = sor.split(";")
        lista.append([sor[0],sor[1],sor[2]])
    txt="A fájl beolvasása... kész!"
    print("\t"+txt)
def count_rec(lista):
    txt=str(len(lista))+" rekord van az adatbázisban."
    print("\t"+txt)
def count_name(name,lista):
    c=0
    for i in range(len(lista)):
        if name==lista[i][0]:
            c+=1
    return c
def name_please(name,lista):
    
    if name in lista[:][0]:
        i=0
        while lista[i][0]!=name:
            i+=1
        txt=name+" néven "+str(count_name(name,lista))+" időpontfoglalás van."
    else:
        txt="A megadott néven nincs időpont foglalás."
    print("\t"+txt)
def names_(lista,i):
    if rec[i][0] not in lista:
        lista.append(rec[i][0])
    
def time_please(time,lista):
    for i in range(len(rec)):
        if time==rec[i][1]:
            names_(lista,i)
    lista.sort()
    
def create_file(filename,time,lista):
    f=open(filename,"w")
    for i in range(len(lista)):
        f.write(lista[i]+"\n")
    txt="A "+filename+" fájl kiírása...kész!"
    print("\t"+txt)
def f1(label):
    print(label)
    imp_file("fogado.txt",rec)
def f2(label):
    print(label)
    count_rec(rec)
def f3(label):
    print(label)
    name=input("\tAdjon meg egy nevet: ")
    name_please(name,rec)
def f4(label):
    print(label)
    names=[]
    txt="Adjon meg egy érvényes időpontot (pl. 17:10): "
    time=input("\t"+txt)
    t=time.split(":")
    filename=t[0]+t[1]+".txt"
    time_please(time,names)
    create_file(filename,time,names)
    for i in range(len(names)):
        txt=names[i]
        print("\t"+txt)
f1("1.feladat")
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")