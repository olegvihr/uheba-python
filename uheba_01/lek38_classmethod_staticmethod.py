# LEGB-rule действует для атрибутов без приставок (self)
# для self атрибутов поиск идет сначала в объекте, потом в классе, затем у предков OCP(object-class-parent)
# если через self попытаться поменять неизменяемый атрибут (строка), то будет создана локальная копия
# если менять через self изменяемый атрибут, то он изменится для всех объектов класса
# cls - это ссылка на класс (не объект!), питон передает его под капотом
# @classmethod используется для работы с атрибутами класса и с другими методами класса
# @staticmethod не получает ссылок под капотом, это просто функция связанная контекстом с классом
# cls = BlueCat


class BlueCat:
    breed = 'Russian Blue'
    names = []
    count = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        BlueCat.increment_count()

    def meow(self):
        print(f'{self.name} of {self.breed} says: Meow!')

    @classmethod
    def increment_count(cls):
        cls.count += 1

    @classmethod
    def make_cat(cls, name):
        if name == 'Tom':
            return cls('Tom', 2)
        elif name == 'Angela':
            return cls('Angela', 1)
        return cls('Ginger', 2)

    @staticmethod
    def get_human_age(age):
        return age * 8


if __name__ == '__main__':
    tom = BlueCat.make_cat('Tom')
    angela = BlueCat.make_cat('Angela')
    tom.meow()
    angela.meow()
    print(BlueCat.get_human_age(angela.age))