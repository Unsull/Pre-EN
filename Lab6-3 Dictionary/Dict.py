# list:
# position = 0, 1, 2, ..., n-1
# x[pos]
x = [1, 2, 3, 4, 5]

# dictionary
# no order
# key : value
# mydict[key] = value
mydict = {"milk": 2, "egg": 1, "ham": 2}
print(mydict)
print(mydict["milk"])
k = "jam"

# if k in mydict.keys()
if k in mydict : # search k in keys
    print(mydict[k])
else :
    print("Add %s in dict" % k)
    mydict[k] = 10 # add key:value pair in dict
print(mydict)

# for k in mydict:
# no order
for k in mydict.keys() :
    print(k, ":", mydict[k])

print(type(mydict.keys()))

for k in sorted(mydict.keys()):
    print(k, ":", mydict[k])

print(len(mydict))


# mydict.pop("milk") 
# mydict.popitem() # ลบตัวล่าสุด