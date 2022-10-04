# P1
w = float(input("Enter package weight: "))

if w > 0 :
    # valid weight
    if w <= 5 :
        cost = w * 20
    elif w <= 10 : # w > 5 kg.
        # First chuck : 5 * 20
        # second chuck : (w-5) * 30
        cost = (5 * 20) + ((w-5) * 30)
    else : # w > 10
        cost = (5 *20) + (5*30) + ((w-10) * 40)
    print("Total delivery cost is %.2f Baht" % cost)

else : # invalid weight
    print("Invalid weight. Bye.")
    
#----------------------------------------------------------
# P2
height = float(input("Your height (cm): "))

if height >= 120 : # can ride
    print("Yes! You can play.")

else :
    print("Sorry, you need %.2f more cm to play." % (120 - height))

#----------------------------------------------------------

# P3
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

#----------------------------------------------------------

# P5
time = int(input("How many hours do you submit late? "))
print("")

score = int(input("What is your estimated score? "))

if time == 0 :
    total = score
    print("Your expected score is %.1f" % total)

elif time <= 24 :
    # cal => calculate
    cal = (score * 20 / 100)
    total = score - cal
    print("Your expected score is %.1f" % total)

elif time <= 48 :
    cal = (score * 50 / 100)
    total = score - cal
    print("Your expected score is %.1f" % total)

else :
    cal = (score * 100 / 100)
    total = score - cal
    print("Your expected score is %.1f" % total)

#----------------------------------------------------------

# P6
code, price = input("Enter product and price: ").split()
price = float(price)

# print(code[0])
p= 0
t = 0

if code[0] == "S" or code[0] == "s" :
    p = price
    t = 0
    
elif code[0] == "T" or code[0] == "t" :
    p = ((100/107) * price) # price / p = 107 / 100
    t = price - p

print("Price without tax = %.2f Baht" % p)
print("7%% Tax = %.2f Baht" % t) # ต้องใส่เป็น %% แล้วมันจะขึ้นเป็น %

#----------------------------------------------------------

# P11
num = input("Enter x op y (+ - * / ^): ").split()

# print(list(num))
a = float(num[0])
op = num[1]
b = float(num[2])

#print(type(op))

if op == "+" :
    total = a + b
    print("%.3f" % total)

elif op == "-" :
    total = a - b
    print("%.3f" % total)

elif op == "*" :
    total = a * b
    print("%.3f" % total)

elif op == "/" :
    total = a / b
    print("%.3f" % total)

elif op == "^" :
    total = a ** b
    print("%.3f" % total)

else : # inputs other signs.
    print("Invalid op")

#----------------------------------------------------------

# P12
import math

a, b, c = input("Enter coefficients a, b, c: ").split()
# list(map(func, var))

a = float(a)
b = float(b)
c = float(c)

x = b*b - 4*a*c

if a == 0 :
    print("This equation is not quadratic.")

elif x < 0 : # a != 0 for sure
    print("This equation has complex roots.")

else : # a != 0 for sure AND b*b - 4*a*c >= 0
    root1 = (-b + math.sqrt(x)) / (2*a)
    root2 = (-b - math.sqrt(x)) / (2*a)
    print("The 1st root = %.2f" % root1)
    print("The 2nd root = %.2f" % root2)