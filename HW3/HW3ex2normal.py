import random
lenA = int(input("Сколько элементов должно быть в списке?: "))
A = []
i = 0
li = []
print("Вводите число, затем Enter")
while i < lenA:
    A.append(float(input()))
    i = i + 1

def fsort(A):
    li = A
    print("Исходный список:" ,li)
    n = 1 
    while n < len(li):
         for i in range(len(li)-n):
              if li[i] > li[i+1]:
                   li[i],li[i+1] = li[i+1],li[i]
         n += 1
    print("Отсортированный список:" ,li)
    
fsort(A)
