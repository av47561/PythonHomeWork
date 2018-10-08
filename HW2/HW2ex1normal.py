import math
lenA = int(input("Укажите число элементов списка: "))
A = []
B = []
i = 0
print("Введите э-ты списка: ")
while i < lenA:
    A.insert(i, (int(input())))
    i = i + 1
print("Полученный список:" ,(A))
for element in A:
    if element < 0:
        continue
    elif element > 0 and (math.sqrt(element) % 1 == 0):
        B.append(math.sqrt(element))
print("Новый список:" ,(B))
