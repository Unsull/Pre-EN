for r in range(1, 13) :
    for c in range(1, 13) :
        print("(%d, %d)" % (r, c), end=" ")
    print()
print()

for r in range(1, 13) :
    for c in range(1, 13) :
        #print("(%d, %d" % (r, c), end=" ")
        print(r*c, end=" ")
    print()