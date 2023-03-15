# name = 'Tom'
# age = 2
from  collections import namedtuple

Cat = namedtuple('Cat', 'name age')



def meow():
    print('Meow')