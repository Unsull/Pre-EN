import math

# distance => ระยะทาง(s)
distance = input("Enter x1, y1, x2, y2: ").split()
x1, y1, x2, y2 = map(float, distance)

print("Please choose your distance:")
print("\t1 Euclidean distance")
print("\t2 Manhattan distance")

# choice => ทางเลือก
choice = int(input("Your choice: "))

if choice == 1 :
    euc = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    print("Euclidean distance = %.5f" % euc)

else :
    man = abs(x1 - x2) + abs(y1 - y2)
    print("Manhattan distance = %.5f" % man)