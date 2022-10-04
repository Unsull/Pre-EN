debt = float(input("Enter credit card debt: "))
pay = float(input("Enter monthly payment: "))

debt1 = 0
m = 1
sum = 0

while True :
    debt1 = (debt * 1.5 / 100)
    sum = debt1 + debt - pay
    debt = sum
    if debt < 0 :
        # print("Month %d : Debt is paid off" % (m))
        break

    if sum < pay :
        print("Month %d : %.2f" % (m, sum))

    if sum < pay :
        print("Month %d : Debt is paid off" % (m+1))
        break
    
    elif sum >= pay :
        print("Month %d : %.2f" % (m, sum))

    else :
        print("Month %d : Debt is paid off" % (m+1))

    m += 1

if debt < 0 :
     print("Month %d : Debt is paid off" % (m))
else  :    
    sum = debt * 1.5 / 100
    sum1 = sum + debt
    total = (m * pay) + sum1
    print("Total payment = %.2f" % total)
# print(debt1)
# print(sum)