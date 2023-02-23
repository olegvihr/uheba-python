# True(1), False(0)
answers = ['Negative', 'Positive']
x = 1
print(answers[x > 0])
falsy = [False, 0, 0.0, '', None, [], {}, set(), tuple(), range(0)]
for e in falsy:
    print(bool(e))


class Cat:
    def meow(self):
        print('meow')


cat = Cat()
print(bool(cat))
x, y = 1, 1
if x and y:
    pass
word = 'Yes'
if word in ('YES', 'Yes', 'yes'):
    print('YES')
else:
    print('NO')


def check(x) -> bool:
    print(f'{x}>0 is {bool}')
    return x > 0


if check(1) and check(1) and check(2) and check(3) and check(4) and check(5) and check(6):
    print('all good')

if check(-1) or check(-1) or check(-1) or check(3) or check(4) or check(5) or check(6):
    print('all good')


def is_even(x) -> bool:
    return x % 2 == 0


print(is_even(2))
