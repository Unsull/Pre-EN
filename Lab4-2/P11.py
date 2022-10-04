w = int(input("Enter size: "))
h = (2*w) - 1

while True :
    dg = int(input("Enter a digit (0-9): "))
    if w < 1 or dg > 9 or dg < 0:
        print("Bye!")
        break

    elif dg == 0 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 or r == h :
                    print("*", end=" ")
                elif c == 1 or c == w :
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 1 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if c == w :
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 2 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 or r == w or r == h :
                    print("*", end=" ")
                elif c == w and r <= w : # upper right
                    print("*", end=" ")
                elif c == 1 and r >= w : # lower left
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 3 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 or r == w or r == h :
                    print("*", end=" ")
                elif c == w : # w คือ แถวตรงกลาง
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 4 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == w : # middle row
                    print("*", end=" ")
                elif c == 1 and r <= w : # upper left
                    print("*", end=" ")
                elif c == w : # right
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 5 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 or r == w or r == h :
                    print("*", end=" ")
                elif c == 1 and r <= w : # upper left
                    print("*", end=" ")
                elif c == w and r >= w : # lower right
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 6 :
         for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 or r == w or r == h :
                    print("*", end=" ")
                elif c == 1 : # left
                    print("*", end=" ")
                elif c == w and r >= w : # lower right
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 7 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 :
                    print("*", end=" ")
                elif c == w :
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 8 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 or r == w or r == h :
                    print("*", end=" ")
                elif c == 1 or c == w :
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()

    elif dg == 9 :
        for r in range(1, h+1):
            for c in range(1, w+1):
                if r == 1 or r == w or r == h :
                    print("*", end=" ")
                elif c == 1 and r <= w : # upper left
                    print("*", end=" ")
                elif c == w : # right
                    print("*", end=" ")
                else :
                    print(" ", end=" ")
            print()