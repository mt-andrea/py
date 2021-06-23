print("Kérek két negatív számot!")
a=input("\ta: ")
b=input("\tb: ")
if a[0]=="-" and b[0]=="-":
    print("\tJó megoldás!")
elif a[0]!="-" and b[0]!="-":
    print("\tHiba: az a pozitív \n\tHiba: a b pozitív")
elif a[0]!="-":
    print("\tHiba: az a pozitív")
elif b[0]!="-":
    print("\tHiba: a b pozitív")
