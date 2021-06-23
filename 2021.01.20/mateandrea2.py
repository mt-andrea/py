langos=["Sima","Tejfölös","Sajtos","Sajtos-tejfölös"]
ar=[300,350,400,600]
for _ in range(len(langos)):
    i=_+1
    print(str(i)+" - "+langos[_]+" "+str(ar[_])+" Ft")
def elj(kod,darab):
    i=0
    while i!=kod-1:
        i+=1
    print("Fizetendő: "+str(ar[i]*darab))
print("Kérek három rendelést.")
for i in range(3):
    kod=int(input("Langos kódja:"))
    darab=int(input("Darab: "))
    elj(kod,darab)