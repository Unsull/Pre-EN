food = float(input("Food price: "))
drink = float(input("Drink price: "))

total = food + drink
print("Total Price = %.2f " % total, "Baht")

discount = ((food - food * 5 / 100) + drink)
print("Discount after check-in = %.2f" %discount, "Baht")

member = (total - (total * 10 / 100))
print("If you are a member, you would pay %.2f" % member, "Baht") 