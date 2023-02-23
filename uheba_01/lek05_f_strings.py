import datetime

a = 'Hello'
b = 'World'

if __name__ == '__main__':
    print(a + ' ' + b)
    print(a, b)
    print(f'{a}, {b}!')
    resault = 1214
    c = f'{resault = }'
    print(c)
    print(f'{resault:b}')
    print(f'{resault:x}')
    pi = 3.141592653589793
    pii = 3
    print(f'{pi:.3f}')
    print(f'{resault:06}')
    print(f'{resault:06x}')
    print(f'{resault:06b}')
    print(f'{resault:^12}')
    print(f'{resault:<12}')
    print(f'{resault:>12}')
    print(f'{resault:=^12}')
    print(f'{resault:0<12}')
    print(f'{resault:0>12}')
    print(f'{resault:,}')
    print(f'Resault = {min(resault, pii)}')
    today = datetime.datetime.now()
    print(today)
    print(f'{today:%Y-%m-%d  %H:%M:%S}')
    real = 86
    full = 100
    print(f'{real / full:.2%}')
