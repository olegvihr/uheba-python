# 1) Именование! Называем вещи своими именами, коллекции во множественном числе, функции -что делают
# 2) Всегда используем f-строки, НИКОГДА не складываем строки
# 3) не делаем то, что происходит по-умолчанию (str(input())
# 4) используем листкомпс и генэксп только если есть преобразование И/ИЛИ фильтрация
# 5) предпочитаем листкомпс и генэксп map/filter
# 6) использования вместо while True других конструкций для вечного цикла
# 7) использование квадратных скобок для list compr без необходимости
# 8) использование индексов в цикле for #пример: for i in range(len(list))
# 9) использование функции len при проверке наличия элементов в коллекции
# 10) использование флага в цикле без необходимости
# 11) в блоке except замалчивание ошибки и неиспользование конкретного исключения

# 1)
value1 = 1
text = 'text'
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, ]
student = ["Oleg Vikharev", 25]


def get_positives(integers: list) -> list:
    return [e for e in integers if e > 0]


# 2)
first = 'Hello'
second = 'World'
print(first + second)  # не правильно так скадывть строки
print(f'{first}' + f'{second}')  # не правильно так скадывть строки
print(f'{first} {second}')  # правильно скадываем строки

# 3)
# value = str(input('Введите значение: '))  # не правильно
value2 = input('Введите значение: ')  # правильно
print(value2)
print(type(value2))
a_dikt = {1: 1, 2: 2}
# value3 = a_dikt.get(1, None) # не правильно
value3 = a_dikt.get(3)  # правильно
print(value3)

# 4)
integers = [e for e in range(10)]  # не правильно
print(integers)
integers = [e ** 2 for e in range(10) if e % 2 == 0]  # правильно
print(integers)
integers = list(range(10))  # правильно
print(integers)

# 5)
integers = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, range(10))))  # не правильно
print(integers)
integers = (e ** 2 for e in range(10) if e % 2 == 0)  # правильно
print(list(integers))

# 6)
while 1 == 1:  # не правильно
    break
while True:  # правильно
    break

# 7)
print(sum([e for e in range(10) if e % 2 == 0]))  # не правильно
print(sum(e for e in range(10) if e % 2 == 0))  # правильно, т.к. не занимает память
print(''.join(str(e) for e in range(10) if e % 2 == 0))  # правильно, если список не нужен, используем гэнэксп

# 8,9)
integers = [1, 2, 3, 4, 5, 6, -7, ]
for integer in range(len(integers)):  # не правильно, не используем range(len(list))
    print(integers[integer])  #

for integer in integers:
    print(integer)

for index, integer in enumerate(integers, 1):  # (1, 1), если нужен индекс, то используем enumerate
    print(f'{index}-{integer}')

if len(integers) > 0:
    pass
if integers:  # вернет True, если список не пустой
    pass

# 10)
flag = True  # не правильно, т.к. слишком громоздкая конструкция
for integer in integers:
    if integer < 0:
        flag = False
        break
print(flag)
print(all(e > 0 for e in integers))  # правильно, необходимо использовать встроенные операторы

# 11)
integers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
            30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 5]
try:  # не правильно, т.к. не должно быть пустым
    int('a')
except:
    pass

try:  # правильно
    int('a')
except Exception as err:  # ловим ошибку, пишем информацию в ветке except
    print((f'{err}, {err.args}'))
    print('Error')
