from collections import OrderedDict, ChainMap, Counter, defaultdict, deque, namedtuple
import csv

# OrderedDict нужен для действия со словарем где необходим порядок элементов, например: сравнение с учетом порядка,
# перестановки элементов с сохранением порядка. Платим памятью!

# ChainMap нужен для логического объядинения словарей для поиска информации, но при изменениях меняется первый словарь

# Counter нужен для считывания количества элементов в последовательности, работает только с помощью hashable.

# defaultdict нужен для создавания словаря со значениями по умолчанию. Значение подставляется при обращении к
# несуществующему ключу.

# deque потокобезопасна, быстро оперирует с обееми сторонами

# namedtuple предназначен для создания структуры данных, нечто среднее между стандартными типами и самописным классом,
# неизменяемый, позволяет обращаться по имени атрибута, позволяет использовать индексы.


Point = namedtuple('Point', 'x y')
with open('points.csv') as file:
    for line in csv.reader(file):
        point = Point._make(line)
        print(point)

# # tom = ('Tom', 4, 'yellow')
#
# Cat = namedtuple('Cat', 'name age color')
# tom = Cat('Tom', 4, 'yellow')
# print(tom)
# print(tom[0])
# print(tom.name)
# print(tom.age)
#


# for line in a_deque:
#     print(line.rstrip())


# a_deque = deque([1, 2, 3], maxlen=3)
# print(a_deque)
# a_deque.append(4)
# print(a_deque)

# a_deque = deque()
# a_deque.append(1)
# print(a_deque)
# a_deque.appendleft(2)
# print(a_deque)


# counter = Counter('Hello')
# print(counter)
# # counter.update('World')
# print(counter)
# print(counter.most_common(3))

# a_dict = defaultdict(int)
# # print(int())
# for char in 'Hello':
#     a_dict[char] += 1
# print(sorted(a_dict.items(), key=lambda x: x[1], reverse=True))

# a_dict = defaultdict(list)
# for char in 'Hello':
#     a_dict[char].append(char)
#
# print(a_dict)


# first = {1: 1, 2: 2, 3: 3}
# second = {4: 4, 5: 5, 6: 6}
#
# chain = ChainMap(first, second)
#
# print(chain)
# print(5 in chain)
# first[1] = 100
# print(chain)
# chain[5]=200
# print(chain)

# order1 = OrderedDict(first)
# order2 = OrderedDict(second)
#
# print(order1 == order2)
#
# print(first == second)
# # print(first.popitem())
# # print(order1.popitem(last=False))
# # order1.move_to_end(1)
# order1.move_to_end(3, last=False)
# print(order1)
