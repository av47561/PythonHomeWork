import random
lenA = int(input("Укажите число элементов списка: "))
A = []
i = 0
while i < lenA:
    A.insert(i, (random.randint(-100, 100)))
    i = i + 1
print(A)
