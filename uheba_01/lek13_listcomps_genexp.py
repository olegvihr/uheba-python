import pprint
import time

# List comprehension = listcoms
# Generator expressions = genexp

# [ВЫРАЖЕНИЕ/ПРЕОБРАЗОВАНИЕ for element in ИСТОЧНИК if УСЛОВИЕ]
# переменные в листкомпс недоступны извне
# читается слева направо
# для словоря обязательно указать КЛЮЧ:ЗНАЧЕНИЕ
# генератор ленивый, не выполняет действий и не занимает память пока не потребуется
# генератор проверяет источник при создании
# генератор одноразовый, если исчерпан то бросает StopIteration
# цикл for перехватывает исключение StopIteration
# используйте генэксп вместо компс, кроме случаев когда нужна длина len или индексы

text = "hello world"
words = [word.capitalize() for word in text.split()]

ints = [-1, 0, 1, -2, 3, -4, 5]
positives = [e for e in ints if e > 0]
# print(e)

squares = [e ** 2 for e in range(10) if e % 2 == 0]

scuares2 = []
for e in range(10):
    if e % 2 == 0:
        scuares2.append(e ** 2)
print(e)

letters = [letter for word in text.split() for letter in word if letter < 'l']

matrix = [list(range(x, x + 3)) for x in range(3)]

unique_letters = {letter for word in text.split() for letter in word if letter < 'o'}

alphabet = {index: letter for index, letter in
            enumerate('abcdefghijklmnopqrstuvwxyz', 1)}  # без "index: letter" будет set набор, а не словарь

# Generator expressions = genexp

positives_gen = (e for e in ints if e > 0)
# positives_gen = (e for e in range(10_000_000_000_000_000_000) if e > 0)
positives_gen = (e for e in range(10) if e > 0)


def some_source():
    # print('!!!')
    # sleep(3)
    # open db
    # read file
    # calculate
    return 1, 2, 3


def some_filter(x):
    time.sleep(1)
    return True


def some_mapping(x):
    time.sleep(1)
    return x


if __name__ == '__main__':
    print(squares)
    print(scuares2)
    print(words)
    print(positives)
    print(letters)
    print(matrix)
    pprint.pprint(matrix, indent=1, width=15)
    print(unique_letters)
    print(alphabet)
    print({value: key for key, value in alphabet.items()})  # не рекомендуется применять на практике, тут для примера
    print(positives_gen)
    print(next(positives_gen))
    for e in positives_gen:
        print(e)
    print('=============')
    # gen = (e for e in some_source())
    for e in positives_gen:
        print(e)

    # it = [some_mapping(e) for e in some_source() if some_filter(e)]
    it = (some_mapping(e) for e in some_source() if some_filter(e))
    print(next(it))
