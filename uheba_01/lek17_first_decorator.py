# функция - полноправный объект
# внутренняя функция может захватывать переменные из внешней

# def exemple(a):
#     # print(f"{func.__name__}")
#     def inner(b):
#         print(a+b)
#
#     inner(3)

def logger(func):
    def wrapper(*args):
        print(f"{func.__name__} started")
        result = func(*args)
        print(f"{func.__name__} finished")
        return result

    return wrapper


@logger
def summ(a, b):  # в этот момент summ=wraper
    return a + b


if __name__ == '__main__':
    # function = summ
    # print(summ)
    # print(function)
    # exemple(2)
    # function = logger(summ)
    # print(function(2, 3))

    # print((logger(summ)(2, 3)))
    # summ = logger(summ)
    # print(summ(2, 3))
    print(summ(2, 3))
