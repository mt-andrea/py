import mateandrea_class
rekordok=[]
rekordok.append( mateandrea_class.Homerseklet("Veszprém", 10, 15)  )  
rekordok.append( mateandrea_class.Homerseklet("Sé", 12, 20)  )  
rekordok.append( mateandrea_class.Homerseklet("Szeged", 9, 25)  ) 
nev=input("Város: ")
mini=int(input("Minimum: "))
maxi=int(input("Maximum: "))
rekordok.append(mateandrea_class.Homerseklet(nev,mini,maxi))
f=open("diff.txt","w")
for i in range(len(rekordok)):
    print(rekordok[i].nev+": "+str(rekordok[i].kulonbseg())+" fok")
    f.write(rekordok[i].nev+": "+str(rekordok[i].kulonbseg())+" fok\n")
print("A fájl kiírása ... kész!")
