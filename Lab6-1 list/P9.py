n = int(input("Number of items in a list: "))
mylist = input("Enter %d integers for the list: " % n).split()
mylist = list(map(int, mylist))
x = int(input("Enter x: "))


# insert x in order
# 1 2 3 4 5 7 8 9 10
# insert 6
# 1) find position where mylist[i] >= x for the first time
# 2) insert at i

# Method 1
isDone = False # flag
for i in range(len(mylist)) :
    if mylist[i] >= x :
        print("Insert at", i)
        mylist.insert(i, x)
        isDone = True
        break
    
if not isDone :
    print("Insert at", len(mylist))
    mylist.append(x)

# print("Final list:", mylist)

print("Final list:", end=" ")

# range(len(mylist)) => print ตามจำนวนที่มีใน mylist 
for j in range(len(mylist)) :
    print(mylist[j], end=" ") # mylist[j] => start mylist number 0


# print("--- Method #2 ---")

# n = int(input("Number of items in a list: "))
# mylist = input("Enter %d integers for the list: " % n).split()
# mylist = list(map(int, mylist))
# x = int(input("Enter x: "))

# for i in range(len(mylist)) :
#     if mylist[i] >= x :
#         print("Insert at", i)
#         mylist.insert(i, x)
#         break

# else : #
#     print("Insert at", len(mylist))
#     mylist.append(x)

# print(mylist)




'''

# mylist put in increasing order
print(mylist)

# insert 10 ในตำแหน่งที่ 1
mylist.insert(1, 10) # .insert(pos, value)
print(mylist)

# remove last item
mylist.pop() # .pop => เอาตัวสุดท้ายออก
print(mylist)

# remove item at index 3
mylist.pop(3)
print(mylist)

'''

