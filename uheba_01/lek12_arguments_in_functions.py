from time import time, sleep


def print_n_times(value: str, n: int = 4):
    for _ in range(n):
        print(value)


def some_function():
    print("some_function called")
    return 1


# def calc(time_=[]):  # не правильно, т.к. [] имеет изменяемый тип
def calc(time_=None):  # правильно
    if time_ is None:
        time_= []
    time_.append(1)
    return time_


if __name__ == "__main__":
    print_n_times("Hello")
    print_n_times("World", n=2)
    print(1, end=',')
    print(1)
    print(calc())
    print(calc())
    sleep(2)
    print(calc())
