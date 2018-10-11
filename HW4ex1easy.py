import random
i = 0
sp1 = [random.randint(-20, 20) for _ in range (5)]
print ("sp1 = ", sp1)
sp2 = [sp1[i] * sp1[i] for i in range (5)]
print ("sp2 = ", sp2)
