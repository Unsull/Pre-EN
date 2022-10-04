print("=== Membership Application === \n")

first_name = input("Please enter the applicant's first name: ")
family_name = input("Last name: ")

birthday= input("Your birthday (year month date): ").split()
birthday[0] = int(birthday[0])
birthday[1] = str(birthday[1])
birthday[2] = int(birthday[2])
age = 2022 - birthday[0]

blessing = input("Your blessing: ")
print()

print("Welcome %s, %s (%d / %s / %d , age %d)" % (family_name, first_name, birthday[0], birthday[1], birthday[2], age))
print(blessing)