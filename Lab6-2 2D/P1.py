s = input("Enter 2D list size (row,col): ").split()
r = int(s[0])
c = int(s[1])

all_list = []
for i in range(0, r) :
    x = input("Enter %d integers for row %d: " % (c, i)).split()
    x = list(map(int, x))
    all_list.append(x)

print(all_list)

print("In order:")
for item in all_list :
    # thing => ของ
    for thing in item :
        print(thing, end="\t")
    print()

print("Reverse col, same row:")
for item in all_list :
    item.reverse()
    for thing in item :
        print(thing, end="\t")
    item.reverse()
    print()

print("Same col, reverse row:")
all_list.reverse()
for item in all_list :
    for thing in item :
        print(thing, end="\t")
    print()

print("Reverse col, reverse row:")
for item in all_list :
    item.reverse()
    for thing in item :
        print(thing, end="\t")
    item.reverse()
    print()
    

'''

print("Reverse col, same row:")
for i in range(r) :
    for j in range(c, -1, -1) :
        print(num[i][j], end="\t")
    print()

'''