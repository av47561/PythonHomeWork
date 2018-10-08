lenA = int(input("Введите желаемую размерность первого списка: "))
A_list = []
print("Элементы списка 1:")
for i in range(lenA):
    new_A_element = int(input())
    A_list.append(new_A_element)
print(A_list)
lenB = int(input("Введите желаемую размерность второго списка: "))
B_list = []
print("Элементы 2 списка:")
for i in range(lenB):
    new_B_element = int(input())
    B_list.append(new_B_element)
print(B_list)
print("Совпадающие элементы: ")
C_list = (set(A_list) & set(B_list))
print(C_list)
A_list = (set(A_list) - set(C_list))
print("Обновленный первый список: ")
print(A_list)
