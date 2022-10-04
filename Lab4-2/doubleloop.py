a = 9
# selection
if a > 0:
    print("if xx")
else:
    print("Nope")

#iteration / loop
while a > 0:
    print(a, ": xx")
    a -= 1
print("------")
print(range(9))
for i in range(9):
    print(i, ": xx")
print("------")

# print x 5 times for each line
# do this for 10 times
for d in range(1,11): # ลูปนอก
    # for each day
    for r in range(1,6): # ลูปใน
        print(d,r,"x")
    print()

for d in range(1,11): # ลูปนอก
    # for each day
    for r in range(1,6): # ลูปใน
        print("x", end=" ") # บรรทัดเดียวกัน
    print()
print()

for d in range(1,11): # ลูปนอก
    # for each day
    for r in range(1,6): # ลูปใน
        print("x", end="-") # บรรทัดเดียวกัน
    print()


