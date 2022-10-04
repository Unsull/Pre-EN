import random

z= 5
y = 10
z = 20
# list : room / room number : data slot / index
mylist = [5, 10, 15]
print(type(mylist))
print(mylist)


# random 100 integers
# put them into a list
# print them
intlist = [] # empty list
for i in range(100) :
    r = random.randint(0, 99)


# mylist put in increasing order
print(mylist)

# insert 10 ในตำแหน่งที่ 1
mylist.insert(1, 10) # .insert(pos, value)
print(mylist)

# remove last item
mylist.pop() # .pop => เอาตัวสุดท้ายออก
print(mylist)

# remove item at index
mylist.pop(3)
print(mylist)