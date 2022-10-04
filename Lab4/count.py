i = 0 # initialization

# while \\\
n = int(input("Enter n: "))
while i < n : # condition
    print(i+1)
    i += 1 # update

print("-------------")

i = 0
while i < n : # condition
    i += 1 # update
    print(i)

print("-------------")

# for \\\
# range(n) => 0, 1, ..., n-1
# range(1,n) => 1, 2, ..., n-1
# range(1,n+1) => 1, 2, ..., n
for j in range(1,n+1) :
    print(j)