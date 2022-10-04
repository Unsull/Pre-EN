k = int(input("Input number of value(s): "))
x = input("").split()
# x = list(map(float, input().split())) => input x in x[x0, x1, x2, ..., xn]

x = list(map(float, x))
mk = x[0]

if k >= 1 :
    # i คือค่าของ x[0], x[1], ..., x[n]
    # x[0:len(x)] => เริ่มจากค่าที่ 0 
    for i in x[0:len(x)] : # len(x) => จำนวนสมาชิกใน x
        mk = (i + mk) / 2
        # print(i)
    print("Weighted Avg = %.4f" % mk)



