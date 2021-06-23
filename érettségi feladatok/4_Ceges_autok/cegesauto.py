import ceges_class
rec=[]
def f1():
    f=open("autok.txt","r",encoding="utf-8")
    for sor in f:
        if sor[-1]=="\n":
            sor=sor[:-1].split(" ")
        else:
            sor=sor.split(" ")
        rec.append(ceges_class.Cars(int(sor[0]),sor[1],sor[2],int(sor[3]),int(sor[4]),int(sor[5])))

def f2(label):
    print(label)
    last=0
    for i in range(len(rec)):
        if rec[i].day>rec[last].day and rec[i].in_out==0:
            last=i
            txt=str(rec[last].day)+". nap renszám: "+rec[last].car_id
    print("\t"+txt)

def f3(label):
    print(label)
    nap=int(input("Nap:"))
    print("Forgalom a ",nap,". napon:")
    for i in range(len(rec)):
        if rec[i].day==nap:
            if rec[i].in_out==0:
                txt=rec[i].time+" "+rec[i].car_id+" "+str(rec[i].emp_id)+" ki"
            else:
                txt=rec[i].time+" "+rec[i].car_id+" "+str(rec[i].emp_id)+" be"
            print("\t"+txt)

def f4(label):
    print(label)
    kint=[]
    for i in range(len(rec)):
        if rec[i].in_out==0:
            if rec[i].car_id not in kint:
                kint.append(rec[i].car_id)
        if rec[i].in_out==1:
            for j in range(len(kint)):
                if rec[i].car_id in kint:
                    kint.remove(rec[i].car_id)
    txt="A  hónap végén "+str(len(kint))+" autót nem hoztak vissza."
    print("\t"+txt)

def car_on_road(car):
    kml=[]
    for i in range(len(rec)):
        if car==rec[i].car_id:
            kml.append(rec[i].km)
    on_road=kml[-1]-kml[0]
    txt=car+" "+str(on_road)+" km"
    print("\t"+txt)

def f5(label):
    print(label)
    cars=[]
    for i in range(len(rec)):
        if rec[i].car_id not in cars:
            cars.append(rec[i].car_id)
    cars.sort()
    for i in range(len(cars)):
        car_on_road(cars[i])

def f6(label):
    print(label)
    trips=[]
    for i in range(len(rec)-1):
        if rec[i].in_out==0:
            j=i+1
            
            while rec[i].car_id!=rec[j].car_id and rec[i].emp_id!=rec[j].emp_id and j<len(rec)-1:
                j+=1
            if rec[i].car_id==rec[j].car_id and rec[i].emp_id==rec[j].emp_id:
                trips.append([rec[i].emp_id,rec[j].km-rec[i].km])
    maxInd=0
    for k in range(len(trips)):
        if trips[k][1]>trips[maxInd][1]:
            maxInd=k
    txt="A leghosszabb út: "+str(trips[maxInd][1])+" km, személy: "+str(trips[maxInd][0])
    print("\t"+txt)

def f7(label):
    print(label)
    x=input("Rendszám: ")
    filename=x+"_menetlevel.txt"
    f=open(filename,"w")
    for i in range(len(rec)):
        if rec[i].car_id==x:
            time1=str(rec[i].day)+". "+rec[i].time
            j=i+1
            while rec[i].car_id!=rec[j].car_id and rec[i].emp_id!=rec[j].emp_id and j<len(rec)-1:
                j+=1
            if rec[i].car_id==rec[j].car_id and rec[i].emp_id==rec[j].emp_id:
                time2=str(rec[j].day)+". "+rec[j].time
                f.write(str(rec[i].emp_id)+"\t"+time1+"\t"+str(rec[i].km)+" km"+"\t"+time2+"\t"+str(rec[j].km)+" km"+"\n")
            elif rec[i].in_out==0 and rec[i].car_id!=rec[j].car_id and rec[i].emp_id!=rec[j].emp_id:
                f.write(str(rec[i].emp_id)+"\t"+time1+"\t"+str(rec[i].km)+" km"+"\n")
    print("Menetlevél kész.")

f1()
f2("2. feladat")
f3("3. feladat")
f4("4. feladat")
f5("5. feladat")
f6("6. feladat")
f7("7. feladat")