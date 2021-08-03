# data_structure_dict_review

## 1. 딕셔너리 순회

혈액형 검사한 결과가 담긴 `blood_types`이 주어졌을때, 해당 딕셔너리를 순회하며, `key`와 `value`를 출력

```python
[출력예시]
A형은 10명입니다.
B형은 11명입니다.
AB형은 5명입니다.
O형은 23명입니다.
```

```python
blood_types = {'A': 10, 'B': 11, 'AB': 5, 'O': 23}

for k, v in blood_types.items():
    print(f'{k}형은 {v}명입니다.')
```



## 2. 딕셔너리 순회 v.2

해당 검사에 참가한 사람들의 총합을 구해보세요

```python
[출력예시]
검사에 참가한 사람은 총 48명입니다.
```

```python
blood_types = {'A': 10, 'B': 11, 'AB': 5, 'O': 23}
total = 0
for k, v in blood_types.items():
    total += v
print(f'검사에 참가한 사람은 {total}명입니다.')
```



## 3. 딕셔너리 구축하기

리스트가 주어질 때, 각각의 요소의 개수를 value 값으로 갖는 딕셔너리 구축

```python
book_title =  ['great', 'too', 'the', 'adventures', 'of', 'holmes', 'the', 'great', 'too', 'hamlet', 'adventures', 'of', 'many', 'fin']
result = {}
for title in book_title:
    if result.get(title,0) == 0:
        result[title] = 1
    else:
        result[title] += 1
print(result)
```

```python
book_title =  ['great', 'too', 'the', 'adventures', 'of', 'holmes', 'the', 'great', 'too', 'hamlet', 'adventures', 'of', 'many', 'fin']
result = {}
for title in book_title:
    result[title] = book_title.count(title)
print(result)
```

