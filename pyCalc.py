def msg(s="<string>"):
    print("-" * 30)
    print(s.center(30))
    print("-" * 30)
    print()


msg("pyCalc")
n1 = int(input("Number: "))
n2 = int(input("Number: "))
tot = n1 + n2

print()
print(f"{n1} + {n2} = {tot}")
print()
