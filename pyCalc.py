from functionalities msg, operator

msg("pyCalc")
n1 = int(input("Number: "))
op = str(input("Operator [+ - * /]: "))
n2 = int(input("Number: "))

tot = operator(op, n1, n2)



print()
print(f"{n1} {op} {n2} = {tot}")
print()
