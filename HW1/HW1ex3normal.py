import math
a, b, c = map(int, input("Введите значения коэффициентов a,b,c :").split()) #Вводим значения через пробел
D = (b**2) - (4*a*c)
if D < 0:
    print("Корней нет")
elif D == 0:
    print("Значение дискриминанта D = " + str(D))
    print("Есть один корень")
    x=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    print (x)
elif D > 0:
    print("Значение дискриминанта D = " + str(D))
    print("Есть два корня")
    x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
    x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
    print(x1)
    print(x2)
