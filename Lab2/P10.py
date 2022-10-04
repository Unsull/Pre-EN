print("Hi! I am a smart cashier!")
food = int(input("Enter the food cost: "))
pay = int(input("Enter the amount you pay: "))
print()

total = pay - food
print("Amount of change =", total)

num = int(total / 1000)
surp = total - num * 1000
print("\t", num, "\t", "1000-Baht bill(s)")

num1 = int(surp / 500)
surp1 = surp - num1 * 500
print("\t", num1, "\t", "500-Baht bill(s)")

num2 = int(surp1 / 100)
surp2 = surp1 - num2 * 100
print("\t", num2, "\t", "100-Baht bill(s)")

num3 = int(surp2 / 50)
surp3 = surp2 - num3 * 50
print("\t", num3, "\t", "50-Baht bill(s)")

num4 = int(surp3 / 20)
surp4 = surp3 - num4 * 20
print("\t", num4, "\t", "20-Baht bill(s)")

num5 = int(surp4 / 10)
surp5 = surp4 - num5 * 10
print("\t", num5, "\t", "10-Baht coin(s)")

num6 = int(surp5 / 5)
surp6 = surp5 - num6 * 5
print("\t", num6, "\t", "5-Baht coin(s)")

num7 = int(surp6 / 1)
surp7 = surp6 - num7 * 1
print("\t", num7, "\t", "1-Baht coin(s)")