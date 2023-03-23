# from lek41_singleton_pattern import Monostate
from lek41_module_two import two, data


def one():
    # return Monostate().data *100
    return data * 100


if __name__ == '__main__':
    result = one() + two()
    print(result)
