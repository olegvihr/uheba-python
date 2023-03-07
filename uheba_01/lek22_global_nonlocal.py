# global и nonlocal нужны только для изменения значений
# global может создать переменную, nonlocal не может создать переменную!
# nonlocal ищет только во внешних скоупах, но не в глобальном
# не используйте global и nonlocal


couter = 100


def increment(value):
    return value + 1

    # couter = 0
    #
    # def inner1():
    #     def inner():
    #         nonlocal couter
    #         couter += 1
    #         print(couter)
    #
    #     inner()
    #
    # inner1()
    #
    # # global couter
    # # # couter += 1
    # # couter = 100
    # # print(couter)


if __name__ == '__main__':
    # increment()
    # print(couter)
    couter = increment(couter)
    print(couter)