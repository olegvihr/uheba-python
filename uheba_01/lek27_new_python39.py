from typing import Any, Optional, Union

def to_str(integers: list[int]) -> list[str]:
# def to_str(flag: Optional[int] = None) -> list[str]:
    return [str(elem) for elem in integers]


if __name__ == '__main__':
    first = {1:1, 2:2, 3:3, 4:4}
    second = {5:5, 6:6, 7:7, 8:8}
    third = {9:9, 10:10, 11:11, 8:999}
    first.update(second)
    # first |= second
    # first = first | second

    # print({**first, **second})
    print(first | second | third)

    # # print(to_str([1, 2, 3]))
    # text = 'text'
    # # text = text.rstrip('At')
    # text = text.removesuffix('xt')
    # print(text)