# 04_데이터 구조 1

# 1. 문자열(String)

> 변경할 수 없고(immutable), 순서가 있고(ordered), 순회 가능한(iterable)

## 1.1 조회/탐색

### 1.1.1 `.find(x)`

x의 **첫 번째 위치**를 반환없으면, `-1`을 반환



### 1.1.2 `.index(x)`

x의 **첫번째 위치**를 반환. 없으면, 오류가 발생



## 1.2 문자열 변경

### 1.2.1 `.replace(old, new[, count])`

바꿀 대상 글자를 새로운 글자로 바꿔서 반환

count를 지정하면 해당 갯수만큼만 시행



### 1.2.2 `.strip([chars])`

특정한 문자들을 지정하면, 양쪽을 제거하거나 왼쪽을 제거하거나(lstrip), 오른쪽을 제거(rstrip).

지정하지 않으면 공백을 제거



### 1.2.3 `.split([chars])`

문자열을 특정한 단위로 나누어 리스트로 반환



### 1.2.4 `'separator'.join(iterable)`

특정한 문자열로 만들어 반환합니다.

반복가능한(iterable) 컨테이너의 요소들을 separator(구분자)로 합쳐(`join()`) 문자열로 반환합니다.



### 1.2.5 `.capitalize()`, `.title()`, `.upper()`

- `.capitalize()` : 앞글자를 대문자로 만들어 반환
- `.title()` : 어포스트로피나 공백 이후를 대문자로 만들어 반환
- `.upper()` : 모두 대문자로 만들어 반환



### 1.2.6 `.lower()`, `.swapcase()`

- `lower()` : 모두 소문자로 만들어 반환
- `swapcase()` : 대 <-> 소문자로 변경하여 반환



# 2. 리스트(List)

> 변경 가능하고(mutable), 순서가 있고(ordered), 순회 가능한(iterable)

## 2.1 값 추가 및 삭제

### 2.1.1 `.append(x)`

리스트에 값을 추가 가능

문자열 추가할떄



### 2.1.2 `.extend(iterable)`

리스트에 iterable(list, range, tuple, string) 값을 추가 가능

리스트 추가할 때 



### 2.1.3 `.insert(i, x)`

정해진 위치 `i`에 값을 추가

> 리스트 길이를 넘어서는 인덱스는 마지막에 아이템 추가



### 2.1.4 `.remove(x)`

리스트에서 값이 x인 것을 삭제

> remove는 값이 업으면 오류 발생



### 2.1.5 `.pop(i)`

정해진 위치 `i`에 있는 값을 삭제하며, 그 항목을 반환

`i`가 지정되지 않으면 마지막 항목을 삭제



## 2.2 탐색 및 정렬

### 2.2.1 `.index(x)`

x 값을 찾아 해당 index 값을 반환

> 찾는 값이 없으면 오류 발생



### 2.2.2 `.count(x)`

원하는 값의 개수를 반환



### 2.2.3 `.sort()`

정렬

내장함수 `sorted()` 와는 다르게 **원본 list를 변형**시키고, **`None`**을 리턴



### 2.2.4 `.reverse()`

반대로 나열  **(정렬 아님)**



## 2.5 리스트 복사 방법

### 2.5.1 slice 연산자 사용 `[:]`

```
a = [1, 2, 3]
```

```
# slice 연산자로 리스트 a의 모든 요소를 변수 b에 저장
# 리스트 b의 첫번째 값을 5로 바꾸고 리스트 a를 출력
# slice 연산자를 활용하면 새로운 리스트를 저장
# ===== 
b = a[:]

b[0] = 5
print(a)
[1, 2, 3]
```



# 3. 데이터 구조에 적용가능한 Built-in Function

순회 가능한(iterable) 데이터 구조에 적용가능한 Built-in Function

> iterable 타입 - `list`, `dict`, `set`, `str`, `bytes`, `tuple`, `range`

## 3.1 `map(function, iterable)`

- 순회가능한 데이터 구조(iterable)의 모든 요소에 function을 적용.

- return은 `map_object` 형태

