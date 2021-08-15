# 1. Web

- 웹 표준

  > W3C, WHATWG



# 2. HTML

> Hyper Text Markup Language

>  구글 효과: HyperText가 인간이 기억하는 방식까지 바꾼 효과

## 2.1 Markup Language

- 태그 등을 이용해서 문서나 데이터의 구조를 명시하는 언어
- 단순하게 데이터를 표현하기만 함
- ex) HTML, Markdown



## 2.2 HTML 기본구조

### 2.2.1 HTML 요소

- HTML문서의 최상위 요소로 문서의 root를 뜻한다.
- head와 body 부분으로 구분된다.

#### 2.2.1.1 head 요소

- 문서제목, 문자코드(인코딩)와 같이 해당 문서 정보 포함
- 브라우저에 나타나지 않는다.
- CSS 선언 혹은 외부 로딩 파일 지정 등도 작성

> OGP:
>
> - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
> - 페이스북에서 제작



#### 2.2.1.2 body 요소

- 브라우저 화면에 나타나는 정보로 실제 내용에 해당



### 2.2.2 DOM(Document Object Moder) 트리

- DOM은 문서의 구조화된 표현을 제공
- 프로그래밍 언어가 DOM 구조에 접근할 수 있는 방법을 제공, 문서 구조, 스타일 내용 등을 변경 할 수 있게 도움
- Web Page의 객체 지향 표현



### 2.2.3 요소

- 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그는 컨텐츠를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용 없는 태그들
  - br, hr, img, input, link, meta
- 요소는 중첩될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - 여는 태그와 닫는 태그의 쌍을 잘 확인
  - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력, 디버깅이 힘들어 질 수 있음



### 2.2.4 속성

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음
- 요소는 속성을 가질 수 있고, 경로나 크기 같은 추가적인 정보 제공
- 요소의 시작태그에 작성, 보통 이름과 값이 하나의 쌍으로 존재
- 태그와 상관 없이 사용가능한 속성들도 있음(HTML Global Attribute)

> HTML Global Attribute:
>
> - id, class
> - hidden
> - lang
> - style
> - tabindex
> - title



### 2.2.5 시멘틱 태그

- HTML5에서 의미론적 요소를 담은 태그의등장
- 대표적 태그들:
  - header: 문서 전체나 섹션의 헤더
  - nav: 네비게이션
  - aside: 사이드에 위치
  - section: 문서의 일반적인 구분
  - article: 문서 안에서 독립적으로 구분
  - footer: 문서의 마지막 부분

- 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- Non semantic 요소는 `div`, `span` 등이 있고 `h1`, `table` 태그들도 시멘틱 태그로 볼 수 있음

- 유지보수가 쉬워지고 코드의 가독성 높임



## 2.3 HTML 문서 구조화

- 마크업 예시

  ```html
  <header>
  	<h1>건강설문</h1>
  </header>
  <section>
  	<form action="#">
      	<div>
              <label for="name">이름을 기재해주세요</label><br>
              <input type="text" id="name" name="name" autofocus>
          </div>
          <div>
              <label for="region">지역을 선택해주세요</label>
              <select name="region" id="region" required>
                  <option value="서울">서울</option>
                  <option value="대전">대전</option>
                  <option value="대구">대구</option>
                  <option value="부산">부산</option>
              </select>
          </div>
          <input type="submit" value="제출"
      </form>
  </section>
  ```

  

# 3. CSS

> Cascading Style Sheets

> 스타일, 레이아웃 등을 통해 문서를 표시하는 방법을 지정하는 언어
>
> ```css
> h1{							-> 선택자(selctor)
>     color: blue;			-> 선언(declaration)
>     font-size: 15px;		-> 속성(property): 값(value)
> }
> ```

- CSS 구문은 선택자와 함께 열림
- 선택자를 통해 스타일을 지정할 HTML 요소를 선택
- 중괄호 안에서 속성과 값, 하나의 쌍으로 이뤄진 선언을 진행
- 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미

## CSS 정의 방법

#### - 인라인(inline)

- 해당 태그에 직접 `style`속성을 활용



#### - 내부 참조

- head 태그 내에 `<style>` 에 지정



#### - 외부 참조

- 외부 CSS 파일을 `<head>`내 `<link>`를 통해 불러오기



## 3.1 선택자(Selector)

- 특정 요소 스타일링 위해선 반드시 필요
- 기본 선택자
  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자
- 결합자
  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자

```html
<style>
	/* 전체 선택자 */
    * {
        color: red;
    }
    /* 요소 선택자 */
    h2 {
        color: orange;
    }
    
    h3,
    h4 {
        font-size: 10px;
    }
</style>
```

```html
<style>
	/* 클래스 선택자 */
    .green {
        color: green;
    }
    /* id 선택자 */
    #purple {
        color: purple
    }
    /* 자식 결합자 */
    .box > p {
        font-size: 30px;
    }
    /* 자손 결합자 */
    .box p{
        color: blue;
    }
</style>
```

### 3.1.1 CSS 선택자 정리

- 요소 선택자
  - HTML 태그를 직접 선택
- 클래스 선택자
  - 마침표(.)문자로 시작하며, 해당 클래스가 적용된 모든 항목을 선택
