# list 합 구하기
def list_sum(n):
    total = 0
    for i in n:
        total += i
    return total
print(list_sum([1, 2, 3, 4, 5]))


# Dictionary list 합 구하기
def dict_list_sum(n):
    total = 0
    for i in n:
        total += i['age']
    return total
print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))



# 2차원 list 합 구하기
def all_list_sum(n):
    total = 0
    for i in n:
        for j in i:
            total += j
    return total
print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))


