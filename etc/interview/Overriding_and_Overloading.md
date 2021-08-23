# Overriding & Overloading

## Overriding

- 부모 클래스에서 정의한 메서드를 자식클래스에서 재정의하는 것(덮어씌우기)

```python
# 부모 클래스
class Calc(object):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        return self.num1 + self.num2

c = Calc(2, 3)
print(c.sum())

# 자식 클래스(부모클래스 상속)
class Minus(Calc):
        # Override
    def sum(self):
        return self.num1 - self.num2

m = Minus(2, 3)
print(m.sum())
```

## Overloading

---

- 동일한 이름의 함수를 매개변수에 따라 다른 기능으로 동작하게 하는 것
- 파이썬에서는 오버로딩을 정식으로 지원하지 않는다.

> 오버라이딩 과 오버로딩을 비교하자면 오버라이딩은 클래스의 상속 시에를 클래스를 수정하는 것이고 오버로딩은 하나의 메서드에 다형성을 부여하는 것이다.
