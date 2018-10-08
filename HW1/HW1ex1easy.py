import random
a = random.randint(-9999999,9999999)
print (a)
a = str(a)
i = 0
while i != len(a):
    if (a[i]) == "-":
       i = i + 1        
    else:
        print(a[i])    
        i = i + 1
