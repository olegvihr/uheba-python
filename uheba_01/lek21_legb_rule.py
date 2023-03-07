# LEGB - rule
# L - local
# E - enclosed
# G - global
# B - builtins

# import builtins

# builtins.scope = 'builtins'

scope = 'global'
# max = 10

def outer():
    scope = 'enclosed'

    def inner():
        scope = 'local'
        print(scope)
        print(max([1, 2, 3, 4, 5]))

    inner()


if __name__ == '__main__':
    outer()
