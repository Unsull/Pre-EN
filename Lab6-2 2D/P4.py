# 2x3 metrix

A = [[2, 44, 66],[50, 50, 45]]
B = [[33, 44, 55],[50, 50, 50]]

# print(a[0])

C = []
for r in range(2) :
    cc = []

    for c in range(3) :
        aa = A[r][c]
        bb = B[r][c]

        if aa == bb :
            print("[%d][%d]: A == B" % (r, c))
            x = 0
            cc.append(x)

        elif aa > bb :
            print("[%d][%d]: A > B" % (r, c))
            x = 1
            cc.append(x)

        elif aa < bb :
            print("[%d][%d]: A < B" % (r, c))
            x = -1
            cc.append(x)

    C.append(cc)

# print(C)
print("List c:")
for item in C :
    for thing in item :
        print(thing, end="\t")
    print()
