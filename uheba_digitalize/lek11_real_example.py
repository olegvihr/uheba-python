import random
from collections import namedtuple

Car = namedtuple('Car', ['color', 'brand'])

class Garage:
    def __init__(self):
        self._cars = [
            Car(color='brown', brand='Porsche'),
            Car(color='black', brand='BMW'),
            Car(color='silver', brand='Mersedes'),
        ]

    def __len__(self):
        return len(self._cars)

    def __getitem__(self, position):
        return self._cars[position]


if __name__ == '__main__':
    garage = Garage()
    print(len(garage))
    print(garage[0])
    print(garage[-1])
    print(garage[1:2])
    print(random.choice(garage))
    for car in garage:
        print(car.brand)