''' --------------------------
Put your functions here 
------------------------------'''

def rdIncome():
    x = float(input("Enter your income: "))
    return x

def isValid(income):
    if income >= 0 and income <= 1000000 :
        return True

    else :
        return False

def compTax(income):
    if income <= 150000 :
        tax = 150000 * 0
        return tax

    elif income <= 500000 :
        tax = (150000 * 0) + ((income - 150000) * 0.1)
        return tax

    elif income <=  1000000 :
        tax = (150000 * 0) + (350000 * 0.1) + ((income - 500000) * 0.2)
        return tax