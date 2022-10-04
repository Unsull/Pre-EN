while True :
    i = input("Net Income: ")

    # lower => เป็นเมธอดของ str เปลี่ยนตัวอักษรเป็นพิมพ์เล็ก
    while i.lower() == "q" :
        print("Bye")
        exit() # exit() => stop program

    i = float(i)
    while i < 0 :
        print("Wrong input: negative income.")
        break

    while i == 0 :
        tax = 0
        print("Tax = %.2f Baht" % tax)
        break

    while i > 0 :
        if i <= 150000 :
            tax = i * 0
            print("Tax = %.2f Baht" % tax)
            break

        elif i <= 300000 :
            tax = (i - 150000 ) * 5/100
            print("Tax = %.2f Baht" % tax)
            break

        elif i <= 500000 :
            tax = ((i - 300000) * 10/100) + (150000 * 5/100)
            print("Tax = %.2f Baht" % tax)
            break

        elif  i <= 750000 :
            # 200000 => 500000 - 300000 จากตัวข้างบน
            tax = ((i - 500000) * 15/100) + (150000 * 5/100) + (200000 * 10/100) 
            print("Tax = %.2f Baht" % tax)
            break

        elif  i <= 1000000 :
            tax = ((i - 750000) * 20/100) + (150000 * 5/100) + (200000 * 10/100) + (250000 * 15/100) 
            print("Tax = %.2f Baht" % tax)
            break

        elif i <= 2000000 :
            tax = ((i - 1000000) * 25/100) + (150000 * 5/100) + (200000 * 10/100) + (250000 * 15/100) + (250000 * 20/100) 
            print("Tax = %.2f Baht" % tax)
            break

        elif i <= 5000000 :
            tax = ((i - 2000000) * 30/100) + (150000 * 5/100) + (200000 * 10/100) + (250000 * 15/100) + (250000 * 20/100) + (1000000 * 25/100) 
            print("Tax = %.2f Baht" % tax)
            break

        else :
            tax = ((i - 5000000) * 35 / 100) + (150000 * 5/100) + (200000 * 10/100) + (250000 * 15/100) + (250000 * 20/100) + (1000000 * 25/100) + (3000000 * 30/100) 
            print("Tax = %.2f Baht" % tax)
            break

