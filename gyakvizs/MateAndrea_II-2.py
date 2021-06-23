title=input("Kérem egy film címét: ")
duration=int(input("Kérem az előbbi film hosszát percekben: "))
def h_min():
    h=duration//60
    mins=duration%60
    print("A(z) "+title+" című film "+str(h)+" óra és "+str(mins)+" perc hosszú.")
h_min()