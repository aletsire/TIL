# 04_데이터 구조 2

# 1. 세트(Set)

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)

## 1.1 추가 및 삭제

### 1.1.1 `.add(elem)`

elem을 세트에 추가



### 1.1.2 `.remove(elem)`

elem을 세트에서 삭제하고, 없으면 KeyError가 발생



### 1.1.3 `.discard(elem)`

elem을 세트에서 삭제하고 없어도 에러가 발생 X



### 1.1.4 `.pop()`

**임의의 원소**를 제거해 반환



# 2 딕셔너리(Dictionary)

> 변경 가능하고(mutable), 순서가 없고(unordered), 순회 가능한(iterable)
>
> `Key: Value` 페어(pair)의 자료구조

## 2.1 조회

### 2.1.1 `.get(key[, default])`

key를 통해 value를 사용

절대로 KeyError가 발생하지 않습니다. default는 기본적으로 None



## 2.2 추가 및 삭제

### 2.2.1 `.pop(key[, default])`

key가 딕셔너리에 있으면 제거하고 그 값을 돌려줍니다. 그렇지 않으면 default를 반환

default가 없는 상태에서 딕셔너리에 없으면 KeyError가 발생



### 2.2.2 `.update()`

값을 제공하는 key, value로  수정