- id 선택자
  - `#`문자로 시작, 해당 아이디가 적용된 모든 항목을 선택
  - 일반적으로 하나의 문서에 1번만 사용
  - 여러번 사용해도 동작하지만, 단일 id 사용을 권장



### 3.1.2 CSS 적용 우선순위

1. `!important`
2. 인라인 > id 선택자 > class 선택자 > 요소 선택자
3. 소스 순서



### 3.1.3 CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
  - 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  - 상속 되는 것: Text 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것: Box model 관련 요소(width, margin, pading 등), position 관련 요소 등



## 3.2 CSS 단위

### 3.2.1 크기 단위

- px
  - 모니터 해상도의 한 화소인 픽셀을 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위
- %
  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용
- em
  - (바로 위 부모 요소에 대한)상속의 영향을 받음
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
- rem
  - (바로 위 부모 요소에 대한)상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐
- viewport
  - 웹페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정
  - `vw`,  `vh`,  `vmin`,  `vmax`



### 3.2.2 색상 단위

1. 색상 키워드
   - 대소문자를 구분하지않음
   - red, blue와 같은 특정 색을 직접 글자로 나타냄
2. RGB 색상
   - 16진법표기법, 함수형 표기법을 사용해서 색을 표현
3. HSL 색상
   - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식



## 3.3 CSS Selectors

### 3.3.1 결합자

- 자손 결합자
  - 하위의 모든 요소
- 자식 결합자
  - 바로 아래의 요소
- 일반 형제 결합자
  - 형제 요소 중 뒤에 위치하는 요소를 모두 선택
- 인접 형제 결합자
  - 형제 요소 중 바로 뒤에 위치하는 요소를 선택

```css
/* 자손 결합자 */
div span {
    color: red;
}
/* 자식 결합자 */
div > span {
    color: red;
}
/* 일반 형제 결합자 */
p ~ span {
    color: red;
}
/* 인접 형제 결합자 */
p + span {
    color: red;
}
```

```html
<span>p태그 앞에</span>
<p>문단 내용</p>
<span>p태그 바로 뒤</span>   /* 일반 형제 결합자, 인접 형제 결합자 경우 모두 적용 */
<b>다른 코드</b>
<span>p태그와 인접핟지 않은 span</span> /* 일반 형제 결합자일 경우 적용, 인접 형제 결합자 경우 적용되지 않음 */
```



## 3.4 CSS Box model

- 모든 HTML 요소는 box 형태로 구성
- 하나의 박스는 네 영역으로 이루어짐
  - content
  - padding
  - border
  - margin

### 3.4.1 box-sizing

- 기본적으로 모든 요소의 `box-sizing`은 `content-box`
  - Padding을 제외한 순수 contents 영역만을 box로 지정
- **우리가 일반적으로 영역을 볼 때는 border까지의 너비**를 보는 것을 원함
  - 그경우 `box-sizing`을 `border-box`로 설정



### 3.4.2 마진 상쇄

- block A의 top과 block B의 bottom에 적용된 각각의 margin이 둘 중 큰 마진 값으로 결합 되는 현상



## 3.5 CSS Display

### 3.5.1 display

- display: `block`
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지
  - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  - 대표적 요소: div / ul, ol, li / p / hr / form
- display: `inline`
  - 줄바꿈이 일어나지 않는 요소
  - content 너비만큼 가로 폭을 차지
  - width, height, margin-top등을 지정할 수 없다
  - 대표적 요소: span / a / img / input / b
- display: `inline-block`
  - block과 inline 레벨 요소 특징 모두 갖는다
  - inline처럼 한 줄에 표시
  - block처럼 width, height, margin 모두 지정 가능
- display: `none`
  - 해당 요소 화면에 표시하지 않음



## 3.6 CSS position

- 문서 상에서 요소를 배치하는 방법을 지정
- `static`: 모든 태그의 기본 값
  - 일반적으로는 좌측 상단
  - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치
- 좌표 property(`top`, `bottom`, `left`, `right`)를 사용해 이동이 가능한 요소들
  - relative: 상대 위치
    - 자기 자신의 static 위치를 기준으로 이동
    - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음
  - absolute: 절대 위치
    - 요소를 일반적인 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음
    - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동(없을 경우 body에 붙음)
  - fixed: 고정 위치
    - 레이아웃에 공간 차지하지 않음
    - 부모요소와 상관없이 viewpoint를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치

```css
div {
    height: 100px;
    width: 100px;
    background-color: blue;
    text-align: center;
}
```

```css
.relative {
    position: relative;
    top: 100px;
    left: 100px;
}
```

```css
.parent {
    position: relative;
}

.absolute-child {
    position: absolute;
    top: 50px;
    left: 50px;
}
```

```css
.fixed {
    postion: fixed;
    bottom: 0;
    right: 0;
}
```



### 3.6.1 absolute의 특징

- 원래 위치해 있었던 과거 위치의 공간은 더 이상 존재하지 않음
- 다른 모든 것과 별개의 독자적인 위치에 존재
- 다른 요소의 위치와 간섭하지 않는 격리된 인터페이스 기능을 만드는데 활용