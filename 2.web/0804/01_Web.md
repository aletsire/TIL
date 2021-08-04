# Web

## Float

- none: 기본값

- left: 요소를 왼쪽으로 띄움

- right: 요소를 오른쪽으로 띄움

  ### Floatclear

  - 선택한 요소의 맨 마지막 자식으로 가상 요소를 하나 생성
  - 보통 content 속성과 함께 짝지어, 요소에 작식용 콘텐츠를 추가할 때 사용
  - 기본값은 inline

```css
.clearfix::after {
    content: "";
    display: block;
    clear: both;
  }
```



## Flexbox

- 요소 간 공간 배분과 정렬 기능을 위한 1차원(단방향) 레이아웃

- 요소

  - Flex Container
  - Flex Item

- 축

  - main axis
  - cross axis

  ### flexbox의 구성요소

  - Flex Container(부모요소)

    - flexbox 레이아웃을 형성하는 가장 기본적인 모델
    - Flex Item들이 놓여있는 영역
    - display 속성을 flex 혹은 inline-flex로 지정

  - Flex Item(자식요소)

    - 컨테이너의 컨텐츠

    ```css
    .flex-container {
        display: flex
    }
    ```

    

  ### Flex에 적용하는 속성

  - 배치 방향 설정
    - flex-direction
  - 메인축 방향 정렬
    - justify-content
  - 교차축 방향 정렬
    - align-items, align-self, align-content
  - 기타
    - flex-wrap, flex-flow, flex-grow, order

  ### flex-direction

  - main-axis 방향만바뀐다.
  - flexbox는 단방향 레이아웃이기 때문

  ### content & items & self

  - content
    - 여러 줄
  - items
    - 한 줄
  - self
    - flex item 개별 요소



## Bootstrap

> CDN(Content Delivery Network)
>
> : 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

### Responsive Web Design

- 다양한 화면 크기를 가진 디바이스들이 등장함에 따라 responsive web design 개념이 등장
- 반응형 웹은 별도의 기술 이름이 아닌 웹 디자인에 대한 접근 방식, 반응형 레이아웃 작성에 도움이 되는 사례들의 모음 등을 기술하는데 사용되는 용어

### Grid system

- Bootstrap Grid system은 flexbox로 제작됨
- `container`, `rows`, `column`으로 컨텐츠를 배치하고 정렬
  - 12개의 column
  - 6개의 grid breakpoints

​		



​	



