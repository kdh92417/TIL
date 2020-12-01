# CSS(Cascading Style Sheet) 기초

<br>

## 어떻게 CSS와 HTML를 합칠까?

---

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

---

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

---

> CSS의 맨 앞에 있을 정도로 매우 중요한 개념인데, 브라우저가 CSS코드를 읽을 때 위에 있는 코드부터 차례차레로 읽힌다는 뜻이다.

- 즉, 코드의 순서가 결과에 영향을 미친다.
