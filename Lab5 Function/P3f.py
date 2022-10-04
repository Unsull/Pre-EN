''' --------------------------
Put your functions here 
------------------------------'''

def getInput():
    while True :
        x = int(input("Enter a 2-digit number: "))
        if x >= 0 and x <= 99 :
            return x        

def checkLottery(lot, guess):
    # no return
    if lot == guess :
        print("Congratulations!")

    elif guess - lot <= 10 and guess - lot > 0 :
        print("Almost got it")

    elif lot - guess <= 10 and lot - guess > 0 :
        print("Almost got it")

    else :
        print("No, sorry :(")