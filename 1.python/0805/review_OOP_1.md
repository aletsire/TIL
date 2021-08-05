# review_OOP

## 1. 넓이, 둘레

- 인스턴스 속성
  - `length`: 가로 길이
  - `width`: 세로 길이
- 인스턴스 메서드
  - `area`: 직사각형의 넓이를 리턴
  - `perimeter`: 직사각형의 둘레의 길이를 리턴

```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
```



## 2. Square

- Rectangle 클래스를 상속받아 Sqaure 클래스를 생성
  - Square 클래스는 Rectangle 클래스에서 상속받은 속성만 있다.
  - 정사각형이므로 인스턴스 생성시 인자로 한 변의 길이만

```python
class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
```



## 3. 개

1. 초기화 메서드는 인자로 개의 이름과 견종을 받아서 인스턴스 변수에 할당한다.
2. 클래스 변수는 태어난 개의 숫자와 현재 있는 개의 숫자를 기록하는 변수로 구성한다.
   - 개가 태어나면 `num_of_dogs`와 `birth_of_dogs`의 값이 각 1씩 증가한다.
   - 개가 죽으면 `num_of_dogs`의 값이 1 감소한다.
3. 개는 각자의 이름과 나이가 있다.
4. `bark()` 메서드를 호출하면 개는 짖을 수 있다.
5. `get_status()` 메서드를 호출하면 `birth_of_dogs`와 `num_of_dogs`의 수를 출력할 수 있다.

```python
class Doggy:
    num_of_dogs=0
    birth_of_dogs=0
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
        Doggy.num_of_dogs += 1
        Doggy.birth_of_dogs += 1

    def __del__(self):
        Doggy.num_of_dogs -= 1

    def bark(self):
        print('왈왈!')

    @classmethod
    def get_status(cls):
        print(f'Birth: {cls.birth_of_dogs}, Current: {cls.num_of_dogs}')
```



## 4. 팀 구성

**구성 요소**

1. 초기화 메서드는 인자로 학생 이름으로 구성된 리스트를 받아서 인스턴스 변수에 할당한다.
2. `pick(n)` 메서드는 학생들 명단에서 인자 n명 만큼 랜덤으로 추출하여 return한다.
3. `match_pair()` 메서드는 학생들 명단을 랜덤으로 2명씩 매칭해 준다. 이때, 학생들 명단의 수가 홀수명이면 단 한팀만 3명으로 구성한다.

```python
import random

class ClassHelper:
    def __init__(self, students):
        self.students = students
        
    def pick(self, number):
        return random.sample(self.students, number)
    
    def match_pair(self):
        random.shuffle(self.students)
        pairs = []
        pair_count = len(self.students) // 2
        
        for idx in range(pair_count):
            if idx == pair_count - 1:
                pair = self.students[idx*2:]
                pairs.append(pair)
                return pairs
            
            pair = self.students[idx*2:idx*2+2]
            pairs.append(pair)
```



