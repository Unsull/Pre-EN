count = int(input("Please enter a vector length (n): "))

v1 = input("Enter values of the vector v1: ").split()
v1 = list(map(float, v1))

v2 = input("Enter values of the vector v2: ").split()
v2 = list(map(float, v2))

print("v1:", v1)
print("v2:", v2)

total = 0
for i in range(0, count) :
    x = v1[i] * v2[i]
    total += x 


print("inner product = %.4f" % total)
