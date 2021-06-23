x=int(input("Kérek egy számot: "))

if x%3==0 and x%5==0:
    print("A szám osztható 3-mal és 5-tel.")
elif x%3==0:
    print("A szám osztható 3-mal, de 5-tel nem.")
elif x%5==0:
    print("A szám osztható 5-tel, de 3-mal nem.")
else:
    print("A szám nem osztható 3-mal, sem pedig 5-tel.")