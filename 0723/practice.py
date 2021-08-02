#1 세로로 출력하기
def list_sum(n):
    total=0
    for number in n:
        total += number
    return total

print(list_sum([1, 2, 3, 4]))

#2
def dict_list_sum(list):
    answer = 0
    for info in list:
        answer += info['age']
    return answer

print(dict_list_sum([{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]))

#3
def all_list_sum(list):
    answer = 0
    for number_list in list:
        for number in number_list:
            answer += number
    return answer

print(all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))

#4
def get_asc_word(list):
    answer = ''
    for number in list:
        answer += chr(number)
    return f'\'{answer}\''
    
print(get_secret_word([65, 108, 101, 120]))

#5
def get_asc_number(word):
    answer = 0
    for char in word:
        answer += ord(char)
    return answer

print(get_secret_number('Alex'))

#6
def get_best_name(a, b):
    val1 = 0
    val2 = 0 
    for chr1 in a:
        val1 += ord(chr1)
    for chr2 in b:
        val2 += ord(chr2)
    if val1 > val2:
        return a
    else:
        return b

print(get_best_name('michael', 'alex'))


