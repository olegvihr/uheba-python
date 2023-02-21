# убираем коментарий, когда нужно произвести отладку скрипта

# __package__ = 'uheba_01.for_lek03.for2_lek03'

from .lek03 import multi

def calc(a,b):
    multi('=',10)
    print(f'a+b={a+b}')

# if __name__ == '__main__':
#     calc(1,2)