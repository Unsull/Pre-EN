n = int(input("Enter n: "))


for i in range(1, n+1) :
    # print(i, end=" ")
    if (i + 4) % 5 == 0 :
        print("!", end="")
    else :
        print("*", end="")