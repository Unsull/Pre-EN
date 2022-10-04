w = float(input("Enter package weight: "))

if w > 0 :
    # valid weight
    if w <= 5 :
        cost = w * 20
    elif w <= 10 : # w > 5 kg.
        # First chuck : 5 * 20
        # second chuck : (w-5) * 30
        cost = (5 * 20) + ((w-5) * 30)
    else : # w > 10
        cost = (5 *20) + (5*30) + ((w-10) * 40)
    print("Total delivery cost is %.2f Baht" % cost)

else : # invalid weight
    print("Invalid weight. Bye.")