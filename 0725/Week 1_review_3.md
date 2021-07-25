# Week 1_review_3

## 1. 최댓값 횟수 구하기

 최댓값과 등장 횟수를 출력하시오.

```python
numbers = [3, 10, 25, 3, 25, 20, 25]

max=0
for i in numbers:
    if i >= max:
        max = i
count =0
for i in numbers:
    if i == max:
        count += 1

print(max,count)
```



## 2. n을 제외

'banana'에서 'n'를 모두 제거한 결과를 출력하시오.

```python
word = 'banana'
answer =''
for i in word:
    if i != 'n':
        answer += i
print(answer)
```



## 3. 단어 뒤집기

orange를 역순으로 뒤집은 결과를 출력하시오.

```python
print(orange[::-1])
```



## 4. 절대값 구하기

복소수일 경우는 절대값을 숫자형일 경우는 절대값을 반환

```python
def my_abs(n):
    if type(n) == complex:
        return (n.real**2 + n.imag**2)**(1/2)
    else:
        if n == 0:
            return n**2
        elif n < 0:
            return -n
        else:
            return n
```



## 4. all()

all()을 직접 구현해보기

```python
def per_all(elements):
    answer = True
    for element in elements:
        if not element:
            answer = False
    return answer
```





## 6. any()

any()를 직접 구현해보기(이번엔 가변함수를 이용해서)

```python
def my_any(*args):
    answer = False
    for arg in args:
        for i in arg:
            if i:
                answer = True
                break
    return answer
```

```python
for i in range(1,number+1):
    for j in range(1, i+1):
        print(j, end =' ')
    print()
```

