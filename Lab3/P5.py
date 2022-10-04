time = int(input("How many hours do you submit late? "))
print("")

score = int(input("What is your estimated score? "))

if time == 0 :
    total = score
    print("Your expected score is %.1f" % total)

elif time <= 24 :
    # cal => calculate
    cal = (score * 20 / 100)
    total = score - cal
    print("Your expected score is %.1f" % total)

elif time <= 48 :
    cal = (score * 50 / 100)
    total = score - cal
    print("Your expected score is %.1f" % total)

else :
    cal = (score * 100 / 100)
    total = score - cal
    print("Your expected score is %.1f" % total)