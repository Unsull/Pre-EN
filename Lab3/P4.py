x = float(input("Enter x: "))
i = 1
count = 0
sum = 0 
sum1 = 0

while sum <= x : # เอาค่า sum มาเช็คกับ x
    sum = 1/i + sum1
    count += 1
    print("Round %d : sum = %.5f" % (count, sum))

    sum1 = sum # update for next round
    i += 1

