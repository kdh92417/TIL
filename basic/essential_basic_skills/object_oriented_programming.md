
## 목차

- [Basic concepts of object-oriented](#basic-concepts-of-object-oriented)
  * [1. Class and Instance](#1-class-and-instance)
    + [1. 1 Class](#1-1-class)
    + [1.2 Instance](#12-instance)
  * [2. Attributes and Methods](#2-attributes-and-methods)
    + [2. 1 Attribute](#2-1-attribute)
    + [2.2 Methods](#22-methods)
  * [3. Inheritance](#3-inheritance)
  * [4. Interface](#4-interface)
    + [Why use interfaces](#why-use-interfaces)
    

- [Features of object-oriented](#features-of-object-oriented)
  * [1. Responsibility and Cooperation](#1-responsibility-and-cooperation)
    + [1.1 Responsibility](#11-responsibility)
    + [1.2 Cooperation](#12-cooperation)
  * [2. Abstract](#2-abstract)
  * [2. Polymorphism And Dependency injection](#2-polymorphism-and-dependency-injection)
    + [2.1 Concepts](#21-concepts)
    + [2.2 TIP](#22-tip)
  * [3. Encapsulation](#3-encapsulation)
    + [3. 1 When not encapsulated](#3-1-when-not-encapsulated)
    + [3. 2 When encapsulated](#3-2-when-encapsulated)
  * [4. Conclusion](#4-conclusion)
    + [책임과 협력](#책임과-협력)
    + [추상화](#추상화)
    + [다형성](#다형성)
    + [캡슐화](#캡슐화)

# Basic concepts of object-oriented

## 1. Class and Instance

### 1. 1 Class

- 클래스는 객체
- Example
    
    ```python
    class Person:
    		pass
    ```
  
<br>
    

### 1.2 Instance

- 클래스를 하나의 인스턴스로 만들 수 있다. → ‘클래스를 인스턴스화’ 라 한다.
- Example
    
    ```python
    Adam = Person()
    Eve = Person()
    ```
    
    위의 `Adam` 과 `Eve` 는 Person Class로부터 만들어졌지만 서로 다른 인스턴스이다 즉, 이 둘은 같은 형태(클래스)를 취하고 있지만, 각자 **다른 메모리 공간에 존재**하고, **각자 독립된 내용**을 담을 수 있다.
    
<br>

## 2. Attributes and Methods

### 2. 1 Attribute

> 클래스의 속성(Attribute)은 클래스에 내에 담기는 데이터들을 말하며, `멤버 변수` 라고도 한다.
클래스 속성은 크게 `클래스 변수` 와 `인스턴스 변수` 로 나눠볼 수 있다.
> 

- 인스턴스 변수
    - 인스턴스 별로 독립적으로 가질 수 있는 값
    
    ```python
    class Job:
        def __init__(self, name, job):
    				# Instance variables
            self.name = name
            self.job = job
    
    Adam = Job('Adam', 'Backend')
    Eve = Job('Eve', 'Frontend')
    
    print(Adam.name, Adam.job)  # Adam Backend
    print(Eve.name, Eve.job)  # Eve Frontend
    ```
    

- 클래스 변수
    - 클래스 자체에 정의되는 변수
    - 인스턴스끼리 같은 클래스 변수를 공유 한다.
    
    ```python
    class Job:
    		# Class variables
        country: str = 'South of Korea'
    
        def __init__(self, name, job):
            self.name = name
            self.job = job
    
    Adam = Job('Adam', 'Backend')
    Eve = Job('Eve', 'Frontend')
    
    # 같은 클래스의 인스턴스들은 똑같은 클래스변수를 가진다.
    print(Adam.country)  # South of Korea
    print(Eve.country)  # South of Korea
    
    # 인스턴스화 하지않고 클래스변수에 바로접근
    print(Job.country)  # South of Korea
    ```
    
<br>

### 2.2 Methods

> 클래스가 가지고 있는 함수이자 객체가 할 수 있는 행위
메서드는 크게 공개형(public) 메서드와 비공개형(private) 메서드로 나눠볼 수 있다. 
 
<br>

- Public Methods
    - 공개형 메서드는 클래스 외부에서 사용가능하다.
    
    ```python
    from mimetypes import init
    
    class Job:
        country: str = 'South of Korea'
    
        def __init__(self, name, job) -> None:
            self.name = name
            self.job = job
    
    		# Public Method
        def work(self) -> None:
            print(f'My job is {self.job}')
    
    Adam = Job('Adam', 'Backend')
    Eve = Job('Eve', 'Frontend')
    
    # 클래스외부에서 공개형 메서드의 사용
    Adam.work()  # My job is Backend
    Eve.work()  # My job is Frontend
    ```
  
<br>

- Private Methods
    - 클래스 내부에서만 사용하는 메서드
    - 파이썬의 경우 접근 제어자 문법이 없다 →이름 앞에  `_` 를 붙여 비공개 변수(메서드)임을 명시한다.
    - `Mangling` : `__` 언더바 두개를 붙여 더 `private` 하게 관리할 수 있으나 완전한 방법이 아니다.
    
    ```python
    class Job:
        country: str = 'South of Korea'
    
        def __init__(self, name, job) -> None:
            self.name = name
            self.job = job
    
        def work(self) -> None:
            work_type = self._get_work_type()
            print(f'My job is {work_type}')
    
        def _get_work_type(self) -> str:
            if self.job == 'Backend':
                return '백엔드 엔지니어'
            elif self.job == 'Frontend':
                return '프론트 엔지니어'
    ```
    → 비공개형 메서드는 외부에서 접근하지 못하거나, 할 수 있더라도 하지 않는 것이 관습

    → 공개형 메서드의 로직의 일부를 내부적으로 재사용하고, 의미를 분리하기 위해 사용하기 위한 목적으로 사용되곤 함

<br>

## 3. Inheritance

> 상속은 이전에 정의한 클래스의 데이터와 메서드를 그대로 내려받는 기능.
이 때, 상속해주는 클래스를 `부모 클래스` 혹은 `기반 클래스` 라고 하며 상속받는 클래스를 `자식 클래스` 혹은 `파생 클래스` 라고 한다.
> 

<br>

- Example
    
    ```python
    # 부모 클래스
    class School:
        def act(self) -> None:
            print(f'나는 {self.identity} 입니다.')
    
    # 자식 클래스
    class Student(School):
        identity = '학생'
    
    # 자식 클래스
    class Teacher(School):
        identity = '선생님'
    
    student = Student()
    teacher = Teacher()
    
    student.act()
    teacher.act()
    ```
    
<br>

## 4. Interface

> 인터페이스는 객체의 행위(메서드)만을 정의한 것으로, 구체적으로는 클래스 메서드의 명세라고 볼 수 있다.
> 

<br>

- 파이썬에서는 인터페이스가 따로 없어 추상클래스로 인터페이스를 구현
    
    ```python
    from abc import ABC, abstractmethod
    
    # 추상 클래스를 상속받아 인터페이스 구현
    class School(ABC):
        @abstractmethod
        def act(self) -> None:
            pass
    
    class Student(School):
    		# 상속받은 인터페이스의 메서드를 구현
        def act(self) -> None:
            print("I'm Student")
    
    class Teacher(School):
    		# 상속받은 인터페이스의 메서드를 구현
        def act(self) -> None:
            print("I'm Teacher")
    
    student = Student()
    teacher = Teacher()
    
    student.act()
    teacher.act()
    ```
    
<br>

### Why use interfaces

위의 인터페이스구현에서 클래스를 사용하는 유저 입장에서는 해당 `School` 이 어떤 행위를 제공하는지 (`Public Methodd`)에 주로 관심이 있다. `School` 이 어떤 데이터를 들고 있고 행위를 하기위해 어떤 알고리즘을 가지고 동작하는지 관심이 없다.

따라서 `School` 을 사용하는 입장에서 `School` 이라고하는 인터페이스만 보면 된다.

→ 구현(저수준 코드)을 의존하기 보단 인터페이스(고수준) 의존하게 되어 결합도를 낮출 수 있다. (**다형성**)

또한 `Student(School)` , `Teacher(School)` 같은 구현클래스가 `School` 클래스를 상속받아 구현 클래스간의 관계를 파악하기도 쉽다.

<br>

# Features of object-oriented

## 1. Responsibility and Cooperation

### 1.1 Responsibility

<br>

> 책임은 한 객체가 특정하게 수행해야하는 범위와 기능을 뜻한다.

<br>

- 사람은 ‘운전’이라는 행위를 하게 된다. → `User` 객체는 운전하는 것에 대한 책임이 있다.
    
    ```python
    class User:
    		def __init__(self) -> None:
    				pass
    
    		def drive(self) -> None:
    				pass
    ```
    
<br>

- 차량은 앞뒤로 가능 기능을 제공 → `MorningCar` 객체는 가속과 감속에 대한 책임이 있다.
    
    ```python
    class MorningCar:
        def __init__(self) -> None:
            pass
    
        def accelerate(self) -> None:
            pass
    
        def decelerate(self) -> None:
            pass
    ```

<br>

> SRP (Signle Responsibility Principle)
>
>하나의 객체는 하나의 책임만 가지도록 설계하는 것이 일반적으로 좋다. 왜냐하면,
>
>- 객체의 정체성이 명확하고, 변경에 용이 하며, 추후 재사용 가능하고
>- 높은 응집도와 낮은 결합도를 유지할 수 있기 때문

<br>

### 1.2 Cooperation

위에서 정의한 `User` 객체와 `MorningCar` 객체의 기능을 구현해보자

- `User`
    
    ```python
    class User:
        def __init__(self) -> None:
            self.car = MorningCar()  # User는 MorningCar를 의존하고 있습니다.
    
        def drive(self) -> None:
            self.car.accelerate()  # User는 MorningCar가 제공하는 공개 메서드를 사용합니다.
    ```
    
<br>

- `MorningCar`
    
    ```python
    class MorningCar:
        def __init__(self):
             self.speed = 0 
             self._fuel = 0  # 파이썬 특성상 private을 _ prefix를 붙여 암묵적으로 사용함
    						
        def accelerate(self):
            self.speed += 1
    
        def decelerate(self):
            self.speed -= 1
    ```
<br>

- 사람이 운전하는 상황
    - 결과적으로 `User` , `MorningCar`  객체를 각자 책임에 맞게 설계하고 `User` 가 `MorningCar` 객체를 호출하여 구현
    - 이렇게 객체가 서로 필요에 따라 의존하는 것을 `협력` 이라고 표현한다.
    
<br>

> **책임 주도 설계**
>
> 객체 지향에서 필요한 객체들의 책임을 중심으로 시스템을 설계하는 방법을 뜻함
>
> 하나의 책임 → 하나의 객체 → 책임 곧 객체의 정체성
>
> 책임주도 설계로 시스템을 설계해나가면
> - 객체들의 정체성이 명확
> - 높은 응집도와 낮은 결합도 유지
> - 시스템은 객체들의 협력으로 로직을 진행

<br>

## 2. Abstract

> 추상화란?
>
> 어떤 구체적인 애들로부터 공통적인 특징들을 뽑아서 만들어 놓은 고수준의 개념체
> 

<br>

- `MorningCar` 객체와 `PorscheCar` 객체의 차량이 있다면 공통특징을 뽑아서 `Car` 라는 추상화 객체를 만들 수 있다.
    
    ```python
    from abc import ABC
    
    # 모든 차량의 공통적인 특징을 뽑아서 만든 추상화 객체
    class Car(ABC):
        @abstractmethod
        def accelerate(self) -> None:
            pass
    
        @abstractmethod
        def decelerate(self) -> None:
            pass
    ```
  
<br>

- 추상화 객체인 `Car` 를 상속받아 `MorningCar` 객체와 `PorscheCar` 객체를 구현할 수 있다.
    
    ```python
    class MorningCar(Car):
        def __init__(self) -> None:
             self.speed = 0
             self._fuel = 0
    
        def accelerate(self) -> None:
            self.speed += 1
    
        def decelerate(self) -> None:
            self.speed -= 1
    
    class PorscheCar(Car):
        def __init__(self) -> None:
            self.speed = 0
            self._fuel = 0
    
        def accelerate(self) -> None:
            self.speed += 3
    
        def decelerate(self) -> None:
            self.speed -= 3
    ```
    
<br>

- 사람 입장에서는 특정 차량이 아니라 추상적인 `Car` 라는 객체만 알면 된다.
    
    ```python
    class User:
        def __init__(self, car: Car) -> None:
            self.car = car
    
        def drive(self):
            self.car.accelerate()
    
    porsche = User(PorscheCar())
    porsche.drive()
    ```

<br>

> 이렇게 구체적인 객체들로부터 공통점을 생각하여 한 차원 높은 개념을 만들어 내는(생각해내는) 것을 `추상화(abstraction)` 라고 한다.

<br>

## 2. Polymorphism And Dependency injection

### 2.1 Concepts

- 다형성(Polymorphism)과 의존성 주입(Dependency injection) 예시
    
    ```python
    # 모닝 차량을 운전하고 싶을 때
    # User클래스에 MorningCar 주입 -> MorningCar를 User클래스에 의존성 주입
    user = User(MorningCar())
    user.drive()
    
    # 포르쉐 차량을 운전하고 싶을 때
    # User클래스에 PorscheCar 주입 -> PorscheCar를 User클래스에 의존성 주입
    user = User(PorscheCar())
    user.drive()
    ```
    

- `User` 클래스가 `Car` 의 자식클래스인 `MorningCar` , `PorscheCar` 객체를 생성자에서 파라미터로 넘겨 각기 다른 차를 운전하는 `user` 를 생성할 수 있는데, 이런 특성을 `다형성(Polymorphism)` 이라 한다.
    
    
- 또한 이때 외부에서 실제로 의존하는 객체(`MorningCar` , `PorscheCar` )를 만들어 넘겨주는 패턴을 `의존성 주입(Dependency injection)` 이라 한다.

<br>

### 2.2 TIP

> **OCP (Open-Close Principle)**
>
>소프트웨어는 확장에대해 열려 있어야 하고, 수정에 대해서는 닫혀 있어야한다는 원칙
>즉 요구사항이 바뀌어 기존 코드를 변경할 때, 기존 코드를 수정하지 않고 새로운 코드를 추가하는 것이 좋다는 것

<br> 

## 3. Encapsulation

> **캡슐화(Encapsulation)** 는 객체 내부의 데이터나 구체적인 로직을 외부에서 모르고 사용해도 문제가 없도록 하는 특성

<br>

### 3. 1 When not encapsulated

- Code Example
    
    ```python
    class MorningCar:
        def __init__(self, fuel: int) -> None:
            self.speed = 0
            self.current_fuel = fuel
            self.max_fuel = 50
            if fuel > self.max_fuel:
                raise Exception(f"최대로 넣을 수 있는 기름은 {self.max_fuel}L 입니다")
    
        def accelerate(self) -> None:
            if self.current_fuel == 0:
                raise Exception("남아있는 기름이 없습니다")
            self.speed += 1
            self.current_fuel -= 1
    
        def decelerate(self) -> None:
            if self.current_fuel == 0:
                raise Exception("남아있는 기름이 없습니다")
            self.speed -= 1
            self.current_fuel -= 1
    ```

<br>

- Use `MorningCar` object
    
    ```python
    # 차량 생성
    >>> car = MorningCar(30)
    
    # 차량 주행
    >>> car.accelerate()
    
    # 차량에 필요한 기름 주유
    >>> car.current_fuel += 50
    
    # 차량의 남은 주유랑을 퍼센트로 확인
    >>> f"{car.current_fuel / car.max_fuel * 100} %"
    ```

<br>
    

- 위의 캡슐화하지 않은 `MorningCar` 객체를 사용함으로써 클래스변수에 직접 접근하여 연산하게되는데, 이러면 `car.max_fuel` 을 초과한 값이 `current_fuel` 클래스변수에 들어갈 수 있어 버그에 취약한 코드가 된다.

- 이렇게 캡슐화 되지 않은 코드는
    - 본인의 책임을 다하고 있지 않으며(SRP 위반)
    - 추후 코드 변화에도 매우 취약하다.
    - e.g. `MorningCar` 객체의 `fuel` 변수의 이름이 다른 이름으로 바뀌게 되면 → `MorningCar` 를 사용하는 모든 코드를 수정 해야됨
        
<br>

### 3. 2 When encapsulated

- `MorningCar` 클래스를 캡슐화
    - 외부에서 이 객체에 필요로 하는 기능을 메서드로 제공
    - 객체의 속성을 직접 수정하거나 가져다 쓰지 못하도록 함 → `정보은닉` 이라고도 함

<br>

- Encapsulation
    
    ```python
    class MorningCar:
        def __init__(self, fuel: int) -> None:
            self.speed = 0
            self._current_fuel = fuel  # 비공개형 변수로 바꿉니다.
            self._max_fuel = 50  # 비공개형 변수로 바꿉니다.
            if fuel > self._max_fuel:
                raise Exception(f"최대로 넣을 수 있는 기름은 {self.max_fuel}L 입니다!")
    
        def accelerate(self) -> None:
            if self._current_fuel == 0:
                raise Exception("남아있는 기름이 없습니다!")
            self.speed += 1
            self._current_fuel -= 1
    
        def decelerate(self) -> None:
            if self._current_fuel == 0:
                raise Exception("남아있는 기름이 없습니다!")
            self.speed -= 1
            self._current_fuel -= 1
    
        # 차량에 주유할 수 있는 기능을 메서드로 제공하고, 구체적인 로직은 객체 외부에서 몰라도 되도록 메서드 내에 둡니다.
        def refuel(self, fuel: int) -> None:
            if self._current_fuel + fuel > self._max_fuel:
                raise Exception(f"추가로 더 넣을 수 있는 최대 연료는 {self._max_fuel - self._current_fuel}L 입니다!")
            self._current_fuel += fuel
    
        # 차량의 남은 주유랑을 퍼센트로 확인하는 기능을 메서드로 제공합니다.
        def get_current_fuel_percentage(self) -> str:
            return f"{self._current_fuel / self._max_fuel * 100} %"
    
    ```
    
    ```python
    # 차량 생성
    >>> car = MorningCar(30)
    
    # 차량 주행
    >>> car.accelerate()
    
    # 차량에 필요한 기름 주유 (예외 발생함)
    >>> car.refuel(50)
    
    # 차량의 남은 주유랑을 퍼센트로 확인
    >>> car.get_current_fuel_percentage()
    ```

<br>

- `MorningCar` 클래스를 사용하는 클라이언트 `MorningCar` 의 속성에 직접 접근하여 연산할 필요가 없다.
    - `MorningCar` 가 제공하는 퍼블릭메서드를 사용하면 된다.
    - `MorningCar` 의 속성 `_current_fuel` 이나 `_max_fuel` 등의 값이 바뀌어도 클라이언트의 코드는 바뀌지 않는다. → 수정에 더 용이한 코드가 됨
    
<br>

## 4. Conclusion

### 책임과 협력

- 객체지향은 객체들의 책임과 협력으로 이루어 진다.

### 추상화

- 추상화를 통해 객체들의 공통 개념을 뽑아 한 차원 더 높은 객체를 만들 수 있다.
    - 객체를 추상화한 클래스를 만든 후, 이 클래스를 상속받아 실제 구체적인 책임을 담당하는 객체를 생성할 수 있다. → 구현

### 다형성

- 다형성으로 코드는 수정과 확장에 유연

### 캡슐화

- 캡슐화를 통해 객체 내부의 정보와 구체적인 로직을 숨길 수 있다. → 정보은닉
    - 외부에선 공개메서드를 사용
    - 수정과 확장에 유연

<br>

## 4. Dependency

> 변경이 전파되기 때문에 의존성이 중요


### 4.1 정적 의존성 (컴파일 의존성)

- 객체 A입장에서 객체 B의 존재를 알고 있을 때, ‘객체 A는 객체 B에 의존성이 있다’라고 한다.
    
    → 코드 레벨에서 직접적으로 두 객체의 의존 관계를 파악할 수 있을 때 `정적 의존성` 이 있다고 한다.
    
    ```python
    # Driver 클래스는 Car 클래스의 존재를 알고 있다. -> Driver클래스는 Car클래스에 의존성이 있다.
    class Driver:
        def __init__(self, name, car: Car) -> None:
            self.name = name
            self.car = car
    ```
    
    → `Driver` 객체가 `Car` 객체에 `정적 의존성` 이 있다.
    
<br>

### 4. 2 동적 의존성 (런타임 의존성)

> 코드 레벨이 아닌 실제 런타임 환경에서 동적으로 의존 관계를 형성하는 것
> 

- 아래 코드에서 `Driver` 객체는 `Car` 객체의 정적 의존성이 있지만 `Boxter` 객체와 `Panamera` 객체에는 의존성이 없다.
    
    ```python
    from abc import ABC, abstractmethod
    
    class Car(ABC):
        @abstractmethod
        def car_type(self) -> None:
            pass
    
    class Boxter(Car):
        def car_type(self) -> str:
            return 'Open Car'
    
    class Panamera(Car):
        def car_type(self) -> str:
            return 'Sport Sedan'
    
    class Driver:
    		# 추상 클래스 혹은 인터페이스를 파라미터 타입으로 초기화
        def __init__(self, name, car: Car) -> None:
            self.name = name
            self.car = car
    
        def drive(self) -> None:
            print(f'{self.name}이 {self.car.car_type()}을 운전합니다.')
    ```
    

- 코드가 실행될 때(런타임 환경) `Boxter` , `Panamera` 에 동적 의존성을 만들 수 있다.
    
    ```python
    # 구현클래스를 인자로 넘긴다. -> 동적으로 의존성 생성
    boxter = Driver('adam', Boxter()) 
    panamera = Driver('eve', Panamera())
    
    boxter.drive()  # adam이 Open Car을 운전합니다.
    panamera.drive()  # eve이 Sport Sedan을 운전합니다.
    ```
    

> 위와 같이 정적 의존성 대상을 고수준코드(`Car`)로 동적 의존성 대상을 저수준 코드(`Boxter` , `Panamera`) 로 넣어주게 되면 유연한 설계가 가능해진다.

<br>

## 5. Coupling and Cohesion

![결합도와 응집도](https://yansfil.github.io/awesome-class-materials/assets/img/cohesion-coupling.5549777b.png)

> 객체지향에서 좋은 설계란? ‘낮은 결합도(Coupling)와 높은 응집도(Cohesion)를 가진 설계’ 라고 말한다.
> 

### 5. 1 Cohesion

> 객체의 책임에 맞게 속성과 메서드가 유기적으로 결합되어 있는 정도를 `응집도` 라고 한다.
> 

- 응집도를 높게 코드를 작성하면 → 관령성이 높은 속성과 메서드가 모인다.
    
    → 흐름을 읽기 편해지고, 
    
    → 불필요한 속성과 메서드를 줄일 수 있어 더 탄탄한 코드를 작성할 수 있다.
    
- 응집도가 낮은 경우
    
    ```python
    class LowCohesion:
        def __init__(self):
            self.a = ...
            self.b = ...
            self.c = ...
        
        def process_a(self):
            print(self.a)
        
        def process_b(self):
            print(self.b)
        
        def process_c(self):
            print(self.c)
    ```
    
- 응집도가 높은 경우
    
    ```python
    class HighCohesion:
        def __init__(self):
            self.abc = ...
        
        def process_a(self):
            self.abc.process_a()
        
        def process_b(self):
            self.abc.process_b()
        
        def process_c(self):
            self.abc.process_c()
    ```

<br>    

### 5. 2 Coupling

> 객체간 의존하는 정도(정적 의존성)를 `결합도` 라 한다.
> 

- `결합도` 가 높을 수록 (한 객체가 다른 객체의 정보(정보, 메서드)를 많이 알 수록)
    - 의존하는 객체의 속성이나 메서드가 수정 → 다른 객체 역시 영향을 받는다.
    - 따라서, 객체를 생성하거나 내부의 로직을 이해하는 데 비용이 커짐

- `결합도` 를 낮게 유지할 수 있는 방향으로 코드를  짜야됨
    - 객체지향 설계에서는 객체 간의 협력이 필수 → 의존 관계를 없애는 것은 불가능
    - 결합도를 낮추기 위해서는
        - 캡슐화를 통해 내부 구현 로직을 숨기고 외부로 노출할 메서드를 추상화
        - 팩토리 패턴, 파사드 패턴과 같은 디자인 패턴을 활용

- `결합도` 가 높은 경우
    
    ```python
    class Developer:
        def drink_coffee(self):
            ...
        
        def turn_on_computer(self):
            ...
        
        def open_ide(self):
            ...
        
        ...
    
    class Company:
        def make_work(self):
            developer = Developer()
            print(f"{developer.name}가 일을 시잡합니다!")
            developer.drink_coffee()
            developer.turn_on_computer()
            developer.open_ide()
            ...
    ```
    

- 캡슐화를 통해 `결합도` 가 낮춘 경우
    
    ```python
    class Developer:
        def develop(self):
            print(f"{self.name}가 일을 시잡합니다!")
            self.drink_coffee()
            self.turn_on_computer()
            self.open_ide()
            ...
        
        def drink_coffee(self):
            ...
        
        def turn_on_computer(self):
            ...
        
        def open_ide(self):
            ...
        
        ...
    
    class Company:
        def make_project(self):
            developer = Developer()
            developer.develop()
    ```
    
<br>

### 5. 3 Summary

객체지향에서의 좋은 설계란?

- 개별 객체에는 책임에 따른 기능들이 충분히 모여있고 → `높은 응집도`
- 이런 객체들이 서로 협력하는 과정에서 의존하는 정도를 최소한으로 만드는 것 → `낮은 결합도`