blessings = []

while True:
   bless = input('What kind of blessing do you want? ')
   n = len(bless)
   if n > 0:
       blessings.append(bless)
   else:
       break

print('You are blessed with')
print(blessings)