# объект - сущность, объединяющая данные и методы для работы с ними (состояние и поведение)
# Чертеж = класс, объект это дом
# класс - это новый тип данных, объект - его конкретный предствавитель
# у любого объекта есть id, значение и тип
# первая потребность для классов - когда не хватает встроенных типов, вторая - разное состояние
# метод - это функция котороя принадлежит классу
# dunder дандар, магическаий метод

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def meow(self):
        print(f'{self.name} says: Meow!')

# import cat

# from  cat import Cat, meow

if __name__ == '__main__':
    # tom = Cat('Tom', 2)
    # print(tom)
    # print(tom.name)
    # meow()

    # cats = [('Tom', 2), ('Angela', 3)]
    # tom = cats[0]
    # print(tom)
    # print(tom[0])


    # tom = cat
    # print(tom.name)
    # print(tom.age)
    # tom.meow()
    # cat.name = 'Angela'
    # print(tom.name)

    tom = Cat('Tom', 4)
    angela = Cat('Angela', 3)
    # print(tom is angela)
    # print(tom == angela)
    print(tom)
    print(angela)
    # print(type(tom))
    tom.meow()
    angela.meow()
    print(tom.name)
    print(tom.age)
    tom.meow()
    # Cat.meow(tom)  !!!
