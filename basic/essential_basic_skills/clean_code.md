# 깔끔한 코드를 위하여! 클린코드


## 목차

- [1.네이밍](#1-네이밍)
  * [컨벤션](#---)
  * [네이밍](#---)
  * [Tip](#tip)
- [2. 주석, 포맷팅](#2--------)
  * [2. 1 주석](#2-1---)
  * [2. 2 관용적으로 사용되는 키워드](#2-2---------------)
  * [2. 3 포맷팅](#2-3----)
- [3. 함수](#3---)
  * [3. 1 함수의 역할은 하나만 - SRP (Single Responsibility Principle)](#3-1---------------srp--single-responsibility-principle-)
  * [3. 2 반복하지 말자 - DRY (Don’t Repeat Yourself)](#3-2-----------dry--don-t-repeat-yourself-)
  * [3. 3 파리미터 수는 적게 유지하자](#3-3----------------)
  * [3. 4 사이드 이펙트를 잘 핸들링하자](#3-4-----------------)
  * [순수함수란?](#------)
- [4. 클래스](#4-클래스)
  * [4. 1 단일 책임 원칙(SRP) 지키기](#4-1----------srp-----)
  * [4. 2 응집도를 높이자](#4-2---------)
  * [4. 3 변경하기 쉽게 만들자](#4-3------------)
- [5. 에러 핸들링](#5-------)
  * [5. 1 - 오류 코드보다는 예외 사용하기](#5-1-------------------)
  * [예외 클래스 잘 정의하기](#-------------)
  * [에러 핸들링 잘하기](#----------)
- [6. 코드 Indent 줄이기(Guard Clausing, Polymorphism)](#6----indent-----guard-clausing--polymorphism-)
  * [6. 1 Gaurd clause](#6-1-gaurd-clause)
  * [6. 2 Polymorphism(다형성)](#6-2-polymorphism-----)



## 1.네이밍

---

### 컨벤션

- `snake_case` :  Python, Ruby 등에서 권장
- `cameCase` :  Java, Javascript 등에서 권장
- `PascalCase` : 대부분의 프로그래밍 언어에서 클래스를 네이밍할 때 사용
- `kebab-case` : HTML Element를 표현할 때 사용

### 네이밍

- 변수 : 명사 혹은 형용사로 작성
    
    ```jsx
    const userData = ... // 명사
    const isValid = ... // 형용사
    ```
    

- 함수와 메서드 : 동사 혹은 형용사로 작성
    
    ```jsx
    function sendData() {
    	...
    }
    
    function inputIsValid() {
    	...
    }
    ```
    

- 클래스 : 일반적으로 명사로 작성
    
    ```jsx
    let Client = new Object();
    ```
    

### Tip

> 구체적이고 명시적으로 적을 것, 짧고 애매한 표현보다 길고 직관적인 표현이 낫다.
> 

```jsx
// as-is
const dt = '20211219KST';

// to-be
const datetimeWithTimezone = '20211219KST';
```

<br>

## 2. 주석, 포맷팅

---

### 2. 1 주석

> 네이밍으로 표현할 수 없는 영역을 주석으로 표현
> 

- 법적인 정보를 담을 때
    
    ```jsx
    // Copyright (c) 2021...
    ```
    

- 의도를 명확하게 설명할 떄
    
    ```jsx
    // throughput을 늘리기 위해 스레드를 10개까지 늘린다.
    for (let idx = 0; idx < 11; idx++) {
    	thread = threading.Thread(target=...)
    	thread.start()
    }
    ```
    

- 중요성을 강조할 떄
    
    ```jsx
    // 최종 결재를 하기 전에 진행해야 하는 validation gkatn
    ```
    

- 결과를 경고할 떄
    
    ```jsx
    // WARNING: API 서버가 항상 양호한지 알 수 없음
    function connectApiServer() {
    	...
    }
    ```
    

### 2. 2 관용적으로 사용되는 키워드

- `TODO` : 당장은 아니지만 다음에 해야할 때
- `FIXME` : 치명적인 에러를 발생하는 코드는 아지미나 수정해야 할 때
- `XXX` : 더 생각해볼 필요가 있을 떄

### 2. 3 포맷팅

**Vertical Formatting**

- 한 파일에 코드를 다 넣지 말고, 개념에 맞게 파일을 나눠서 사용
    
    ```jsx
    // as-is
    // store.js에 전부 있음
    const FruitsStore = new Object();
    
    const DesertStore = new Object();
    
    // to-be
    // FruitStore.js
    const FruitsStore = new Object();
    
    // DesertStore.js
    const DesertStore = new Object();
    ```
    

- 다른 개념의 코드는 Spacing으로 분리
- 비슷한 개념의 코드는 붙여서 사용
    
    ```jsx
    function testUserByProduct() {
    	const user = new User()
    	const	product = new Product()
    
    	product.setSoldOut(true)
    	user.get(product)
    
    }
    ```
    

Horizontal Formatting

- 한 줄에 코드를 다 넣기보단 변수 등을 활용해서 가독성 높이기
    
    ```jsx
    // as-is
    personList.extend([Person('adam'), Person('even'), Person('noa')])
    
    // to-be
    const items = [Person('adam'), Person('even'), Person('noa')];
    personList.extend(items);
    ```
    
<br>

## 3. 함수

---

### 3. 1 함수의 역할은 하나만 - SRP (Single Responsibility Principle)

- as-is
    
    ```jsx
    const Database = new Object();
    
    function createUser(email, password) {
    	if (!email.includes('@') || email.length < 6) {
    	    throw new Error('유저 정보를 제대로 입력하세요')
    	} 
    	
    	const user = {"email" : email, "password" : password};
    	
    	const database = Database("mysql")
    	database.add(user)
    	
    	const emailClient = EmailClient()
    	emailClient.setConfig(...)
    	emailClient.send(email, "회원가입을 축하합니다")
    	
    	return true
    }
    
    createUser('@faeafaa', 'af')
    ```
    

- to-be
    
    ```jsx
    function createUser(email, password) {
      validateCreateUser(email, password);
    
      const user = buildUser(email, password)
    
      saveUser(user)
      sendEmail(email)
    
      return
    }
    
    function validateCreateUser(email, password) {
      if (!email.includes('@') || email.length < 6) {
        throw new Error('유저 정보를 제대로 입력하세요')
      }
    }
    
    function buildUser(email, password) {
      return {
        "email": email,
        "password": password
      }
    }
    
    function saveUser(user) {
      const database = Database("mysql")
      database.add(user)
    }
    
    function sendEmail(email) {
      const emailClient = EmailClient()
    	emailClient.setConfig(...)
    	emailClient.send(email, "회원가입을 축하합니다")
    }
    ```
    

### 3. 2 반복하지 말자 - DRY (Don’t Repeat Yourself)

- as-is
    
    ```jsx
    function createUser(email, password) {
      if (!email.includes('@') || email.length < 6) {
        throw new Error('유저 정보를 제대로 입력하세요')
      }
    }
    
    function updateUser(email, password) {
      if (!email.includes('@') || email.length < 6) {
        throw new Error('유저 정보를 제대로 입력하세요')
      }
    }
    ```
    

- to-be
    
    ```jsx
    function validateCreateUser(email, password) {
      if (!email.includes('@') || email.length < 6) {
        throw new Error('유저 정보를 제대로 입력하세요')
      }
    }
    
    function createUser(email, password) {
      validateCreateUser(email, password)
    }
    
    function updateUser(email, password) {
      validateCreateUser(email, password)
    }
    ```
    

### 3. 3 파리미터 수는 적게 유지하자

- as-is
    
    ```jsx
    const User = function (name, age, sex) {
      console.log(`안녕하세요 저의 이름은${name}이고, 나이는 ${age}, ${sex} 입니다.`)
    }
    
    const Adam = User('adam', '30', 'male') 
    ```
    

- to-be
    
    ```jsx
    const Person = function (name, age, sex) {
      this.name = name;
      this.age = age;
      this.sex = sex;
    }
    
    const User = function (person) {
      console.log(`안녕하세요 저의 이름은${person.name}이고, 나이는 ${person.age}, ${person.sex} 입니다.`)
    }
    
    const Eve = new Person('eve', 25, 'female')
    const newUser = User(Eve);
    ```
    

### 3. 4 사이드 이펙트를 잘 핸들링하자

> 사이드 이펙트(Side Effect)는 함수가 실행됐을 때 함수 이외의 어떤 것들에 변화를 주는 것을 뜻한다. 사이드 이펙트를 잘 다루지 못하면, 예측하지 못하는 문제들이 발생할 수 있다.
> 

```jsx
// 사이드 이펙트 X
function getUserInstance(email, password) {
  user = User(email, password)
  return user
}

// 사이드 이펙트 O
function updateUserInstance(user) {
  user.email = 'new email';
}

// 사이드 이펙트 O
function createUser(email, password) {
  user = User(email, password)
  startDBSession(); // 외부 DB Session에 변화를 줄 수 있다.
}
```

- 사이드 이펙트를 잘 핸들링 하는 방법
    1. 코드를 통해 충분히 예측할 수 있도록 네이밍을 잘하는 것이 중요
        1. update, set 같은 직관적인 prefix를 붙여서 사이드 이펙트가 있을 수 있음을 암시
    2. 함수의 사이드 이펙트가 있는 부분과 없는 부분으로 잘 나눠서 관리
        1. 명령(side effect O)과 조회(side effect X) 를 분리하는 `CQRS` 방식이 있다
    3. 일반적으로 update를 남발하기 보단 순수 함수 형태로 사용하는 것이 더 직관적이고 에러를 방지할 수 있다.
    
- as-is
    
    ```jsx
    const carts = []
    
    function addCart(product) {
    	carts.push(product)
    }
    
    const product = Product(...)
    addCart(product)
    ```
    

- to-be
    
    ```jsx
    const cart = ['apple', 'orange']
    
    function getAddedCart(product) {
      return [...cart, product]
    }
    
    const carts = getAddedCart('mango')
    
    console.log(carts)
    ```
    

### 순수함수란?

- 어떤 함수에 동일한 인자를 주었을 때 항상 동일한 값을 리턴하는 함수
- 외부의 상태를 변경하지 않는 함수
- [참조 블로그](https://jeong-pro.tistory.com/23)

<br>

## 4. 클래스

---

### 4. 1 단일 책임 원칙(SRP) 지키기

> 하나의 클래스는 하나의 책임만 가지도록 한다.
> 

- as-is
    
    ```jsx
    const Store = function () {
      
      this.communicateUser = function () {
        //
      }
    
      this.manageProducts = function () {
    		//
      }
    
      this.manageMoney = function () {
    		//
      }
    }
    ```
    

- to-be : 책임을 나눠서 Manager 클래스에게 책임을 전가
    
    ```jsx
    const CounterManager = function () {
      
      this.communicateUser = function () {
        
      }
      
    }
    
    const ProductManager = function () {
    
      this.manageProducts = function () {
    
      }
    }
    
    const Owner = function () {
    
      this.manageMoney = function () {
    
      }
    }
    ```
    

### 4. 2 응집도를 높이자

- **응집도는 클래스의 변수와 메서드들이 얼마나 유기적으로 엮여있냐를 나타내는 지표이다.**
    - 응집도가 높을수록 클래스의 메서드들은 인스턴스 변수들을 많이 사용
    - 응집도가 낮을수록 클래스의 메서드들은 인스턴스 변수들을 적게 혹은 사용하지 않는다.

- as-is
    
    ```jsx
    const LowCohesion = function () {
      let a = 'a'
      let b = 'b'
      let c = 'c'
    
      this.getA = function () {
        return a
      }
    
      this.getB = function () {
        return b
      }
    
      this.getC = function () {
        return c
      }
    }
    
    const test = new LowCohesion();
    ```
    
- to-be
    
    ```jsx
    const HighCohesion = function () {
      const abc = function () {
    
      }
    
      this.process_a = function () {
        abc.process_a();
      }
    
      this.process_b = function () {
        abc.process_b();
      }
    
      this.process_c = function () {
        abc.process_c();
      }
    }
    
    const test = new LowCohesion();
    ```
    

### 4. 3 변경하기 쉽게 만들자

> 새 기능을 수정하거나 기존 기능을 변경할 때, 코드의 변경을 최소화하는 게 중요하다
> 

일반적으로 클래스(객체)는 구현(Concrete)와 추상(Abstract)으로 나뉘게 된다. 구현에는 실제 동작하는 구체적인 코드가, 추상은 인터페이스나 추상클래스처럼 기능을 개념화한 코드가 들어간다.

일반적으로 변경하기 쉽게 설계하기 위해선 추상화를 해두고 구체 클래스에 의존하지 않고 추상 클래스(인터페이스)에 의존하도록 코드를 짜는 것이 중요하다.

- as-is
    
    ```python
    class Teacher:
        def teach(self):
            print('강의를 합니다.')
    
    class Student:
        def lesson(self):
            print('수업을 듣습니다.')
    
    class School:
        def __init__(self, people): # 구체 클래스에 의존
            self.people = people
    
    		# people이 다양해질수록 코드를 계속 변경해야됨
        def make_act(self):
            for person in self.people:
                if isinstance(person, Teacher):
                    person.teach()
                elif isinstance(person, Student):
                    person.lesson()
    ```
    
- to-be
    
    ```python
    class Person(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def act(self):
            ...
    
    # 상속을 통해 쉽게 구현이 가능 -> 확장이 열려있다.
    class Teacher(Person):
        def act(self):
            print("강의를 합니다")
    
    class Student(Person):
        def act(self):
            print("수업을 듣습니다.")
    
    class School:
        def __init__(self, people: List[Person]): #추상 클래스에 의존합니다.
            self.people = people
    
        # person이 늘어나더라도 변경에는 닫혀있다.
        def make_act(self):
            for person in self.people:
                person.act()
    ```
    
<br>

## 5. 에러 핸들링

### 5. 1 - 오류 코드보다는 예외 사용하기

> 오류 코드를 사용하게 되면 상단에 오류인지 확인하는 불필요한 로직이 들어가게 된다.  오류의 범주에 들어가지 않은 상태를 나타내는 것이라면, 예외(`Exception` )로 명시적으로 에러 처리를 표현해주는 것이 좋다.
> 

- as-is
    
    ```python
    from enum import Enum 
    
    # Enum을 이용한 에러코드 생성
    class ErrorCodes(Enum):
        VALUE_ERROR="VALUE_ERROR"
    
    def we_can_raise_error():
        ...
        return ERROR_CODES.VALUE_ERROR
    
    def use_ugly_function():   
    		result = we_can_occur_error()
        if result == ErrorCodes.VALUE_ERROR:
            # 처리 코드
        ...
    ```
    

- to-be
    
    ```python
    def we_can_raise_error():
        if ...
            raise ValueError("에러 발생")
    
    def use_awesome_function():
        try:
            we_can_occur_error()
            ...
        except ValueError as e:
            # 에러 처리 로직
    ```
    

### 예외 클래스 잘 정의하기

- 기본 `Exception` 만 쓰기 보단 내장된 `built in Exception` 을 잘 활용하면 좋다.
    - Python : **[https://docs.python.org/ko/3/library/exceptions.html](https://docs.python.org/ko/3/library/exceptions.html)**
- 상황에 맞게 `Custom Exception` 을 만들어 사용하는 것도 좋다.
    
    ```python
    # Create Custom Exception
    class WithParameterCustomException(Exception):
        def __init__(self, msg, kwargs):
            self.msg = msg
            self.kwargs = kwargs
    
        def __str__(self):
            return f"message {self.msg} with parameter {self.kwargs}"
    
    # Execute Custom Exception
    raise WithParameterCustomException("This is a problem", {"name": "grab"})
    ```
    

### 에러 핸들링 잘하기

- 에러를 포착했다면 잘 핸들링 해야된다.
    
    ```python
    def we_can_raise_error():
        ...
        raise Exception("Error!")
    
    # BAD: 에러가 났는지 확인할 수 없게 됩니다.
    def use_ugly_function1():
        try:
            we_can_raise_error()
            ...
        except:
            pass
    
    # BAD: 로그만 남긴다고 끝이 아닙니다.
    def use_ugly_function2():
        try:
            we_can_raise_error()
            ...
        except Exception as e:
            print(f"에러 발생{e}")
    
    # GOOD
    def use_awesome_function():
        try:
            we_can_raise_error()
            ...
        except Exception as e:
            logging.error(...) # Error Log 남기기
            notify_error(...) # 예측 불가능한 외부 I/O 이슈라면 회사 내 채널에 알리기(이메일, 슬랙 etc)
            raise OtherException(e) # 만약 이 함수를 호출하는 다른 함수에서 추가로 처리해야 한다면 에러를 전파하기
        finally:
            ... #에러가 발생하더라도 항상 실행되어야 하는 로직이 있다면 finally 문을 넣어주기
    ```
    
- 에러 핸들링을 모을 수 있으면 한곳으로 모은다.
    
    → 보통 같은 수준의 로직을 처리한다면 한 곳으로 모아서 처리하는 게 더 에러를 포착하기 쉽다.
    
- as-is
    
    ```python
    def act_1():
        try:
            we_can_raise_error1()
            ...
        except:
            #handling
    
    def act_2():
        try:
            we_can_raise_error2()
            ...
        except:
            #handling
    
    def act_3():
        try:
            we_can_raise_error3()
            ...
        except:
            #handling
    
    # 에러가 날 지점을 한눈에 확인할 수 없습니다. 
    # act_1이 실패하면 act_2가 실행되면 안 된다면? 핸들링하기 어려워집니다.
    def main():
        act_1()
        act_2()
        act_3()
    ```
    
- to-be
    
    ```python
    def act_1():
        we_can_raise_error1()
        ...
    
    def act_2():
        we_can_raise_error2()
        ...
    
    def act_3():
        we_can_raise_error3()
        ...
    
    # 직관적이며 에러가 날 지점을 확인하고 처리할 수 있습니다.
    # 트랜잭션같이 한 단위로 묶여야하는 처리에도 유용합니다.
    def main():
        try:
            act_1()
            act_2()
            act_3()
        except SomeException1 as e1:
            ...
        except SomeException2 as e2:	
            ...
        except SomeException2 as e3
            ...
        finally:
            ...
    ```
  
<br>
    

## 6. 코드 Indent 줄이기(Guard Clausing, Polymorphism)

> `if-else` 조건문을 많이 사용하게 되면 코드 라인이 길어지고 indent가 많아져 가독성이 떨어지는 문제가 발생한다. 이때 `Guard Clausing` 과 `Polymorhism(다형성)` 을 사용하면 코드를 클린하게 짤 수 있다.
> 

### 6. 1 Gaurd clause

`if-else` 문 같은 nested 코드를 줄이기 위해 코드 상단에 Fail이 되는 로직을 위로 넣어두는 것이 좋다.

- as-is
    
    `if-else` 문으로 중첩된  indent가 발생하여 가독성을 해침
    
    ```python
    def say_hi_to_spring_user(developer):
        if developer.is_front_end:
            raise Exception("프론트 엔지니어입니다")
        elif developer.is_back_end:
            if not developer.use_java:
                raise Exception("자바를 사용하지 않습니다")
            else:
                if developer.use_spring:
                    print("안녕하세요!")
                else:
                    raise Exception("자바의 다른 프레임워크를 사용합니다")
        else:    
            raise Exception("who are you?")
    ```
    

- to-be
    
    Fail이 되는 부분순으로 코드를 짜면 가독성이 좋아진다.
    
    ```python
    #Fail이 되는 부분을 상위로 올리면 코드를 더 쉽게 읽을 수 있습니다.
    def say_hi_to_spring_user(developer):
        if not developer.is_backend:
            raise Exception("백엔드 엔지니어가 아닙니다")
        
        if not developer.use_java:
            raise Exception("자바를 사용하지 않습니다")
    
        if not developer.use_spring:
            raise Exception("스프링을 사용하지 않습니다")
        
        print("안녕하세요!")
    ```
    

### 6. 2 Polymorphism(다형성)

- as-is
    
    ```python
    class Developer:
        def coding(self):
            print("코딩을 합니다")
    
    class Designer:
        def design(self):
            print("디자인을 합니다")
    
    class Analyst:
        def analyze(self):
            print("분석을 합니다")
    
    class Company:
        def __init__(self, employees):
            self.employees = employees
    
        def make_work(self):
            for employee in self.employees:
                if type(employee) == Developer:
                    employee.coding()
                elif type(employee) == Designer:
                    employee.design()
                elif type(employee) == Analyst:
                    employee.analyze()
    
    ```
    

- to-be
    
    ```python
    # Employee로 추상화해둡니다.(다형성)
    class Employee(metaclass=abc.ABCMeta):
        @abc.abstractmethod
        def work(self):
            ...
    
    class Developer(Employee):
        def work(self):
            print("코딩을 합니다")
    
    class Designer(Employee):
        def work(self):
            print("디자인을 합니다")
    
    class Analyst(Employee):
        def work(self):
            print("분석을 합니다")
    
    class Company:
        def __init__(self, employees: List[Employee]):
            self.employees = employees
    
        # if문을 사용하지 않고 다형성을 통해서 이를 해결합니다.
        def make_work(self):
            for employee in self.employees:
                employee.work()
    ```