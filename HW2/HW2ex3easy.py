lenA = int(input("Укажите число элементов списка: "))
A = []
B = []
i = 0
print("Введите э-ты списка: ")
while i < lenA:
    A.insert(i, (int(input())))
    i = i + 1
print("Полученный список:" ,(A))
i = 0
while i < lenA:
    if A[i] % 2 == 0:
        B.append(A[i] / 4)
        i = i + 1
    else:
        B.append(A[i] * 2)
        i = i + 1
print("Новый список:" ,(B))
