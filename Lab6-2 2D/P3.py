# 4x4 metrix
# 1) get inputs for A
print("Input values for the matrix A: ")

A = []
for i in range(4) : # for each row
    aa = input("Row %d: "%i).split()
    aa = list(map(int, aa)) # aa is a list
    A.append(aa)

# 2) show A
# print(A)
print("Matrix A")
for item in A :
    # print(item)
    for thing in item: # print liats A[0], A[1], ..., A[n]
        print(thing, end=" ")
    print()

# 3) calc B
# B = A + At
B = []
for r in range(4) :
    bb = []
    for c in range(4) :
        # A[r][c] + At[r][c]
        x = A[r][c] + A[c][r]
        bb.append(x)
    B.append(bb)
    
# 4) show B
print("Matrix B")
for item in B :
    for thing in item :
        print(thing, end=" ")
    print()


'''

print("A: rev col, same row")
for r in range(4): # r = 0,1,2,3
    for c in range(3,-1,-1): # c = 3,2,1,0
        print(A[r][c], end="\t")
    print()
    
'''