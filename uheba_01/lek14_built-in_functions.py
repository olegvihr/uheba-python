a_list = [0, 0, 1, 0, True, 'sd']
a_list2 = ['as', 'a', 'sdfsd', 'sdgsdgsdf']


# if any(a_list):
#     print(list(filter(None, a_list)))
#     print([e for e in a_list if e])

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f'{self.name=} is {self.age=} years old'


if __name__ == '__main__':
    # print(all(a_list))
    # print(any(a_list))
    # print(all(a_list2))
    # print(bool(a_list2))
    cats = [Cat('Tom', 2), Cat('Dymka', 3), Cat('Jerry', 4)]
    # print(max(a_list2, key=len))
    # print(max(cats, key=lambda cat: cat.age))
    # for cat in iter(cats):
    # for line in iter(input, 'end'):
    #     print(line.upper())
    ints = [int(x) for x in iter(input, '')]
    print(ints)