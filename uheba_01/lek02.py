# про отладку скрипта

def get(value):
    if value > 0:
        return 'Positive'
    elif value < 0:
        return 'Negative'
    return 'Zero'


if __name__ == '__main__':
    k = 0
    for i in range(10):
        k += 1

    value = int(input())
    print(get(value).upper())
