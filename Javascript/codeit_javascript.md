# Basic

```jsx
// Wrong
console.log("He said "i'm Iron man"");

// Collect
// 따음표 앞에 역슬래쉬를 같이 입력하면 된다.
console.log ("he said \"i\'m Iron Man\"");

// 백틱을 이용
console.log (`he said "i'm Iron Man"`);

// 문자열 사칙 연산 가능
conosle.log('Hello' + 'World'); // HelloWorld
```

<br>

## typeof 연산자

```jsx
function sayHello() {
  console.log('Hello');
}

console.log(typeof 'sfsa')   // string
console.log(typeof 13)       // number
console.log(typeof 13.3)     // number
console.log(typeof sayHello) // function

// NaN (Not a Number)
console.log(typeof 8 - 3)    // typeof가 사칙연산보다 우선순위이기때문에 NaN 이 된다.
```

## 형 변환 (Type Conversion)

<br>

```jsx
// 문자열로 바꿀때 -> String
console.log(String(31))

// 숫자형으로 바꿀때 -> Number
console.log(Number('31'))
```

## 템플릿 문자열

```jsx
let year = 2021;
let month = 10;
let day = 18;

// qorxlrrhk ${} 템플릿문자열을 이용하여 가독성 높게 코드를 작성 가능하다.
console.log(`생년월일은 ${year}년 ${month}월 ${day}일 입니다.`)
// 생년월일은 2021년 10월 18일 입니다.
```

`null` VS `undefined`

- null : 값이 없음
- undefined : 값이 지정되지 않았음

<br>

## 옵셔널 파라미터

- Python 과 마찬가지로 뒤쪽에 선언해주는 것이 좋다

<br>

## 변수의 Scope

```jsx
// Scope : 범위 , 영역
function myFunction() { // 블록 문 (Block Statement)
  let x = 3;
  console.log(x);
}

	myFunction();    // 3
console.log(x);    // Uncaught ( x is not defined )
```

```jsx
// Scope : 범위 , 영역
let x = 3;    // 글로벌 변수, 전역 변수 (Global Bariable)

function myFunction() { // 블록 문 (Block Statement)
	let x = 5; // 로컬 변수, 지역 변수 (Local Variable)
  console.log(x);
}

myFunction();
console.log(x);

// 5
// 3
```