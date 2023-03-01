
# my_list = [[0], [1, 2], [3, 4, 5]]

# Способ 1. Создадим пустой список, потом n раз добавим в него новый элемент – список длины m, составленный из нулей:
n, m = int(input()), int(input())  # считываем значения n и m
my_list = []

for _ in range(n):
    my_list.append([0] * m)

print(my_list)

# Способ 2. Сначала создадим список из n элементов (для начала просто из n нулей). Затем сделаем каждый элемент списка ссылкой на другой список из m элементов, заполненный нулями:

# n, m = int(input()), int(input())  # считываем значения n и m
my_list = [0] * n

for i in range(n):
    my_list[i] = [0] * m

print(my_list)

# Способ 3. Можно использовать генератор списка: создадим список из n элементов, каждый из которых будет списком, состоящих из m нулей:

# n, m = int(input()), int(input())  # считываем значения n и m

my_list = [[0] * m for _ in range(n)]

print(my_list)

# Обратите внимание, что очевидное решение, использующее операцию умножения списка на число (операция повторения) оказывается неверным:

# n, m = int(input()), int(input())    # считываем значения n и m

my_list = [[0] * m] * n

print(my_list)
# В этом легко убедиться, если присвоить элементу my_list[0][0] любое значение, например, 17, а затем вывести список на печать:
# n, m = int(input()), int(input())

my_list = [[0] * m] * n
my_list[0][0] = 17

print(my_list)
""" Вложенный список нельзя создать при помощи операции повторения (умножения списка на число). Для корректного
создания вложенного списка мы используем способы 1- 3, отдавая предпочтение способу 3
"""

# n = 4                                          # количество строк (элементов)
# my_list = []

# for _ in range(n):
#     elem = [int(i) for i in input().split()]   # создаем список из элементов строки
#     my_list.append(elem)
#
# n = 4
# my_list = []
#
# for _ in range(n):
#     elem = [int(i) for i in input().split()]  # создает одномерный (!) список, а не вложенный.
#     my_list.extend(elem)

my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(my_list[0][0])
print(my_list[1][2])
print(my_list[2][1])

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[i][j], end=' ')   # используем необязательный параметр end
    print()                             # перенос на новую строку

for row in my_list:
    for elem in row:
        print(elem, end=' ')
    print()

for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        print(my_list[j][i], end=' ')    # выводим my_list[j][i] вместо my_list[i][j]
    print()

# Используем вложенный цикл для подсчета суммы всех чисел в списке:

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for i in range(len(my_list)):
    for j in range(len(my_list[i])):
        total += my_list[i][j]
print(total)

# Или то же самое с циклом не по индексу, а по значениям:

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:
    for elem in row:
        total += elem
print(total)

my_list = [[1, 9, 8, 7, 4], [7, 3, 4], [2, 1]]

total = 0
for row in my_list:      # в один цикл
    total += sum(row)
print(total)

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    maximum = max(row)
    minimum = min(row)

print(maximum + minimum)

my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]

maximum = my_list[0][0]
minimum = my_list[0][0]

for row in my_list:
    if max(row) > maximum:
        maximum = max(row)
    if min(row) < minimum:
        minimum = min(row)

print(maximum + minimum)