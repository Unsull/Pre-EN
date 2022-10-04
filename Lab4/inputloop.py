# repeaatdly get inputs from a user
# stop when the number is not positive

n = 1

while n > 0 : # condition to continue
    n = int(input("Enter a pos num: "))
print("---Stop---")

while True : # fovever loop
    n = int(input("Enter a pos num: "))
    if n <= 0 : # consd to stop
        break # get out of the loop

print("---Stop---")