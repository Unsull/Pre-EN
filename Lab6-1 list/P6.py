# mylist = input("Enter 13 integers: ").split()
# mylist = list(map(int, mylist))

# for i in range(13) :
#     n1 = mylist[i]
#     n2 = mylist[12]
#     if n1 == n2 :
#         x = 0

#         n2 = mylist[i+13-1]
#         x += 1

#     elif mylist[6] :
#         pass

#     else :
#         print("Not symmetric.")
#         break

# if x == 1 :
#     print("Symmetric.")

mylist = input("Enter 13 integers: ").split()
mylist = list(map(int, mylist))

n1 = mylist[0] + mylist[1] + mylist[2] + mylist[3] + mylist[4] + mylist[5]
n2 = mylist[7] + mylist[8] + mylist[9] + mylist[10] + mylist[11] + mylist[12]

if n1 != n2 :
    print("Not symmetric.")

elif n1 == n2 :
    print("Symmetric.")