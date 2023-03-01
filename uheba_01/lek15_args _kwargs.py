# позиционные аргументы всегда идут в начале
# / - все что слева - только позиционные аргументы
# *, - все что справа - только keyword аргументы
# *args собирает все позиционные аргументы в кортеж
# **kwargs собирает все keyword аргументы в словарь


a, *b, c = [1, 2, 3, 4, 5, 6]


def example(a, b, /, c, *, d):
    print(a)
    print(b)
    print(c)
    print(d)


# def my_print(a, *args):
# def my_print(*args, number=1):
def my_print(*args, **kwargs):
    print(f"Got keyword: {kwargs}")
    for arg in args:
        print(str(arg), **kwargs)


if __name__ == '__main__':
    print(f'{a=}')
    print(f'{b=}')
    print(f'{c=}')
    print(*[1, 2, 3, 4, 5, 6])
    print(1, 2, 3, 4, 5, 6)
    # example(c=1, b=2, a=3)
    # example(1, 2, 3)
    example(1, 2, c=3, d=True)
    # my_print(1, 2, 3, 4, 5, sep=':', end='-', number=100)
    print(1, 2, **{'sep': ':', 'end': '-'})
    print(1, 2, sep=':', end='-')
