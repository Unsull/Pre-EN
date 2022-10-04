mylist = []

while True :
    item = input("Item to buy: ")
    if item == "" :
        break
    else :
        mylist.append(item)

print("There are %d items in your shopping list:" % len(mylist))
print(mylist)

if len(mylist) > 5:
    print("Too many items, removing %d last items" % (len(mylist) - 5))
    
    n = len(mylist) - 5
    print(mylist[0:len(mylist)-n])
    print("Final shopping list: ")

'''
if len(mylist) > 5 :
    print("Too many items, removing %d last items" % (len(mylist) - 5))
    print("Final shopping list: ")

    for i in list(mylist) :
        if len(mylist) :
            mylist.remove(i)
    
    # for i in range(5, len(mylist)) : # ตั้งแต่ตัวที่ 6 ถึงตัว สุดท้าย
    #     mylist.pop(5) # remove ตัวที่ 5 ออกไปเรื่อยๆ
    #     # print(mylist)
    

    print(mylist)

'''