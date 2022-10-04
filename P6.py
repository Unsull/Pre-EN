code, price = input("Enter product and price: ").split()
price = float(price)

# print(code[0])
p= 0
t = 0

if code[0] == "S" or code[0] == "s" :
    p = price
    t = 0
    
elif code[0] == "T" or code[0] == "t" :
    p = ((100/107) * price) # price / p = 107 / 100
    t = price - p

print("Price without tax = %.2f Baht" % p)
print("7%% Tax = %.2f Baht" % t) # ต้องใส่เป็น %% แล้วมันจะขึ้นเป็น %