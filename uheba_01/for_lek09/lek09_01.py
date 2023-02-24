print(f'start module: {__name__}')
def calc(a, b):
    print("calc in 01")
    return a + b

if __name__ == "__main__":
    print("abracadabra")
    print(calc(1, 2))
