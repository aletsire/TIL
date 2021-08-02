def add(*args):
    list_1 =[]
    for arg in args:
        list_1 += [arg]
    return list_1

print(add(2, 3, 4, 5, 6))


def get_numbers(a, *args):
    return a,args

print(get_numbers(1))
print(get_numbers(1,2,3))


# # 언패킹
x = [1, 2, 3]
print(get_numbers(x))
print(get_numbers(*x))
print(get_numbers(*[1, 2, 3]))


