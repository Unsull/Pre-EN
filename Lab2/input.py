# input คือ การรับค่าเข้า

# input("") ปกติจะรับเป็น string
x = input("Enter an integer : ")
y = input("Enter your name : ")

# echo input data
print("Your x is :" , x)
print("Your name is :" , y)

# convert the input string an integer
xx = int(input("Enter an integer : "))
print(xx + 4)

zz = float(input("Enter a number : "))
print(zz)

''' 
This is a block comment
You can type many lines in this block
And the program will ignore them
    ใช้ comment ที่อธิบายหลายบรรทัด
'''

# รับค่า 2 ตัว แล้วแบ่งด้วย .split() 
name, last = input("Enter name and lastname : ").split()
print(name)
print(last)