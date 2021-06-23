print("a - Bukarest\nb - Prága\nc - Budapest\nd - Pozsony\nKérem a helyes válasz betűjelét!")
valasz1=input("\tMagyarország főbárosa: ")
valasz2=input("\tCsehország fővárosa: ")
if valasz1=="c" and valasz2=="b":
    print("\tJó megoldás!")
elif valasz1!="c" and valasz2!="b":
    print("\tMagyarország fővárosa hibás!\n\tCsehország fővárosa hibás!")
elif valasz1!="c":
    print("\tMagyarország fővárosa hibás!")
elif valasz2!="b":
    print("\tCsehország fővárosa hibás!")
