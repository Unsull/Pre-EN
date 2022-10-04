''' --------------------------
Do not change anything here 
------------------------------'''
import P3f
import random

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    # lot = 30
    lot = random.randrange(0,100) # random an integer
    # lotf = random.uniform(0,1) # random a floating point number
    guess = P3f.getInput()
    text = P3f.checkLottery(lot, guess)

    print("lottery number =", lot)

