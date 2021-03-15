# Recursive Algorithm

## 재귀 함수란

하나의 함수에서 자신을 다시 호출하여 작업을 수행 하는 함수

- Recursive case : 현 문제가 너무 커서, 같은 형태의 더 작은 부분 문제를 재귀적으로 푸는 경우

- Base case : 이미 문제가 충분히 작아서, 더 작은 부분 문제로 나누지 않고도 바로 답을 알 수 있는 경우

<br>

## 예제

### 피보나치 수열 재귀함수로 구현해보기

```python
# n번째 피보나치 수를 리턴
def fib(n):
    # Base Case
    if n < 3:
        return 1
    # Recursive Case
    else:
        return fib(n - 2) + fib(n - 1)

# Test
for i in range(1, 11):
    print(fib(i))
```

<br>

### 1부터 n까지의 합인 n번째 삼각수(triangle number)를 구현

```python
# 1부터 n까지의 합을 리턴
def triangle_number(n):
    # Base Case
    if n < 2:
        return n

    # Recursive Case
    else:
        return triangle_number(n - 1) + n


# Test
for i in range(1, 11):
    print(triangle_number(i))
```
