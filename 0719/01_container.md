# 01_컨테이너

여러 개의 값을 저장할 수 있는 것

- 시퀀스(Sequence)형: 순서가 있는(ordered) 데이터
- 비 시퀀스(Non-sequence)형: 순서가 없는(unordered) 데이터

# 1. 시퀀스(sequence)형 컨테이너

`시퀀스`는 데이터가 순서대로 나열된(ordered) 형식

* 순서대로 나열된 것 != `정렬되었다(sorted)`

## 1.1 특징
1. 순서를 가진다.

2. 데이터 위치 특정 가능



## 1.2 종류

* 리스트(list)
* 튜플(tuple)
* 레인지(range)
* 문자형(string)



## 1.3 리스트(`list`)

대괄호`[]` 및 `list()` 

값에 대한 접근은 `list[i]`



## 1.4 튜플(`tuple`)

 `()`로 묶어서 표현

tuple은 수정 불가능(불변, immutable)



## 1.5 레인지(`range()`)

`range`  숫자의 시퀀스를 나타내기 위해 사용

기본형 : `range(n)`

> 0부터 n-1까지 값을 가짐

범위 지정 : `range(n, m)`

> n부터 m-1까지 값을 가짐

범위 및 스텝 지정 : `range(n, m, s)`

> n부터 m-1까지 +s만큼 증가한다



# 2. 비 시퀀스형(Non-sequence) 컨테이너

- 세트(set)
- 딕셔너리(dictionary)

## 2.1 `set`

`set` 순서가 없고 중복된 값이 없는 자료구조

- `set`는 중괄호`{}`를 통해 만듦
- 빈 세트를 만들려면 `set()`을 사용 (`{}` 사용 불가능)
- 활용할 수 있는 연산자는 차집합(`-`), 합집합(`|`), 교집합(`&`)



## 2.2 `dictionary`

`dictionary`는 `key`와 `value`로 구성



## 2.3 데이터의 분류

> ```
> mutable` vs. `immutable
> ```

데이터 변경 가능한 것(`mutable`)들과 변경 불가능한 것(`immutable`)로 구분

### 2.3.1 변경 불가능한(`immutable`) 데이터

- 리터럴(literal)
  - 숫자(Number)
  - 글자(String)
  - 참/거짓(Bool)
- range()
- tuple()
- frozenset()



### 2.3.2 변경 가능한(`mutable`) 데이터

- `list`
- `dict`
- `set`