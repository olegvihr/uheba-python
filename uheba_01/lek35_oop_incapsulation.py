# Инкапсуляция заключается в сборе в одно место (класс) данных и методов для работы с ними И представлении пользователю
# публичного интерфейса (API)
# _ - (protected) знак того, что этот атрибут не предназначен для использования. Работа объекта не гарантируется, при
# использовании таких атрибутов
# __ - (private) под капотом преобразуется в object._Class__attribute (только для случаев когда начинается с __) Name Mangling

# Публичный API(интерфейс) - это контракт, все методы будут работать, внутренняя же реализация не гарантируется.
# Совет - делать одно _ для внутренних атрибутов и реализаций, не перебарщивать с __ и сеттерами/геттерами

# import collections
#
# text = collections
# print(dir(text))
# print([e for e in dir(text) if not e.startswith('_')])

class Person:
    def __init__(self, first_name, last_name, age):
        self.list = [first_name, last_name, age]
        # self._first_name = first_name
        # self._last_name = last_name
        # self.__age = age
        # self.__one__ = 1

    def set_age(self, age):
        if age < 1 or age > 120:
            raise ValueError("Age must be between 1 and 120")
        self.list[2] = age

    def describe(self):
        print(f' I am {self.list[0]} {self.list[1]}, Im {self.list[2]} years old!')


if __name__ == '__main__':
    ivan = Person('Ivan', 'Ivanov', 20)
    # ivan._age = 1000
    # ivan.age = 1000
    # ivan.set_age(1200)
    ivan.describe()
    # print(ivan.__one__)
    # print(ivan._age)
    # print(dir(ivan))
    # print(ivan._Person__age)
