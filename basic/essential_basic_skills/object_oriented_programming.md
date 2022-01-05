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
    

> 이렇게 구체적인 객체들로부터 공통점을 생각하여 한 차원 높은 개념을 만들어 내는(생각해내는) 것을 `추상화(abstraction)` 라고 한다.
>