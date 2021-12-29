# CSS(Cascading Style Sheet) 기초

<br>

## 1. 어떻게 CSS와 HTML를 합칠까?

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

<br><br>

## 2. CSS의 규칙들

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

<br><br>

## 3. Cascading의 뜻

> CSS의 맨 앞에 있을 정도로 매우 중요한 개념인데, 브라우저가 CSS코드를 읽을 때 위에 있는 코드부터 차례차레로 읽힌다는 뜻이다.

- 즉, 코드의 순서가 결과에 영향을 미친다.

<br><br>

## 4. Block vs Inline

- `inline` element : 한줄에 이어서 나오는 태그 ex) `span`, etc..
- `block` element : 옆에 아무것도 없이 한줄을 다차지 하는 태그 ex) `div`, `image`, etc..

- block만 가지고 있는 특징

  - block은 높이와 너비를 가지고 있다.
  - block은 box이다.
  - `margin`, `padding`, `border`의 특징을 가지고 있다.

- inline 특징
  - 높이와 너비를 가질 수 없다.

<br></br>

## 4. margin, border, padding

### margin

- box의 border(경계)의 바깥에 있는 공간이다.

- 값이 하나면 사방에 다 적용되고, 2개면 top/bottom , left/right 로 되고, 4개 값의 적용되면 top, right, bottom, left로 적용이 된다.

- ```css
  margin: 10px 20px;
  margin: 10px 30px 40px 50px;
  margin: 30px;
  ```

<br>

> ### collapsing margins 현상
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

## 5. Id 와 Class

- `id`는 스타일을 지정할 때 한가지만 지정해서 쓰는 이름 (표기 방식은 `#이름`)

- `class`는 그룹으로 묶어서 스타일을 지정할 때 쓰는 이름 (표기방식은 `.이름`)
  - 한 태그에 여러 클래스를 가질 수 있다. (id는 1개만)

<br><br>

## 6. display 태그

- ### inline-block 속성

> inline의 속성을 가지되 block으로 인식하게 하여 높이와, 너비 그리고 사방에 마진을 가질 수 있다. 하지만 old하고 많은 문제가 있어 별로 추천하지는 않는다.

<br>

- 안좋은 이유

  1. default 값의 빈 공간이 있어 좋지 않다. (아무것도 추가하지 않았지만 box 간에 빈공간이 생김)

  2. 정해진 형식이 없어서 깔끔하지 않다.
  3. 반응형 디자인을 할 수가 없다.

<br><br>

## 7. Flexbox

> 위의 `display`의 단점을 개선하고 좀더 편리하게 box들을 디자인하고자 만든 것이 `flexbox`이다.

<br>

- ### flexbox의 규칙

  1.  자식 엘리먼트에는 어떤 것도 적지 말아야된다. (부모엘리먼트에만 명시해야된다.ex) `div`의 부모를 `display`: `flex`;로 만든다.)

      - 예시

        ```css
        body {
          display: flex;
        }
        ```

      - `display: flex;` 로 flex 속성을 주면 `justify-content` 속성을 적용할 수 있다.

      <br>

  2.  주축(main axis)와 교차축(cross axis)

      > `main axis` 와 `cross axis`는 flexbox 에서 기본적으로 축들이 가지는 모습이다.

<br>

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

<br><br>

## 8. Position 태그

### `position: fixed;`

- 스크롤을 내려도 위치가 변함이 없다.

- `top, right, bottom, left` : 절대 좌표로서 위치를 지정한다.

<br>

### `position: relative;`

- element가 처음 위치한 곳을 기준으로 수정한다.

- `top, right, bottom, left` : 상대 좌표로서 위치를 지정한다.

<br>

### `position: absolute;`

- absolute는 가장 가까운 relative 부모를 기준으로 이동시켜준다.

- `top, right, bottom, left` : 가까운 relative 부모를 기준으로 위치를 이동

<br><br>

## 9. Pseudo Selectors

세부적으로 엘리먼트를 선택해주는 것을 **Pseudo Selector** 라고 한다.

<br>

### 예시

- 첫번째 div : `div:first-child`

- 마지막 div : `div:last-child` or `div:last-of-type`

- 원하는 순서의 div : `div:nth-child(숫자)`

  - 숫자에 방정식을 넣어도됨 ex) `div:nth-child(2n + 3)` : 3번째부터 짝수 인것들 지정

- input태그의 required 인지 아닌지 여부에 따라 지정

  - `input:required {}` or `input:optional {}`

<br>

### Combinators

- `태그` `태그` : 태그안에 태그를 지정

  - `span p {}` : `span` 안에 있는 `p`태그

- 부모태그 `>` 자식태그 : 부모태그 바로밑에있는 자식태그를 지정

  - `div > span` : `div` 태그 바로 밑에 있는 `span` 태그

- 태그형제 `+` 태그 : 형제태그 옆에있는 태그를 지정

  - `div` + `span` : `div`태그 바로 옆 `span`태그 지정

- 태그 `~` 태그 : 바로 옆에있지는 않은 이웃 형제태그를 지정

  - ```html
      <style>
        <!-- p태그 옆 span태그를 지정하고 싶을떄 `+` 태그로는 바로옆이 아니라서 지정이안된 그래서 -->
        <!-- `~` 태그로 지정 -->
        p ~ span {
          color: white;
        }
      <style>
      <body>
        <div>
          <p>
          </p>
          <address>hi</address>
          <span>hello</span>
        </div>
      </body>
    ```

<br>

### Attribute를 통해 지정

- `태그[Attribute] {}` : 해당 태그 안에 있는 모든 Attribute를 가진 태그를 지정

  - `input[type="password"] {}` : input태그의 type이 password인 태그 지정

- `~` : 어떤 text가 포함된 모든 태그를 지정

  - `input[placeholder~="name"] {}` : placeholder에 `name` 이 포함된 모든 태그지정

  - `$` : 끝에 오는 경우

  - `^` : 처음에 오는 경우

<br>

### States

- active : 버튼을 누르고 있을 때

  - ex) `button:active {}`

- hover : 마우스가 대상 위에 놓여져 있을 때

- focus : 키보드로 선택되었을 때

- visited : 링크를 클릭 했엇을 때

- focus-within : focused인 자식을 가진 부모 엘리먼트에 적용

<br>

### 기타

- `::` : 해당 상태나 액션 등을 취할 때 그 상태 또는 액션만 변화하게 만든다.

  - `::placeholder` : placeholder

  - `::selection` : 드래그할 때

  - `::first-letter` : 첫 글자

<br><br>

## Variables

css에서도 프로그래밍 언어처럼 변수를 저장하여 사용 할 수가 있다.

### 예시

- ```css
  :root {
    --main-color: #fcce01;
    --default-border: 1px solid var(--main-color);
  }

  p {
    background-color: var(--main-color);
  }
  a {
    background-color: var(--main-color);
    border: var(--default-border);
  }
  ```

- `--main-color`를 document의 root에 저장한 뒤

- `var(--main-color)` 를 저장해두었던 변수에서 끄집어서 사용할 수가 있다.

- `--` + `변쉬이름` 저장, 공백이 있을 시 dash `-` 로 채우고 사용시에는 `var(변수이름)`

<br><br>

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
