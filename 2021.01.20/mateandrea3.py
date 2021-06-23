import mateandrea_class
rec=[]
f=open("jegyek.txt", "r",encoding="utf-8")
for sor in f:
    if sor[-1]=="\n":
        sor=sor[:-1].split(";")
    else:
        sor=sor.split(";")
    rec.append(mateandrea_class.Tanulo(sor[0],int(sor[1]),int(sor[2]),int(sor[3]),int(sor[4]),int(sor[5])))
print("A fájl beolvasása ... kész!")
for i in range(len(rec)):
    print(rec[i].nev+" átlaga: "+rec[i].kimenet())