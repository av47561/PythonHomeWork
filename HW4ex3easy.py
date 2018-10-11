import random
i = 0
sp1 = [random.randint(-1000, 1000) for _ in range (15)]
print ("sp1 = ",sp1)
sp2 = [el for el in sp1 if (el > (0) ) and (el % 3 == 0) and (el % 4 != 0)]
print ("sp2 = ",sp2)
