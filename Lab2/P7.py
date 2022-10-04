import math

read = input("Enter x1, y1, x2, y2: ").split()

x1, y1, x2, y2 = map(float, read)
'''
x1 = float(read[0])
y1 = float(read[1])
x2 = float(read[2])
y2 = float(read[3])
'''

euclidean = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
print("Euclidean distance = %.6f " % euclidean)

manhattan = abs(x1 - x2) + abs(y1 - y2)
print("Manhattan distance = %.6f " % manhattan)