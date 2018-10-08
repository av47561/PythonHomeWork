#Задача решена на мой взгляд "топорным методом", если возможно,
#хотелось бы узнать как заменить 0f,1f,2f значениями вводимой переменной,
#у меня к сожалению не получилось.

a = float(input("Введите десятичное число: "))
count = int(input("До скольки знаков округлить число?: "))

def okruglenie(a,count):
    if count == 0:
        print("%.0f" % a)
    if count == 1:
        print("%.1f" % a)
    elif count == 2:
        print("%.2f" % a)
    if count == 3:
        print("%.3f" % a)
    if count == 4:
        print("%.4f" % a)
    if count == 5:
        print("%.5f" % a)
    if count == 6:
        print("%.6f" % a)
    if count == 7:
        print("%.7f" % a)
    if count == 8:
        print("%.8f" % a)
    if count == 9:
        print("%.9f" % a)
    if count == 10:
        print("%.10f" % a)

okruglenie(a,count)
    
