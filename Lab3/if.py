# method 3

height = float(input("Enter hight: "))
price = float(input("Enter price: "))

if height < 90 :
    print("Free")
    pay = 0

elif height < 120 : # height >= 90
    print("Half")
    pay = 0.5 * price

else : # height >= 120
    print("Full")
    pay = price 

print("You pay %.2f Baht." % pay)