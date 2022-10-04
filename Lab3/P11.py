num = input("Enter x op y (+ - * / ^): ").split()

# print(list(num))
a = float(num[0])
op = num[1]
b = float(num[2])

#print(type(op))

if op == "+" :
    total = a + b
    print("%.3f" % total)

elif op == "-" :
    total = a - b
    print("%.3f" % total)

elif op == "*" :
    total = a * b
    print("%.3f" % total)

elif op == "/" :
    total = a / b
    print("%.3f" % total)

elif op == "^" :
    total = a ** b
    print("%.3f" % total)

else : # inputs other signs.
    print("Invalid op")