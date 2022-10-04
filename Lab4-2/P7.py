n = int(input("Enter n: "))

for i in range(n) : 
    # นับจาก n ลงไปเรื่อยๆ
    for j in range(i, n) : # เริ่มที่ i ถึง n-1
        print(" ", end=" ")
    
    for j in range(i+1) :
        print("*", end=" ")
        
    print()