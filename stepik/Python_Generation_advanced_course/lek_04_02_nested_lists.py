'''
Примечание 1.
Независимо от вложенности списков, нам нужно помнить по возможности все списочные методы:

метод append() добавляет новый элемент в конец списка.
метод extend() расширяет один список другим списком.

метод insert() вставляет значение в список в заданной позиции.

метод index() возвращает индекс первого элемента, значение которого равняется переданному в метод значению.

метод remove() удаляет первый элемент, значение которого равняется переданному в метод значению.

метод pop() удаляет элемент по указанному индексу и возвращает его.

метод count() возвращает количество элементов в списке, значения которых равны переданному в метод значению.

метод reverse() инвертирует порядок следования значений в списке, то есть меняет его на противоположный.

метод copy() создает поверхностную копию списка.

метод clear() удаляет все элементы из списка.

оператор del позволяет удалять элементы списка по определенному индексу.

Примечание 2. Методы строк, работающие со списками:

метод split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных символов, символ табуляции (\t) или символ новой строки (\n).
метод join() собирает строку из элементов списка, используя в качестве разделителя строку, к которой применяется метод.
'''

numbers = [10, 3]
constants = [3.1415, 2.71828, 1.1415]
countries = ['Russia', 'Armenia', 'Argentina']
flags = [True, False]
info = ['Timur', 1992, 72.5]

my_list = [[0], [1, 2], [3, 4, 5]]

print(my_list)
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(len(my_list))

my_list = ['Python', [10, 20, 30], ['Beegeek', 'Stepik']]

print(my_list[0])
print(my_list[1])
print(my_list[2])

print(my_list[0][2])  # индексирование строки 'Python'
print(my_list[1][1])  # индексирование списка [10, 20, 30]
print(my_list[2][-1])  # индексирование списка ['Beegeek', 'Stepik!']
print(my_list[2][-1][-1])  # индексирование строки 'Stepik!'
# print(my_list[3])          # у списка my_list индексы от 0 до 2  ошибка: IndexError: index out of range

my_list = [[0], [1, 2], [3, 4, 5], [], [10, 20, 30]]

print(len(my_list))

total = 0

for li in my_list:
    total += len(li)

print(total)

list1 = [1, 7, 12, 0, 9, 100]
list2 = [1, 7, 90]
list3 = [1, 10]

print(min(list1, list2, list3))
print(max(list1, list2, list3))

list1 = [[1, 7, 12, 0, 9, 100], [1, 7, 90], [1, 10]]
list2 = [['a', 'b'], ['a'], ['d', 'p', 'q']]

print(min(list1))
print(max(list1))
print(min(list2))
print(max(list2))

# my_list = [[1, 7, 12, 0, 9, 100], ['a', 'b']]
# элементы вложенных списков в этой ситуации должны быть сравнимы, ошибка: TypeError: '<' not supported between instances of 'str' and 'int'

print(min(my_list))
print(max(my_list))
list1 = [[0, [9, 2]], [1, [4, 6, 3], [5, 2, 3], 8, 3]]
print(list1[1][2][1])