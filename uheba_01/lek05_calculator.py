# function calculator with operators + - / *

def calculator(expression):
    allowed = '+-/*'
    if not any(sign in expression for sign in allowed):
        raise ValueError(f'Invalid expression ({allowed})')
    for sign in allowed:
        if sign in expression:
            try:
                left, right = expression.split(sign)
                left, right = int(left), int(right)
                return {
                    '+': lambda a, b: a + b,
                    '-': lambda a, b: a - b,
                    '*': lambda a, b: a * b,
                    '/': lambda a, b: a / b,
                }[sign](left, right)
            except (ValueError, TypeError):
                raise ValueError("Выражение должно содержать 2 числа и один оператор")

def plus(a, b):
    """
    :param a:
    :param b:
    :return:
    """

    return a + b


if __name__ == '__main__':
    print(plus(10, 12))
