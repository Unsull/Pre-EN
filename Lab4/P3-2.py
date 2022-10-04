x, op, y = input("Enter x op y (+ - * / // %): ").split()
x = float(x)
y = float(y)


while x != 0 or y != 0 :

    # valid operands
    if op == "+" :
       print("%.2f %s %.2f = %.2f" % (x, op, y, x+y)) 

    elif op == "-" :
        print("%.2f %s %.2f = %.2f" % (x, op, y, x-y)) 

    elif op == "*" :
        print("%.2f %s %.2f = %.2f" % (x, op, y, x*y))

    elif op == "/" :
        print("%.2f %s %.2f = %.2f" % (x, op, y, x/y))
        '''
        if y == 0 :
            print("divider is 0")
        else :
            print("%.2f %s %.2f = %.2f" % (x, op, y, x/y))
'''
    elif op == "//" :
        print("%d %s %d = %d" % (x, op, y, int(x)//int(y)))
        '''
        if y == 0 :
            print("divider is 0")
        else :
            print("%.2f %s %.2f = %.2f" % (x, op, y, x//y))
'''
    elif op == "%" :
        print("%d %s %d = %d" % (x, op, y, int(x)%int(y)))

    else :
        print("Wrong op.")

    x, op, y = input("Enter x op y (+ - * / // %): ").split()
    x = float(x)
    y = float(y)

# out of loop
print("Bye!")