def get_user() :
    items = {}

    while True:
        to_do = input("To do: ")
        if len(to_do) > 0 :
            details = input("* details: ")
            items[to_do] = details
        else :
            break
    return items


items = get_user()
# print(items)

print("You have  %d thing(s) to do:" % len(items))

for k in sorted(items.keys()):
    print("*", k)

# choice => ทางเลือก
choice = input("Command (enter name for details or 'all' for everything): ")

while True :
    if choice in items :
        # for k, v in items.items() :
        #     print("*", k)
        #     print("**", v)
        # print("Bye")
        # break

        print("*", choice)
        print("**", items[choice])
        print("Bye")
        break

    elif choice == "all" :
        for k in sorted(items.keys()):
            print("*", k)
            print("**", items[k])
        print("Bye")
        break

    else :
        print("Bye")
        break