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