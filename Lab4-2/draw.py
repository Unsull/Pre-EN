n = 9

print("--- filled box ---")
for r in range(1, n+1) :
    for c in range(1, n+1) :
        print("+", end=" ")
    print()

print("--- empty box ---")
# r => ตัวหน้า เช่น 2,3 r = 2
# c => ตัวหลัง เช่น 2,3 r = 3
for r in range(1, n+1) :
    for c in range(1, n+1) :
        if r == 1 or r == n :
            print("+", end=" ")
        elif c == 1 or c == n :
            print("+", end=" ")
        else :
            print(" ", end=" ")
    print()

print("--- cross ---")
for r in range(1, n+1) :
    for c in range(1, n+1) :
        if r == c :
            print("+", end=" ")
        elif c + r == n+1 :
            print("+", end=" ")
        else :
            print(" ", end=" ")
    print()

print("--- plus ---")
for r in range(1, n+1) :
    for c in range(1, n+1) :
        if r == (n+1)/2 : # assume n odd
            print("+", end=" ")
        elif c == (n+1)/2  :
            print("+", end=" ")
        else :
            print(" ", end=" ")
    print()

print("--- star ---")
for r in range(1, n+1) :
    for c in range(1, n+1) :
        if r == (n+1)/2 :
            print("+", end=" ")
        elif c == (n+1)/2  :
            print("+", end=" ")
        elif r == c :
            print("+", end=" ")
        elif c + r == n+1 :
            print("+", end=" ")
        else :
            print(" ", end=" ")
    print()