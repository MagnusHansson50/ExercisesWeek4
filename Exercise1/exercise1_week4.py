#1a
# def foo(t):
#     print("test")
#
# foo("hej")

#1b
# def fun1(x, y):
#     return x * y
#
# print(3, 5)

#1c
# def fun1(x, y):
#     return x * y
#
# print(fun1(3, 5))

#1d
# def fun2(i):
#     return 5 * i
#
# x = 2
# y = 3
# a = fun2(fun2(x) + fun2(y))
# print(a)

#1e
# a = 5
# def fun3(a):
#     a += 1
#
# a += 2
# print(a)

#1f
# def foo(i):
#     return 2*i*i
#
# def goo(x, y):
#     return x(y)
#
# a = goo(foo, 3)
# print(a)

#1g
# def is_number(x):
#     if isinstance(x, int):
#         return True
#     elif isinstance(x, float):
#         return True
#     return False
#
# print(is_number(5.5))
# print(is_number(42))

#1h
# def average_words(strings):
#     found = []
#     for item in strings:
#         if 4 < len(item) < 8:
#             found.append(item)
#     return found
#
# print(average_words(["sup", "how's", "it", "going", "reflecting", "on", "programs", "and", "coding"]))

#1i
def find_min(numbers):
    if len(numbers) > 0:
        counter = numbers.pop(0)
        for item in numbers:
            if item < counter:
                counter = item
        print(f"The smallest item is: {counter}")
        return counter
    else:
        print("tom lista")

find_min([10, 3, -4, -11])
find_min([])
find_min([100])


