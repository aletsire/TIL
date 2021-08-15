# 1. CSS layout

## 1.1 Float

- none: 기본값
- left: 요소를 왼쪽으로 띄움
- right: 요소를 오른쪽으로 띄움

```css
.left {
    float: left;
}
```

- Float clear

```css
.clearfix::after {
    content: "";
    display: block;
    clear: both;
}
```

> - float하고 나서 사이의 빈 공간을 없에기 위한 방법
> - 기본값은 inline



## 1.2 Flexbox

- 요소 간 공간 배분과 정렬 기능을 위한 1차원 레이아웃
- 요소
  - Flex Container(부모 요소)
    - display 속성을 flex 혹은 inline-flex로 지정
  - Flex Item(자식 요소)
- 축
  - main axis(메인축)
  - cross axis(교차축)

```css
.flex-container {
    display: flex;
}
```

### 1.2.1 Flex에 적용하는 속성

- 배치방향 설정
  - flex-direction
    - item이 쌓이는 방향 설정
    - main-axis가 변경
    - row(default): 주축의 방향이 왼쪽에서 오른쪽
    - column: 위에서 아래
    - row-reverse
    - column-reverse
- 메인축 방향 정렬
  - justify-content
    - main축 정렬
    - flex-strat(default): 시작 지점부터 차례로
    - flex-end: 쌓이는 방향이 뒤쪽부터
    - center
    - space-between: 좌우 정렬(item들 간의 간격이 동일)
    - space-around: 균등 좌우 정렬(내부 여백은 외각 여백의 2배)
    - space-evenly: 균등 정렬(모든 여백이 동일)
- 교차축 방향 정렬
  - align-items
    - cross 축 정렬
    - stretch(default): 컨테이너를 가득 채움
    - flex-start: 위
    - flex- end
    - center
    - baseline: item 내부의 text에 기준선을 맞춤
  - align-self
    - 개별 item에 적용
    - auto(default)
    - flex-start
    - flex-end
    - center
    - baseline
    - stretch: 부모 컨테이너에 자동으로 맞춰서 늘어남
  - align-content
- 기타
  - flex-wrap
    - 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
    - nowrap(default): 모든 아이템들을 한 줄에 나타냄(자리가 없어도 튀어나옴)
    - wrap: 넘치면 아랫줄로
    - wrap-reverse: 넘치면 윗줄로
  - flex-flow
    - flex-direction과 flex-warp의 설정값을 순서대로 작성
  - flex-grow
    - 주축에서 남는 공간을 항목들에게 분배하는 방법
    - 상대적 비율 정하는 것 아님
    - default: 0
    - 음수 불가능
  - order
    - 적은 숫자일수록 앞으로 이동

```html
<style>
    .flex-container {
     /* 정렬하려고하는 부모요소에 선언 */
        dispaly: flex;
    
    /* 요소들을 한줄로 배치되게 할 것인지 여부 결정 */  
    /* flex-wrap: nowrap  -> 이게 기본값 */
	/* flex-wrap: wrap */
    flex-wrap: wrap-reverse;        
    flex-direction: column;   /* flex-flow: column wrap  -> 이걸로 한번에 표시*/
</style>
```



# 2. Bootstrap

- CDN(Content Delivery Network)
  - 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

> 브라우저 <html>의 root 글꼴 크기는 16px -> 1rem: 16px

## Spacing

- mx-0

```css
.mx-0 {
    margin-right: 0;
    margin-left: 0;
}
```

- mx-auto

```css
.mx-auto {
    margin-right: auto;
    margin-left: auto
}
```

- py-0

```css
.py-0 {
    padding-top: 0;
    padding-bottom: 0;
}
```

> s: left
>
> r: right

```html
<div class="box mt-3 ms-5">margin-top 3 margin-left 5</div>
<div class="box m-5">margin 5</div>
<div class="box mx-auto">좌우 가운데 정렬</div>
<div class="box ms-auto">오른쪽 정렬</div>
```

### Color

```html
<div class="bg-primary">파랑</div>
<div class="bg-secondary">회색</div>
<div class="bg-danger">빨강</div>
<div class="text-success">파란 글씨</div>
<div class="text-danger">빨간 글씨</div>
```

### Text

```html
<div class="text-start">앞에서 글시작</div>
<div class="text-center">가운데 정렬</div>
<div class="text-end">마지막으로 정렬</div>
<a href="#" class="text-decoration-none">하이퍼링크 underline없이</div>
<div class="fw-bold">굵은 글씨</div>
<div class="fw-normal">일반 글씨</div>
<div class="fw-light">가는 글씨</div>
<div class="fst-italic">이탈리체(기울어진)</div>
```

### Display

```html
<div class="d-inline p-2 bg-primary">한줄 안에 필요한 공간만 차지하는 파란색</div>
<div class="d-block p-2 bg-primary">한줄 안에 필요한 공간만 차지하는 검은색</div>
<div class="d-block p-2 bg-dark">한줄을 다 차지하는 검은색</div>
<div class="box bg-success d-sm-none d-md-block">일정 viewpoint에선 보이고 안보이고</div>
```

### Responsive Web Design

- 다양한 화면 크기를 가진 디바이스들로 인해 등장



## Grid system

- flexbox로 제작
- `container`, `rows`, `column`으로 컨텐츠 배치 및 정렬
- 12개의 column, 6개의 grid breakpoints

```html
<div class="container">
    <div class="row">
        <div class="box col-9">col-9</div>
        <div class="box col-4">col-4</div>
        <div class="box col-3">col-3</div>
    </div>
</div>
```



```html
<div class="container">
    <div class="row justify-content-center align-items-center">
        <div class="box col-9">col-9 상하좌우 가운데 위치</div>
    </div>
</div>
```



```html
<div class="container">
    <div class="row">
        <div class="box col-9 align-self-start">col-9 보조축 위에서부터</div>
        <div class="box col-4 align-self-center">col-4 보조축 가운데</div>
        <div class="box col-3 align-self-end">col-3 보조축 아래에서부터</div>
    </div>
</div>
```

