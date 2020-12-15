# Html 과 CSS를 이용하여 Messenger Website를 만들면서 배운 것들

## .gitignore

- `.gitignore` : 깃에 올리고싶지 않은 것들을 자동으로 올리지 제외시키게 하는 파일이다.

  - 파일을 `.gitignore`로 만든 뒤, `.확장자` 쓰면 된다.
  - 폴더는 `/폴더이름`

<br>

## index.html

- index.html : 대부분의 웹 서버가 디폴트로 index.html을 찾아보도록 설정되어 있다. (index : 첫번째)

<br>

## BEM(Block Element Modifier)

- 좀 더 쉽게 읽히는 css를 가지는 규칙이다.

- `id` 와 `class`를 사용하면서 프로그래머들이 `id`를 사용했는지 `class`를 사용했는지 햇갈리는 경우가 발생해서 이문제를 해결하고자 모든 부분에 `class` 만을 사용하기로하여 생겨난 규칙이다.

- 사용유무는 자유지만 이용하는 것을 추천

- 예시

  - `.btn`
  - `btn__price`
  - `btn--orange`
  - `btn`은 블럭이고, btn안에 정보가 담겨져있다. price, orange

<br>

## 아이콘 구하는 법

- 첫째. 직접 아이콘을 구하는

- 둘째. 직접 이미지를 만들고 추출하거나 svg 파일을 이용하여 구할 수 있다.

  - svg란 픽셀이 없는 파일형식이다 수학으로만 구성된 형식

### 참고사이트

- https://heroicons.dev/
- https://fontawesome.com/

<br>

## 리셋 CSS

- 원하든 원하지 않든 브라우저가 알아서 html에 body에 적용시키는 스타일이 있는데, 이것들을 모두 없애주는 CSS파일

- reset css 카피하여 파일로 만든뒤, styles.css 에서 @import 하면된다.

  - ```css
    @import "reset.css";
    ```

- [참조사이트](https://cssreset.com/scripts/eric-meyer-reset-css/)

- 먼저 브라우저 스타일을 없애고 우리가 직접 디자인 하는 것이 더 좋은 방법!
