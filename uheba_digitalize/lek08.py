# новое в Python 3.8

import re

from uheba_01.lek32_pattern_matching import some

hello = 'Приват, Василий!'
name = re.search(r', (.*)!', hello)
if name:
    print(name.group(1))


if (name := re.search(r', (.*)!', hello)):  # walrus - оператор присваивания
    print(name.group(1))


def some_func(x, y, /):  # строго позиционные аргументы при помощи /
    print(x, y)

some_func(1, 2)

name = 'Oleg'
print(f'{name}')
print(f'name={name}')
print(f'{name=}')  # изменение в f-стринг

from typing import TypedDict  # новые типы в typing - TypedDict
class Client(TypedDict):
    id: int
    name: str

client = Client(id=1, name='Oleg')


from importlib.metadata import version

print(version('requests'))