class First:
    def __init__(self):
        self._login = 'login'
        self.__pasword = 'paswords'


class Second(First):
    def __init__(self):
        super().__init__()
        self._login = 'sfsfs'
        self.__pasword = 'MY_pass'


# class MyList(list):
#     def __str__(self):
#         return super().__str__().replace(',', ',\n')

# class Empty:
#     pass

# class Engine:
#     pass
#
# class Wheel:
#     pass
#
# class Car:
#     def __init__(self):
#         self.engine = Engine()
#         self.wheels = [Wheel()] * 4
#
#     def start(self):
#         self.engine.start()


if __name__ == '__main__':
    first = First()
    second = Second()
    print(dir(second))
    print(second._login)
    print(second._Second__pasword)
    print(second._First__pasword)
    # print(dir(Empty()))
    # print([1, 2, 3])
    # my_list = MyList([1, 2, 3])
    # print(my_list)
    # print(my_list[1])
    # my_list.extend([4, 5])
    # print(my_list)
    # print(dir(my_list))
