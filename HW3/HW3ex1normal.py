lenfib = int(input("Укажите длину ряда Фибоначчи: "))
n = int(input("Укажите первый интересующий вас элемент ряда: "))
m = int(input("Укажите последний интересующий вас элемент ряда:"))
n = n - 1

def fib(lenfib,n,m):
    fib = []
    fib.insert(0, 1)
    fib.insert(1, 1)
    i = 2
    while i < lenfib:
        fib.insert(i, (fib[i-1] + fib[i-2]))
        i = i + 1
    #Возвращаем ряд с n по m включительно.
    print(fib[n:m:1])

fib(lenfib,n,m)
        
