# Html 과 CSS를 이용하여 Messenger Website를 만들면서 배운 것들

## .gitignore

- `.gitignore` : 깃에 올리고싶지 않은 것들을 자동으로 올리지 제외시키게 하는 파일이다.

  - 파일을 `.gitignore`로 만든 뒤, `.확장자` 쓰면 된다.
  - 폴더는 `/폴더이름`

## index.html

- index.html : 대부분의 웹 서버가 디폴트로 index.html을 찾아보도록 설정되어 있다. (index : 첫번째)

## BEM(Block Element Modifier)

- 좀 더 쉽게 읽히는 css를 가지는 규칙이다.

- `id` 와 `class`를 사용하면서 프로그래머들이 `id`를 사용했는지 `class`를 사용했는지 햇갈리는 경우가 발생해서 이문제를 해결하고자 모든 부분에 `class` 만을 사용하기로하여 생겨난 컨벤션이다.

- 예시

  - `.btn`
  - `btn__price`
  - `btn--orange`
  - `btn`은 블럭이고, btn안에 정보가 담겨져있다. price, orange
