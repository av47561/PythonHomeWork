Nbileta = input("Введите ваш шестизначный номер билета: ")

def happy(Nbileta):
    str(Nbileta)
    first = Nbileta[:3]
    second = Nbileta[3:]
    firstSum = (sum(map(int,str(first))))
    secondSum = (sum(map(int,str(second))))
    if firstSum == secondSum:
        print("У вас счастливый билет!")
    else:
        print("Бесполезный билет :(")
            
happy(Nbileta)
