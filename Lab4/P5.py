debt = float(input("Enter credit card debt: "))
pay = float(input("Enter monthly payment: "))

m = 1
total = debt

while True :
    total = (debt * 1.5 / 100) + total # เก็บค่าผลรวม total
    debt = ((debt * 1.5 / 100) + debt) - pay
    #print(sum)
    if debt < 0 :
        print("Month %d : Debt is paid off" % m)
        break

    elif debt > 0 :
        print("Month %d : %.2f" % (m, debt))

    m += 1

print("Total payment = %.2f" % total)