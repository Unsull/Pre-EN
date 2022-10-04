''' --------------------------
Put your functions here 
------------------------------'''

def read():
    while True :
        x = int(input("Please enter a positive integer: "))
        if x > 0 :
            return x
        print("Invalid input value. Please try again.")
    # ไม่จำเป็นต้องใส่ else ก็ได้ เพราะถ้า x > 0 จะ return แล้วออกจากฟังชั่นไปเลย

def findPower(base, power):
    return base ** power