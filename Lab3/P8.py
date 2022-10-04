# i => income
i = float(input("Net Income: "))

if i < 0 :
    print("Wrong input: negative income.")

elif i <= 150000 :
    tax = i * 0
    print("Tax = %.2f Baht" % tax)

elif i <= 300000 :
    # tax max => 7500
    tax = (i - 150000 ) * 5 / 100
    print("Tax = %.2f Baht" % tax)

elif i <= 500000 : 
    # tax max => 20000
    tax = (i - 300000) * 10 / 100 + 7500
    print("Tax = %.2f Baht" % tax)

elif i <= 750000 :
    # tax max => 37500
    tax = (i - 500000) * 15 / 100 + 27500 # 20000 + 7500
    print("Tax = %.2f Baht" % tax)

elif i <= 1000000 :
    # tax max => 50000
    tax = (i - 750000) * 20 / 100 + 65000
    print("Tax = %.2f Baht" % tax)

elif i <= 2000000 :
    # tax max => 250000
    tax = (i - 1000000) * 25 / 100 + 115000
    print("Tax = %.2f Baht" % tax)

elif i <= 5000000 :
    # tax max => 900000
    tax = (i - 2000000) * 30 / 100 + 365000
    print("Tax = %.2f Baht" % tax)

else :
    tax = (i - 5000000) * 35 / 100 + 1265000
    print("Tax = %.2f Baht" % tax)