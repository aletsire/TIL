# Week 1_review_4

## 1. 모래성 쌓기

함수의 인자

1. 쌓아야 할 높이
2. 낮 시간 동안 쌓는 높이
3. 밤 시간 동안 무너지는 높이

```python
def castle(height, day, night):
    count = 0
    while True:
        height = height - day
        count += 1
        if height < 0:
            return count
        else:
            height = height + night
```



## 2. 자리수 더하기

각 자릿수의 합을 계산하여 출력하시오.

```python
def sum_all(n):
    total = 0
    while True:
        total += n%10
        if n ==0 :
            break
        n = n//10
    return total
```



## 3. 회문

단어가 회문이면 True, 회문이 아니면 False를 반환하는 함수를 반복문(`while`)과 재귀 함수를 사용해서 각각 작성하시오.

```python
def is_re_while(word):
    while len(word)>1:
        if word[0] == word[-1]:
            word = word[1:-1]
        else:
            return False
    return True


def is_re_recursive(word):
    if len(word) <=1:
        return True
    if word[0]==word[-1]:
        return is_pal_recursive(word[1:-1])
    else:
        return False
```



