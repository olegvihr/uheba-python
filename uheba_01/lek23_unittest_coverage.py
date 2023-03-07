# написать функцию calculator, которая принимает на вход строку, содержащую два целых чисела и один знак арифметического
# оператора + - / * и возвращает результат вычисления. Если не целые или нет операторов, возвращается бросать исключение
# ValueError.

def calculator(expression):
    allowed = '+-/*'
    if not any(sing in expression for sing in allowed):
        raise ValueError(f"Выражение должно содержать хотя бы один знак ({allowed})")
    for sing in allowed:
        if sing in expression:
            try:
                left, right = expression.split(sing)
                left, right = int(left), int(right)
                return {
                    '+': lambda x, y: x + y,
                    '-': lambda x, y: x - y,
                    '*': lambda x, y: x * y,
                    '/': lambda x, y: x / y,
                }[sing](left, right)
            except (ValueError, TypeError):
                raise ValueError(f"Выражение должно содержать 2 целые числа и 1 знак")


if __name__ == '__main__':
    print(calculator('2/0'))