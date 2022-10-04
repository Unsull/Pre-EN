mylist = input("Enter 13 integers: ").split()
mylist = list(map(int, mylist))

if mylist[0] == mylist[12] :
    if mylist[1] == mylist[11] :
        if mylist[2] == mylist[10] :
            if mylist[3] == mylist[9] :
                if mylist[4] == mylist[8] :
                    if mylist[5] == mylist[7] :
                        if mylist[6] == mylist[8] :
                            print("Symmetric.")
                        else :
                            print("Not symmetric.")
                    else :
                        print("Not symmetric.")
                else :
                    print("Not symmetric.") 
            else :
                print("Not symmetric.")
        else :
            print("Not symmetric.")
    else :
        print("Not symmetric.")
else :
    print("Not symmetric.")
