import MateAndrea_class
species=[]
for i in range(3):
    name=input("Állat faja: ")
    mass=input("Tömege (kg): ")
    species.append(MateAndrea_class.Specie(name, mass))
maxind=0
for i in range(len(species)):
    if species[i].mass>species[maxind].mass:
        maxind=i
print("A legnehezebb állat: "+species[maxind].name)
f=open("legnehezebb.txt", "w")
f.write(species[maxind].name)
print("A fájl kiírása ... kész!")