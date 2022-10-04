mydict = {}

for i in range(10) :
    name, score = input("Enter name and score: ").split()
    score = float(score)
    mydict[name] = score
# print(mydict)

print("--------------------")
print("Sorted student data:")
for j in sorted(mydict.keys()) :
    print(j, end="\t")
    print(mydict[j])

print("--------------------")
# print("Student(s) with max score of 99.00: letter")
# print("Student(s) with min score of 7.00: bobby fred")
max_data = []
for m in mydict.keys() :
    # print(mydict[m])
    max_data.append(mydict[m])

max_data = max(max_data)
# print(max_data)
print("Student(s) with max score of %.2f: " % max_data ,end=" ")

for n in sorted(mydict.keys()) :
    if mydict[n] == max_data :
        print(n, end=" ")
print()

min_data = []
for a in mydict.keys() :
    # print(mydict[m])
    min_data.append(mydict[a])

min_data = min(min_data)
# print(max_data)
print("Student(s) with min score of %.2f: " % min_data ,end=" ")

for b in sorted(mydict.keys()) :
    if mydict[b] == min_data :
        print(b, end=" ")
print()

print("Student(s) who passes the exam >= 50.00:", end=" ")
for k in sorted(mydict.keys()) :
    if mydict[k] >= 50 :
        print(k, end=" ")
print()

average = 0
for count in sorted(mydict.keys()) :
    if mydict[count] :
        average += mydict[count]
# print(average)

average = average / len(mydict)
print("Student(s) who scored at least and above average score of %.2f: " % average , end=" ")
for n in sorted(mydict.keys()) :
    if mydict[n] >= average :
        print(n, end=" ")
print()

print("--------------------")
while True :
    name = input("Enter your query name: ")
    if name == "Quit" or name == "quit" :
        print("Bye")
        exit()

    elif name in mydict :
        if mydict[name] >= 50 :
            print("Score of %s is %.2f" % (name, mydict[name]))
            print("%s has PASSED the exam." % name)

        elif mydict[name] < 50 :
            print("Score of %s is %.2f" % (name, mydict[name]))
            print("%s has NOT passed the exam." % name)

    else :
        print("%s is not in the database." % name)