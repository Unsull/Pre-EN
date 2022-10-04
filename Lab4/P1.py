n = int(input("Enter n: "))

for i in range(1, n+1) :
    # end=" " => add space instead of /n
    print(i, end =" ")
print("\n-----------------")

for i in range(1, n+1) :
    print(i, end =" ")
    if i % 10 == 0 : # หาร 10 ลงตัว
        print() # \n เคาะบรรทัด
print("\n-----------------")

for i in range(1, n+1) :
    if i % 5 == 0 :
        print("X", end=" ")
    else :
        print(i, end=" ")

    # เช็ค if แยก 10 ตัว เคาะบรรดทัด
    if i % 10 == 0 :
        print() 
print("\n-----------------")