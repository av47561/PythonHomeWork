import collections
lenA = int(input("Укажите число элементов списка: "))
A = []
C = []
i = 0
print("Введите э-ты списка: ")
while i < lenA:
    A.insert(i, (int(input())))
    i = i + 1
print("Полученный список:" ,(A))
B = list(set(A))
print("Неповторяющиеся элементы исходного списка:" ,(B))
for i in A:
   if A.count(i) == 1:
      C.append(i)
print("Элементы исходного списка, которые не имеют повторений:" ,(C))
