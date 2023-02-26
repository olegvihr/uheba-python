# lambda аналог def !!!
# можно писать все, что допустимо после return в def
# не выполняется до вызова ()!!
# код можно писать без лямбд

from operator import attrgetter, itemgetter


def square(x):
    return x ** 2


def is_even(x):
    return x % 2 == 0


def second(x):
    return x[1]


square2 = lambda x: x ** 2
even_odd = lambda x: 'Even' if x % 2 == 0 else 'Odd'
any_ = lambda: abracadabra  # не выполняется до вызова


class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Cat {self.name}, age is {self.age}"


if __name__ == "__main__":
    print(square(2))
    print(square2(3))
    print(even_odd(4))
    print(any_)
    abracadabra = 42
    print(any_())
    x = 2
    result = lambda n=x: n ** 2
    x = 3
    result2 = lambda n=x: n ** 2
    print(result())
    print(result2())
    ints = list(range(10))
    print(list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, ints))))
    print([i ** 2 for i in ints if i % 2 == 0])
    a_dict = {'a': 7, 'd': 2, 'c': 1, 'b': 4, 'e': 5, }  # ('a', 7)
    print(sorted(a_dict.items(), key=lambda x: x[0]))
    print(sorted(a_dict.items(), key=itemgetter(0)))  # from operator import attrgetter, itemgetter

    cats = [Cat('Tom', 2), Cat('Dymka', 3)]
    print(sorted(cats, key=lambda cat: cat.age))
    print(sorted(cats, key=attrgetter('age')))  # from operator import attrgetter, itemgetter

