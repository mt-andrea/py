import metjelentes_class

rec=[]
def f1():
    f=open("tavirathu13.txt","r",encoding="utf-8")
    for sor in f:
       sor=sor[:-1].split(" ")
       rec.append(metjelentes_class.Met(sor[0],sor[1],sor[2],int(sor[3])))

def f2(label):
    print(label)
    city=input("Adja meg egy település kódját! Település: ")
    maxind=0
    for i in range(len(rec)):
        if city==rec[i].city and int(rec[i].time)>int(rec[maxind].time):
            maxind=i
    print("Az utolsó mérési adat a megadott településről "+rec[maxind].time[:2]+":"+rec[maxind].time[2:]+"-kor érkezett")

def f3(label):
    print(label)
    maxi=0
    mini=0
    for i in range(len(rec)):
        if rec[i].temp>rec[maxi].temp:
            maxi=i
        elif rec[i].temp<rec[mini].temp:
            mini=i
    print("A legalacsonyabb hőmérséklet: "+rec[mini].city+" "+rec[mini].time[:2]+":"+rec[mini].time[2:]+" "+str(rec[mini].temp)+" fok. \nA legmagasabb hőmérséklet: "+rec[maxi].city+" "+rec[maxi].time[:2]+":"+rec[maxi].time[2:]+" "+str(rec[maxi].temp)+" fok.")

def f4(label):
    print(label)
    c=True
    for i in range(len(rec)):
        if rec[i].wind=="00000":
            print(rec[i].city+" "+rec[i].time[:2]+":"+rec[i].time[2:])
            c=False
    if c:
        print("Nem volt szélcsend a mérések idején.")

def med(city):
    temp01=[]
    temp07=[]
    temp13=[]
    temp19=[]
    temps=[]
    for i in range(len(rec)):
        if rec[i].city==city and rec[i].time[:2]=="01":
            temp01.append(rec[i].temp)
        elif rec[i].city==city and rec[i].time[:2]=="07":
            temp07.append(rec[i].temp)
        elif rec[i].city==city and rec[i].time[:2]=="13":
            temp13.append(rec[i].temp)
        elif rec[i].city==city and rec[i].time[:2]=="19":
            temp19.append(rec[i].temp)
    if temp01!=[] and temp07!=[] and temp13!=[] and temp19!=[]:

        temps+=temp01
        temps+=temp07
        temps+=temp13
        temps+=temp19
        s=0
        for _ in range(len(temps)):
                s+=temps[_]
        txt="Középhőmérséklet: "+str(round(s/len(temps),))
    else: 
        txt="NA"
    return txt

def avg(city):
    mini=0
    maxi=0
    for i in range(len(rec)):
        if rec[i].city==city and rec[i].temp>rec[maxi].temp:
            maxi=i
        elif rec[i].city==city and rec[i].temp<rec[mini].temp:
            mini=i
    txt="Hőmérséklet-ingadozás: "+str(rec[maxi].temp-rec[mini].temp)
    return txt

def f5(label):
    print(label)
    cities=[]
    for i in range(len(rec)):
        if rec[i].city not in cities:
            cities.append(rec[i].city)
    for j in range(len(cities)):
        print(cities[j]+" "+med(cities[j])+"; "+avg(cities[j]))
def f_write(city):
    filename=city+".txt"
    f=open(filename, "w")
    f.write(city+"\n")
    for _ in range(len(rec)):
        if rec[_].city==city:
            f.write(rec[_].time[:2]+":"+rec[_].time[2:]+" "+int(rec[_].wind[3:])*"#"+"\n")
    f.close()

def f6(label):
    print(label)
    cities=[]
    for i in range(len(rec)):
        if rec[i].city not in cities:
            cities.append(rec[i].city)
    for i in range(len(cities)):
        f_write(cities[i])
    print("A fájlok elkészültek.")

f1()
f2("2.feladat")
f3("3.feladat")
f4("4.feladat")
f5("5.feladat")
f6("6.feladat")