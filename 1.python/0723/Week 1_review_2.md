# Week 1_review_2

## 1. List 합

list의 모든 요소들의 합을 구하는 list_sum 함수를 sum함수를 사용하지 않고 작성하시오.

출력값: 10

```python
def list_sum(n):
    total=0
    for number in n:
        total += number
    return total

print(list_sum([1, 2, 3, 4]))
```



## 2. List 합 - Dictionary

모든 dictionary의 'age' 에 해당하는 value 들의 합을 반환하는 dict_sum 함수를 sum함수를 사용하지 않고 작성하시오.

출력값: 25

```python
def dict_sum(list):
    answer = 0
    for info in list:
        answer += info['age']
    return answer

print(dict_sum([{'name': 'kim', 'age': 15}, {'name': 'park', 'age': 10}]))
```



## 3. 2개의 List로 이루어진 합

 2중 list의 모든 요소들의 합을 반환하는 list_sum 함수를 sum함수를 사용하지 않고 작성하시오

출력값: 55

```python
def list_sum(list):
    answer = 0
    for number_list in list:
        for number in number_list:
            answer += number
    return answer

print(list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]]))
```



## 4. 아스키 코드_1

 각 정수에 대응되는 아스키 문자를 이어붙인 문자열을 구하는 chr_word 함수를 작성하시오.

출력값: 'Alex'

```python
def chr_word(list):
    answer = ''
    for number in list:
        answer += chr(number)
    return f'\'{answer}\''
    
print(chr_word([65, 108, 101, 120]))
```



## 5. 아스키 코드_2

각 문자에 대응되는 아스키 숫자들의 합을 구하는 ord_number 함수를 작성하시오.

```python
def ord_number(word):
    answer = 0
    for char in word:
        answer += ord(char)
    return answer

print(ord_number('Alex'))
```



## 6. 큰 값의 이름

 각 문자에 대응되는 아스키 숫자들의 합을 비교하 여 더 큰 합을 가진 문자열을 구하는 bigger_name 함수를 작성하시오.

출력값: michael

```python
def bigger_name(a, b):
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

print(bigger_name('michael', 'alex'))
```



