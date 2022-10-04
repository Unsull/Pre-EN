order = int(input("The order for table: "))

item1 = input("Dish item: ")
many1 = int(input("How many: "))

item2 = input("Dish item: ")
many2 = int(input("How many: "))

item3 = input("Dish item: ")
many3 = int(input("How many: "))

totle = many1 + many2 + many3

print()
print("=================================")

print("Order for Table", order)
print("*", item1, ":", many1)
print("*", item2, ":", many2)
print("*", item3, ":", many3)
print("Total items : %d" %totle)
