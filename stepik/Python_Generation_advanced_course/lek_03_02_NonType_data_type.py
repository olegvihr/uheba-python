class MetaSingleton(type):  # Пример на языке Python на МетаКлассах
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


var = None
print(type(var))

var = None
if var is None:  # используем оператор is, правильно
    print('None')
else:
    print('Not None')

var = None
if var == None:  # используем оператор ==, не правильно
    print('None')
else:
    print('Not None')

print(None == None)  # True

print(None == 17)  # False
print(None == 3.14)  # False
print(None == True)  # False
print(None == [1, 2, 3])  # False
print(None == 'Beegeek')  # False

print(None == 0)  # False
print(None == False)  # False
print(None == '')  # False

# Сравнивать None с другими типами данных можно только на равенство.
# print(None > 0)  # приводит к ошибке:TypeError: '>' not supported between instances of 'NoneType' and 'int' ('bool')
# print(None <= False)

# Обратите внимание, что функции, не возвращающие значений, на самом деле в Python возвращают значение None.
def print_message() :
    print('Я - Тимур,')
    print('король матана. ')

print_message()
res = print_message()  # В переменной res хранится значение None.