num1 = 3 * True - (True + False)
num2 = (True + True + False) ** 3 + 5
print(num1 + num2)

a = 6
b = 10
print(not a == 10 and b == 10)

a = 6
b = 10
print(not (not a == 10 or not b == 10))

numbers = [-6, -8, 0, 1, 3, 8, -7, 12, 17, 24, 25, 3, 5, 1]
res = 0
for num in numbers:
    res += (num % 2 == 1) and (num > 1)
print(res)


def is_even(num):
    return num % 2 == 0


print(is_even(8))
print(is_even(7))

print(isinstance(3, int))
print(isinstance(3.5, float))
print(isinstance('Beegeek', str))
print(isinstance([1, 2, 3], list))
print(isinstance(True, bool))

print(type(3))
print(type(3.5))
print(type('Beegeek'))
print(type([1, 2, 3]))
print(type(True))
