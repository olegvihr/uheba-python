# Closures Замыкание
# замыкание это внутренняя функция, которая возвращается из внешней и использует переменные из внешнего скоупа
# каждое замыкание хранит свое состояние, они не пересекаются
# хранит состояние(данные), предоставляет интерфейс для работы с ними, "скрывает" данные, помогает избегать  global

def names():
    all_names = []

    def inner(name: str) -> str:
        all_names.append(name)
        return all_names

    return inner

# def average():
#     values = []
#     def inner(value: int) -> float:
#         values.append(value)
#         return sum(values) / len(values)
#     return inner

def count():
    count = 0

    def inner(value: int) -> int:
        nonlocal count
        count += value
        return count

    return inner

def pow_(base):
    # def inner(value):
        # return value ** base
    return lambda value: value**base
    # return inner


if __name__ == '__main__':
    p = pow_(2)
    print(p(5))

    # boys = names()
    # boys('Oleg')
    # print(boys.__closure__[0].cell_contents)

    # pow__ = pow_(2)
    # pow_2 = pow_(3)
    # print(pow__(5))
    # print(pow__(6))
    # print(pow__(7))
    # print(pow_2(5))
    # print(pow_2(6))
    # print(pow_2(7))

    # count = count()
    # print(count(1))
    # print(count(1))
    # print(count(1))
    # print(count(-3))

    # avg = average()
    # print(avg(10))
    # print(avg(20))
    # print(avg(30))

    # boys = names()
    # girls = names()
    # print(boys('Pesho'))
    # print(boys('Dima'))
    # print(boys('Oleg'))
    # print(girls('Katya'))
    # print(girls('Olya'))
    # print(girls('Nika'))