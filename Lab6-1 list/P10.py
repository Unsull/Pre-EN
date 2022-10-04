mylist = input("Enter 10 integers: ").split()
mylist = list(map(int, mylist))

number = []

for x in range(len(mylist)) :
    # เช็คจำนวนตัวซ้ำ
    if mylist[x] not in number : # ถ้าเลขใน mylist ตัวที่ x ไม่มีใน number
        number.append(mylist[x])

print("Unique numbers:", end=" ")
for j in range(len(number)) :
    print(number[j], end=" ")