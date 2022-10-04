s = int(input("Enter a size: "))
mylist = input("Enter %d integers: " % s).split()
mylist = list(map(int, mylist))

print("In order:")
for i in range(s) : # range(len(mylist))
    print(mylist[i], end = " ")
print()

print("Reverse order:")
for i in range(s) :
    # s = 5, s-1 = 4
    # s-1-i = 4, 3, 2, 1, 0 : i = 1...4
    print(mylist[s-1-i], end = " ")
print()




'''

print("Reverse order:")
for i in range(s-1, -1, -1) :
    print(mylist[i], end = " ")
print()

print("Reverse order:")
mylist.reverse() # ..reverse() => list เปลี่ยน
for i in range(len(mylist)):
    print(mylist[i], end = " ")
print()

'''