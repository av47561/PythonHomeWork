import os
a = input(str('Нажмите нужную клавишу для действия: \n 1-Перейти в папку \n 2-Просмотреть содержимое текущей папки \n 3-Удалить папку \n 4-Создать папку \n Ваш выбор: ' ))
print(a)

def CD():
    path = input(str('Введите путь к нужной директории: '))
    try:
        os.chdir(path)
        print('Успешный переход в: ', os.getcwd())
    except FileNotFoundError:
        print('Такой директории нет')

def CheckDir():
    print('Содержимое текущей директории : \n {}'.format(os.listdir()))

def Delete():
    ForDel = input(str('Имя папки на удаление: '))
    try:
        os.rmdir(ForDel)
        print('Успешное удаление папки: ', ForDel)
    except FileNotFoundError:
        print('Не удалось удалить, проверьте правильность имени каталога.')
def CreateDir():
    ForCreate = input(str('Имя папки для создания: '))
    try:
        os.mkdir(ForCreate)
        print('Успешное создание папки: ', ForCreate)
    except FileExistsError:
        print('Не удалось создать папку, она уже существует.')

if a == ('1'):
    CD()
elif a == ('2'):
    CheckDir()
elif a == ('3'):
    Delete()
elif a == ('4'):
    CreateDir()
