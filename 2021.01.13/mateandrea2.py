def eljaras(nev,ido):
    if 60-ido>=0:
        print("\t"+nev+": "+str(60-ido)+" perce maradt")
    else:
        print("\t"+nev+": idő túllépés")

print("Kérek három nevet és percben a felhasznál időt.")
for i in range(3):
    nev=input("\tNév: ")
    ido=int(input("\tIdő (perc): "))
    eljaras(nev,ido)