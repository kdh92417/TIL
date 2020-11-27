# 기초 HTML

<br>

## HTML이란 ?

- HTML(HyperText Markup Language)은 웹페이지를 기술하기 위한 마크업 언어 이다.
  좀더 자세히 말하자면 웹페이지의 내용(content)과 구조(structure)을 담당하는 언어로써 HTML 태그를 통해 정보를 구조화하는 것이다.

- 최근 HTML5 버전까지 업데이트 되었다.
- [HTML의 등장과 배경](https://webclub.tistory.com/491)

## HTML5

- HTML5는 문서는 `<!DOCTYPE html>`으로 시작하여 문서형식(document type)을 HTML5로 지정한다.
- 예시

```html
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8" />
    <title>Hello World</title>
  </head>
  <body>
    <h1>Hello World</h1>
    <p>안녕하세요 HTML5 입니다.</p>
  </body>
</html>
```

<br>

## 기본문법

### 1. 태그

- <태그이름> 으로 시작하여 <태그이름/> 으로 끝나고 태그 사이에 내용이 있는 구조를 요소라고 합니다.
- 끝 태그가 필요없는 것은 태그가 그 자체로 요소가 됩니다.
  ![HTML 요소](https://poiemaweb.com/img/tag.png)

- 한글, 일본어, 중국어가 포함된 페이지라면 utf-8 이라는 값으로 문자 인코딩을 추가해줘야 합니다.

```html
<meta charset="utf-8" />
```

- 디바이스의 가로 크기가 곧 웹 페이지의 가로와 같다는 의미입니다. 모바일에서 웹사이트가 예쁘게 잘 보이려면 추가해야 하는 정보입니다. 해당 정보를 추가하지 않으면 데스크탑 버전의 웹페이지가 축소되어 보이는 현상이 나타납니다.

```html
<meta name="viewport" content="width=device-width" />
```

<br>

### 2. 어트리뷰트 (Attribute)

- 어트리뷰트(Attribute 속성)이란 요소의 성질, 특징을 정의하는 명세이다. 요소는 어트리뷰트를 가질 수 있으며 어트리뷰트는 요소에 추가적 정보(이미지 파일의 경로, 크기 등..)를 제공한다.
  ![Attribute](https://poiemaweb.com/img/html-attribute.png)

<br>

### 3. 주석 (Comments)

- 주석은 주로 개발자에게 코드를 설명하기 위해 사용되며 브라우저는 주석을 화면에 표시하지 않는다.
<pre><code>Lorem ipsum dolor sit amet consectetur adipisicing elit. Maiores, cum?</code></pre>

<br>

### 4. 문법

---

#### ol 태그와 ul태그

- ul : unordered list  
  순서가 없는 목록 리스트
- ol : ordered list
  순서가 있는 목록 리스트

```html
<ul>
  <li>감자</li>
  <li>고구마</li>
</ul>
<ol>
  <li>웨이트</li>
  <li>내추럴</li>
</ol>
```

> <ul>
>   <li>감자</li>
>   <li>고구마</li>
> </ul>
> <ol>
>   <li>웨이트</li>
>   <li>내추럴</li>
> </ol>

### Reference

- https://poiemaweb.com/
