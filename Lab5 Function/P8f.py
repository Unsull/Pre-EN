''' --------------------------
Put your functions here 
------------------------------'''

def fact(n): # ใส่ n เข้าไปเป็น argument
    f = 1
    for i in range(1, n+1) :
        f *= i
    return f