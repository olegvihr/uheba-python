from typing import List, Union, Optional

def calc(x: Union[int, float], y: Union[int, float]) -> Union[int, float]:
    return x + y

def to_int(a_list: List[str])->List[int]:
    return [int(i) for i in a_list]


if __name__ == '__main__':
    # print(calc(2, 2))
    # calc(2, 3).upper()
    # print(calc('2', 3))
    # print(to_int([1, 2, 3, 4, 5, 6]))
    # to_int(['1', '2', '3', '4', '5', '6'])
    print(calc(1.2, 2.3))