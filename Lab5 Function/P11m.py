''' --------------------------
Do not change anything here 
------------------------------'''
import P11f

''' --------------------------
Put your code for the main part here 
------------------------------'''
if __name__ == "__main__":
    income = P11f.rdIncome()
    if P11f.isValid(income):
        print("Income: %d" % income)
        print("Tax: %d" % P11f.compTax(income))
    else:
        print("Invalid income.")
