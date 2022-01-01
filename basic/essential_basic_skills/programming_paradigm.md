


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
* [2. Object Oriented](#2-object-oriented)

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

### Pros and Cons

- 장점
    - 절차지향 프로그래밍으로 작성된 코드는 일반적으로 이해하기 쉽다. ← `TOP -> DOWN` 식이고 함수단위로 나뉘어져 있기 때문
    - 로직이 복잡한 것이나 계속해서 기능을 확장해나가야 하는 것이 아니라면, 유지보수도 용이

- 단점
    - 전체 로직이 매우 복잡하거나 동적으로 로직을 바꿔야 하는 등의 기능 확장이 필요할 때 유지보수가 어렵다.

### Conclusion

따라서 절차지향은 프로그램이 수행하는 알고리즘이 명확하고, 기능 확장 등이 자주 일어나지 않는 상황에서 사용하기에 좋다.

<br>

## 2. Object Oriented