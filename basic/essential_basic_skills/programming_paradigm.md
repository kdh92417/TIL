


# What is a programming paradigm

> 프로그래밍 패러다임은 프로그래밍할 때 관점을 제공해주고, 설계를 결정하도록 돕는 패러다임
> 

- 절차지향 프로그래밍 : 프로그래밍을 함수적 호출 과정을 중심으로 바라보고 설계
- 객체 지향 프로그래밍 : 객체의 책임과 협력을 중심으로 설계


<br>

## Table of Contents


* [1. Procedure Oriented](#1-procedure-oriented)
  + [Concept](#concept)
  + [Example](#example)
  + [Pros and Cons](#pros-and-cons)
  + [Conclusion](#conclusion)
- [2. Object Oriented Programming](#2-object-oriented-programming)
  * [Example](#example)
  * [Pros and Cons](#pros-and-cons)
- [3. Functional Programming](#3-functional-programming)
  * [Outline](#outline)
  * [Pure Function](#pure-function)
  * [Why don't you want to have an external state?](#why-don-t-you-want-to-have-an-external-state-)
  * [Functional Programming Example](#functional-programming-example)
  * [Pros and Cons](#pros-and-cons-1)
- [4. Organize](#4-organize)
  * [Procedure Oriented Programming](#procedure-oriented-programming)
  * [Object Oriented Programming](#object-oriented-programming)
  * [Functional Programming](#functional-programming)
  

<br>

## 1. Procedure Oriented

### Concept

> 절차지향(Procedure Oriented) 프로그래밍은 프로시저 콜, 즉 함수 호출을 중심으로 프로그래밍을 생각하는 것
> 

- 데이터를 중앙 집중식으로 관리 → 프로세스 로직과 데이터가 별도의 위치에 분리
- 작은 함수단위로 나누고 프로그래밍 메인 로직이 시작되는 곳부터 하위 로직이 실행되는 곳까지 `TOP -> DOWN` 방식으로 구성되곤 한다.

### Example

```python
def read_input_file(file_path: str) -> str:
    if file_path.endwith(".txt"):
        reader = get_file_reader(file_type="txt")
        return reader.read(file_path)
    elif file_path.endwith(".csv"):
        reader = get_file_reader(file_type="csv")
        return reader.read(file_path)
    elif file_path.endwith(".xlsx"):
        reader = get_file_reader(file_type="xlsx")
        return reader.read(file_path)
    else:
        raise ValueError("파일 확장자는 txt, csv, xlsx 중 하나여야 합니다.")

def get_file_reader(file_type: str) -> Reader:
    if file_type == "txt":
   		...
    elif file_type == "csv":
        ...
    elif file_type == "xlsx":
        ...

def parse_input_data(data: str) -> List[str]:
    ...

def save_data(data: List[str]) -> None:
    ...

def main() -> None:
    data = read_input_file("input_file.txt")
    parsed_data = parse_input_data(data)
    save_data(parsed_data)
    
if __name__ == "__main__":
    main()
```

<br>

### Pros and Cons

- 장점
    - 절차지향 프로그래밍으로 작성된 코드는 일반적으로 이해하기 쉽다. ← `TOP -> DOWN` 식이고 함수단위로 나뉘어져 있기 때문
    - 로직이 복잡한 것이나 계속해서 기능을 확장해나가야 하는 것이 아니라면, 유지보수도 용이

- 단점
    - 전체 로직이 매우 복잡하거나 동적으로 로직을 바꿔야 하는 등의 기능 확장이 필요할 때 유지보수가 어렵다.

### Conclusion

따라서 절차지향은 프로그램이 수행하는 알고리즘이 명확하고, 기능 확장 등이 자주 일어나지 않는 상황에서 사용하기에 좋다.

<br>

## 2. Object Oriented Programming

> 객체라고 하는 단위에 책임을 명확히 하고 서로 협력하도록 프로그래밍 하는 패러다임
> 

- 절차지향과 다르게 객체는 데이터와 함수(메서드)를 함께 가지고 있다.
- 객체 내부의 데이터는 외부에 공개할 필요가 없거나 해서는 안 되는 데이터라면 모두 자신 내부에 숨겨 알지 못하도록 한다.

### Example

- 사용자로부터 파일을 입력받아 파일을 파싱한 후, 이 내용을 저장소에 저장하는 코드
    
    ```python
    from abc import abstractmethod, ABC
    from typing import List
    
    class Processor:
        def __init__(self,
                     file_reader: FileReader,
                     data_parser: DataParser,
                     repository: Repository) -> None:
            self.file_reader = file_reader
            self.data_parser = data_parser
            self.repository = repository
    
        def execute(self, file_path: str) -> None:
            data = self.file_reader.read(file_path)
            parsed_data = self.data_parser.parse(data)
            self.repository.save(parsed_data)
    
    # 데이터를 파싱하는 역할
    class DataParser:
        def parse(self, data: str) -> List[str]:
            ...
    
    #저장소에 파일을 저장하는 역할
    class Repository:
        def init(self, database_url: str):
            ...
    
        def save(self, data: List[str]) -> None:
            ...
    
    # 파일을 읽는 추상 클래스
    class FileReader(ABC):
        def read(self, file_path: str) -> str:
            self._validate(file_path)
            data = self._open_file(file_path)
            return self._read(data)
    
        @abstractmethod
        def _read(self, data: str) -> str:
            pass
    
        # 공통으로 사용하는 메서드입니다.
        def _validate(self, file_path: str) -> None:
            if not file_path.endwith(self.file_type):
                raise ValueError(f"파일 확장자가 {self.file_type} 아닙니다.")
    
        @abstractmethod
        def _open_file(file_path: str) -> str:
            ...
    
    # FileReader 상속
    # txt 파일을 읽는 책임을 가진 FileReader 파생 클래스입니다.
    class TxtFileReader(FileReader):
        def file_type(self) -> str:
            return "txt"
    
        def _read(self, data: str) -> str:
            ...
    
        ...
    
    # FileReader 상속
    # csv 파일을 읽는 책임을 가진 FileReader 파생 클래스입니다.
    class CsvFileReader(FileReader):
        def file_type(self) -> str:
            return "csv"
    
        def _read(self, data: str) -> str:
            ...
    
        ...
    
    # FileReader 상속
    # xlsx 파일을 읽는 책임을 가진 FileReader 파생 클래스입니다.
    class XlsxFileReader(FileReader):
        def file_type(self) -> str:
            return "xlsx"
    
        def _read(self, data: str) -> str:
            ...
    
        ...
    
    # 프로세서 실행 (txt 파일을 읽어야할 경우)
    class Main:
        def run(self) -> None:
            processor = Processor(
                file_reader=TxtFileReader(),
    	        	data_parser=DataParser(),
                repository=Repository()
            )
    
    # 프로세서 실행 2 (CSV 파일을 읽어야할 경우)
    class Main:
        def run(self) -> None:
            processor = Processor(
                file_reader=CsvFileReader(), # 이 한줄만 바뀝니다.
    	        	data_parser=DataParser(),  
                repository=Repository()
            )
    
    ```
    

- 위의 프로그래밍은 전체적으로 객체와 객체 간의 메서드 호출로 이루어짐
- 각 객체는 자신의 기능을 수행하는데 필요한 데이터를 직접 가지고 관리할 수 있다.
- `FileReader` 클래스를 상속받아서 각각의 파일종류별로 실행할 수 있도록 확장성있게 코드를 짤 수 있다.
    - `TxtFileReader`, `CsvFileReader`, `XlsxFileReader` 클래스가 모두 `FileReader` 의 파생 클래스 → 이런 객체 지향의 특성을 “**다형성**” 이라 한다.
    - 어떤 객체에 필요한 객체를 때에 따라 다르게 주입하는 것을 “**의존성 주입**” 이라 한다.
    
<br>

### Pros and Cons

- 여러명의 개발자들이 협력하거나, 확장 가능하도록 코드를 설계해야 하는 경우 적합
- 확장이 가능하고 유연한 만큼 처음 코들르 보는 사람들은 어렵고 헷갈릴 수 있다.
- 실행 환경에서 입력에 따라 다양한 작업 흐름이 만들어지기 때문에 → 디버깅하기가 상대적으로 어려움

<br>

## 3. Functional Programming

> 함수형 프로그래밍은 외부 상태를 갖지 않는 함수들의 연속으로 프로그래밍을 하는 패러다임이다, 즉 같은 입력을 넣었을 때 언제나 같은 출력을 내보낸다는 의미
> 

### Outline

> 기존 개체 지향 프로그래밍에서 가지는 문제를 해결하는 대안으로 `함수형 프로그래밍` 이 주목받고 있다.
> 

- 함수의 비일관성 : 객체의 멤버 변수가 변경될 경우 함수(메서드)가 다른 결과를 반환할 수 있다.
- 객체간 의존성 문제 : 객체 간 상호작용을 위해서 다른 객체의 함수들을 호출 → 이는 자연스럽게 프로그램 복잡도를 증가시킴
- 객체 내 상태 제어의 어려움 : 외부에서 객체의 상태를 변경하는 메소드들이 호출되면 → 언제 어디서 객체의 상태를 변경했는지 추적이 어려움
- 함수형 프로그래밍 코드에서는 한번 초기화한 변수는 변하지 않는다. 이런 특성을 `불변성` 이라고 하는데, 이 `불변성` 을 통해 `안정성` 을 얻을 수 있다.

<br>

### Pure Function

> 함수형 프로그래밍에서는 함수가 외부 상태를 갖지 않는다는 것이 중요하다. 이를 위해서 외부의 상태를 갖지 않는 `순수 함수` 를 사용한다.
> 

- 일반 함수
    
    ```python
    c = 1
    
    def func(a: int, b: int) -> int:
        return a + b + c  # c 라는 외부 값, 상태가 포함되어 있기에 함수형이 아닙니다.
    ```
    
- 순수 함수
    
    ```python
    def func(a: int, b: int, c: int) -> int:
        return a + b + c  # 주어진 파라미터만 사용합니다. 별도의 상태가 없습니다.
    ```
  
<br>

### Why don't you want to have an external state?

> 일반적으로 통제하지 못하는 외부 상태를 사용한다면 예측하지 못한 결과를 가질 수 있기 때문
> 

```python
class Calculator:
    def __init__(self, alpha: int) -> None:
        self.alpha = alpha
        self.beta = 0

    def run() -> int
    	return self.alpha + self.beta

# run메서드실행시 항상 같은값을 가지라는 보장이 없다.
calculator = Calculator(alpha=3)
calculator.run()  # 3 반환
calculator.beta = 1
calculator.run()  # 4 반환
```

- 위의 코드 처럼 언제든지 상태가 변할수 있는 것을 가리켜 `사이드 이펙트` 라 한다.
    - 객체지향에서는 위의 문제를 해결하고자 접근제어자( `private` , `protected` )와 같은 기능등을 제공하지만 완벽한 솔루션이 되지 못한다.
    
<br>

### Functional Programming Example

함수형 프로그래밍은 보통 다음과 같은 순서로 문제를 해결

1. 문제를 잘개 쪼갠다.
2. 쪼개진 문제들 중 하나를 해결하는 **순수 함수**를 만든다.
3. 순수 함수들을 결합하여 문제들을 해결

보통 함수형 프로그래밍에서는 함수를 조합하는 방식으로 `Pipelining` , `PartialApplication` , `Curring` 등이 있다.

```python
# Pipelining
def main():
    pipe_func = pipe(read_input_file, parse_input_data, save_data)
    return pipe_func("input_file.txt")

# Partial application
def power(base, exp): #powering
    return base ** exp

def main():
    square = partial(power, exp=2)
    cube = partial(power, exp=3)
    square(2) #2의 제곱인 4 반환
    cube(2) #2의 세제곱인 8 반환
```

<br>

### Pros and Cons

- 사이드가 이펙트가 없기 때문에 → 안정적이다.
- 따라서 동시성을 가지는 프로그램에 사용하기 적합
    - 특히 대용량 데이터를 병력적으로 처리할 때 사이드 이펙트가 없도록 설계하는 것이 매우 중요한데, 최근 데이터 처리기술의 발전으로 함수형프로그래밍이 부상

- 실제로 함수형 프로그래밍을 하기 위해선, 상태를 허용하지 않기에 → 객체 지향과 같은 기능의 코드를 구현하려면 다양한 함수들을 조합해서 사용해야됨
- 친숙하지 않은 설계방식으로 인해 러닝커브가 높다.

<br>

## 4. Organize

> 프로그래밍 패러다임이란 프로그래밍을 어떤 기준으로 바로보고 작성할 것인지에 대한 관점
> 

### Procedure Oriented Programming

- 순차적인 함수 호출의 관점
- TOP → DOWN
- 코드를 확장하거나 자주 실행에 따라 로직이 바뀌어야 하는 경우에 수정이 어렵다

<br>

### Object Oriented Programming

- 다형성과 의존성 주입으로 코드를 확장하기 쉬우며, 실행환경의 다양한 입력에 대응하기 좋다
- 하지만, 런타임이 되기 전에 실제로 코드가 어떤 방향으로 흐르는지 알기 어려우며, 디버깅도 어렵다

<br>

### Functional Programming

- 상태를 갖지 않는 함수들의 활용
- 상태를 갖지 않기 때문에 → 예측에서 벗어나는 결과(사이드 이펙트)가 없다.
- 하지만 실제로 상태를 가지지 않는 함수를 작성하고 활용하는 코드를 작성하는 것은 어렵다.