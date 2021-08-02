# Week 1_review_1

## 1. 세로로 출력

 1부터 5까지의 수를 세로로 한줄씩 출력하시오.

```python
number = 5
for i in range(1,number+1):
    print(i)
```



## 2. 거꾸로 세로로 출력

5부터 0까지의 수를 세로로 한줄씩 출력하시오.

```python
number = 5
for num in range(number,-1,-1):
    print(num)
```



## 3. N줄 덧셈

 1부터 주어진 자연수 10까지를 모두 더한 값을 출력하시오.

```python
number = 10
total = 0
for num in range(number+1):
    total += num
print(total)
```



## 4. N의 약수

10의 약수를 오름차순으로 출력하는 프로그램을 작성하시오

```python
number = 10
for num in range(1,number+1):
    if number % num == 0:
        print(num, end = ' ')
```



## 4. 중간값

리스트 numbers에 입력된 숫자에서 중간값을 출력하라.

```python
numbers = [
    85, 72, 37, 80, 69, 65, 68, 95, 22, 49, 67,
    51, 61, 63, 87, 66, 25, 80, 84, 71, 60, 64,
    52, 89, 60, 49, 31, 23, 100, 94, 11, 25, 24
]
numbers_sort = sorted(numbers)
print(numbers_sort[int((len(numbers_sort)-1)/2)])
```





## 6. 계단 만들기

자연수 4를 입력 받아, 아래와 같이 높이가 4인 내려가는 계단을 출력하시오.

```python
[출력 예시]
1
1 2 
1 2 3 
1 2 3 4 
```

```python
for i in range(1,number+1):
    for j in range(1, i+1):
        print(j, end =' ')
    print()
```

