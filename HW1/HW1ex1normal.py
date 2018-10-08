import random
a = random.randint(0,9999999)
print ("Исходное число")
print (a)
m = max([int(i) for i in str(a)])
print ("Наибольшая цифра в числе")
print (m)

