# yield показывает что функция = генератор
# генератор ленивый (lazy), одноразовый (eager), кидает StopIteration при исчерпании
# после выполнения yield встает на паузу


squares = (e ** 2 for e in range(0, 11, 2))

def squares2():
    print("Generator working...")
    for i in range(0, 11, 2):
        yield i ** 2

def pause():
    print("Generator working...")
    while True:
        print(a)
        yield a

a = 10
gen = pause()
print(gen)
print(next(gen))
a = 20
print(next(gen))
a = 30
print(next(gen))


# gen = squares2()
# # print(gen)
# for i in gen:
#     print(i)

