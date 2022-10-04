inputloop = True
while inputloop:
    tincome = input("Net Income: ") #รายรับ
    if tincome  == "q" or tincome == "Q":
        inputloop = False
        print("Bye")
    else:
        tincome = float(tincome)
        if tincome < 0:
            print("Wrong input: negative income.") #รายรับน้อยกว่า 0
        elif tincome <= 150000:
            tax = 0
            print("Tax = %.2f Baht" % tax)
        elif tincome <= 300000:
            tax = (tincome-150000)*0.05
            print("Tax = %.2f Baht" % tax)
        elif tincome <= 500000:
            tax = (tincome-300000)*0.10 + 7500 
            print("Tax = %.2f Baht" % tax)
        elif tincome <= 750000:
            tax = (tincome-500000)*0.15 + 7500 + 20000 - 5000
            print("Tax = %.2f Baht" % tax)
        elif tincome <= 1000000:
            tax = (tincome-750000)*0.20 + 7500 + 20000 + 37500 - 5000
            print("Tax = %.2f Baht" % tax)
        elif tincome <= 2000000:
            tax = (tincome-1000000)*0.25 + 7500 + 20000 + 37500 + 50000 - 5000
            print("Tax = %.2f Baht" % tax)
        elif tincome <= 5000000:
            tax = (tincome-2000000)*0.30 + 7500 + 20000 + 37500 + 50000 + 250000 - 5000
            print("Tax = %.2f Baht" % tax)
        else:
            tax = (tincome-5000000)*0.35 + 7500 + 20000 + 37500 + 50000 + 250000 + 900000 - 5000
            print("Tax = %.2f Baht" % tax)