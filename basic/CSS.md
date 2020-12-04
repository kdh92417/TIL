# CSS(Cascading Style Sheet) 기초

<br>

## 어떻게 CSS와 HTML를 합칠까?

- 첫번쨰는 같은 HTML코드와 CSS코드를 놓는 방법

  - head 부분에 style 태그안에 CSS 코드를 포함시킨다.
  - `inline CSS`라 한다.
  - 예시

    ```html
    <head>
      <style></style>
    </head>
    ```

      <br>

- **두번쨰는 CSS와 HTML를 분리시키는 방법 (이방법으로 하는 것을 추천)**

  - CSS파일을 만든다. (styles.css)

  - `link` 태그를 이용해서 파일을 연결한다.
  - styles.css는 HTML과의 관계에 있어서 **스타일시트** 이다.
  - `external CSS` 라 한다.
  - 예시
    ```html
    <head>
      <link href="styles.css" rel="stylesheet" />
    </head>
    ```
      <br>

<br>

## CSS의 규칙들

1. CSS가 하는 일은 HTML 태그를 가르키는 일이다.

   - 가리키는 것 자체를 `selector` 라고 한다.

   - selector 안에 있는 코드를 `속성(Property)` 이라 한다.
   - 속성을 쓴 줄의 마지막에 `새미콜론(';')` 을 붙여야한다.
   - 예시
     ```css
     h1 {
       color: blue;
       font-size: 20px;
     }
     ```
     <br>

<br>

## Cascading의 뜻

> CSS의 맨 앞에 있을 정도로 매우 중요한 개념인데, 브라우저가 CSS코드를 읽을 때 위에 있는 코드부터 차례차레로 읽힌다는 뜻이다.

- 즉, 코드의 순서가 결과에 영향을 미친다.

<br><br>

## Block vs Inline

- `inline` element : 한줄에 이어서 나오는 태그 ex) `span`, etc..
- `block` element : 옆에 아무것도 없이 한줄을 다차지 하는 태그 ex) `div`, `image`, etc..

- block만 가지고 있는 특징

  - block은 높이와 너비를 가지고 있다.
  - block은 box이다.
  - `margin`, `padding`, `border`의 특징을 가지고 있다.

- inline 특징
  - 높이와 너비를 가질 수 없다.

<br></br>

## margin, border, padding

### margin

- box의 border(경계)의 바깥에 있는 공간이다.

- 값이 하나면 사방에 다 적용되고, 2개면 top/bottom , left/right 로 되고, 4개 값의 적용되면 top, right, bottom, left로 적용이 된다.

- ```css
  margin: 10px 20px;
  margin: 10px 30px 40px 50px;
  margin: 30px;
  ```

- > #### collapsing margins 현상
  >
  > 여러 블록의 위쪽 및 아래쪽 바깥 여백(마진)은 경우에 따라 제일 큰 여백의 크기를 가진 단일 margin 으로 결합(상쇄)되곤 합니다. 이런 현상을 `collapsing margin` 현상이라고 한다.
  >
  > 서로다른 box의 border이 같을 때 이런 현상이 일어납니다.
  >
  > 위/아래 쪽만 이런 현상이 일어납니다.

<br>

### padding

- box border(경계)의 안쪽에 잇는 공간이다.

- margin과 마찬가지로 값이 1개일때는 사방, 2개일때는 위아래, 4개일때는 좌/위/우/아래 값을 나타낸다.

<br>

### border

- border는 말 그대로 box의 경계(border)이다.

- border의 속성
  - ```css
    border: 선굵기 선스타일 색상;
    ```
    ```css
    div {
      border: 2px solid black;
    }
    ```

<br>

### Useful Tip

- inline일 경우 margin은 좌/우 의 값만 가지고, padding은 사방에 공간을 가질 수 있다.

<br>

## Id 와 Class

- `id`는 스타일을 지정할 때 한가지만 지정해서 쓰는 이름 (표기 방식은 `#이름`)

- `class`는 그룹으로 묶어서 스타일을 지정할 때 쓰는 이름 (표기방식은 `.이름`)
  - 한 태그에 여러 클래스를 가질 수 있다. (id는 1개만)

<br>

## display 태그

<br>

### inline-block 속성

> inline의 속성을 가지되 block으로 인식하게 하여 높이와, 너비 그리고 사방에 마진을 가질 수 있다. 하지만 old하고 많은 문제가 있어 별로 추천하지는 않는다.

        1. default 값의 빈 공간이 있어 좋지 않다. (아무것도 추가하지 않았지만 box 간에 빈공간이 생김)
        2. 정해진 형식이 없어서 깔끔하지 않다.
        3. 반응형 디자인을 할 수가 없다.

<br>

## Flexbox

> 위의 `display`의 단점을 개선하고 좀더 편리하게 box들을 디자인하고자 만든 것이 `flexbox`이다.

flexbox의 규칙

**1. 자식 엘리먼트에는 어떤 것도 적지 말아야된다. (부모엘리먼트에만 명시해야된다.ex) `div`의 부모를 `display`: `flex`;로 만든다.)**

- 예시

  ```css
  body {
    display: flex;
  }
  ```

- `display: flex;` 로 flex 속성을 주면 `justify-content` 속성을 적용할 수 있다.

<br>

**2. 주축(main axis)와 교차축(cross axis)**

> `main axis` 와 `cross axis`는 flexbox 에서 기본적으로 축들이 가지는 모습이다.

<image src="https://miro.medium.com/max/1173/1*2k7hWdeIsF_Hor_5O4w1Mg.png" width="70%">

- `justify-content` 의 property(속성)은 main axis(주축)위에서 움직인다.

- `align-items` 라고 불리는 property(속성)는 cross axis(교차축)에 적용 된다.

- 하지만 `main axis` 와 `cross axis`는 바꿀 수 있다.

  - `flex-direction`의 옵션을 default인 `row`에서 `column`으로 바꾸면 된다.

  - 예시
    ```css
    body {
      flex-direction: column;
    }
    ```

<br>

### flex-wrap

- `flex-wrap: nowrap;`

  - 모든 요소를 같은 줄에 있게 만들어준다.

  - flexbox의 width의 사이즈는 초기 설정값으로면 인식하고 같은 줄에 하기위해 사이즈를 바꾼다.

<br>

## Etc

- `*` 의 뜻은 전부를 뜻한다.

  - ```css
    * {
      border: 1px solid black;
    }
    ```

- selector 간에 `,`(쉼표)를 넣어서 css태그를 적용시킬 수 있다.

  - ```css
    #tomato,
    #tomato2 {
      color: black;
    }
    ```

- `vh` : viewport height 라고하는데 100vh는 화면(스크린) 높이의 100%를 말한다.
  - 화면에 크기에 따라 높이가 바뀐다.
