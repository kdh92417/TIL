# 출근하는 방법 Level 1

## 문제

영훈이는 출근할 때 계단을 통해 사무실로 가는데요. 급할 때는 두 계단씩 올라가고 여유 있을 때는 한 계단씩 올라 갑니다.

어느 날 문득, 호기심이 생겼습니다. 한 계단 또는 두 계단씩 올라가서 끝까지 올라가는 방법은 총 몇 가지가 있을까요?

계단 4개를 올라간다고 가정하면, 이런 방법들이 있습니다.

- 1, 1, 1, 1
- 2, 1, 1
- 1, 2, 1
- 1, 1, 2
- 2, 2
  총 5개 방법이 있네요.

함수 staircase는 파라미터로 계단 수 n을 받고, 올라갈 수 있는 방법의 수를 효율적으로 찾아서 리턴합니다.

<br>

## 풀이

- 이문제는 피보나치수열과 비슷한 문제로 정확히는 `fib(n+1)`은 `staircase(n)`와 똑같다.

<br>

### 힌트보고 푼 풀이

```python
def staircase(n):
    # 코드를 작성하세요.
    if n < 2:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        c = a + b
        a, b = b, c
    return c

# 테스트
print(staircase(0))
print(staircase(6))
print(staircase(15))
print(staircase(25))
print(staircase(41))
```

<br>

### Codeit 풀이

```python
def staircase(n):
    if n < 2:
        return 1

    a, b = 1, 1

    for i in range(n):
        a, b = b, a + b

    return a


# 테스트
print(staircase(0))
print(staircase(4))
print(staircase(15))
print(staircase(25))
print(staircase(41))
```

- n에 비례하는 반복문 하나가 있어서 이 함수의 시간 복잡도는 O(n)이다.

<br>

### 재귀를 이용한 풀이

```python
fib_cache = {}
def staircase(n):

    if n < 2:
        return 1

    if n in fib_cache:
        return fib_cache[n]
    else:
        temp = staircase(n-2) + staircase(n - 1)
        fib_cache[n] = temp
        return temp

# 테스트
print(staircase(0))
print(staircase(4))
print(staircase(15))
print(staircase(25))
print(staircase(41))
```

- cache를 이용하므로 부분문제를 한번만 풀게되지만 모든 부분 문제를 풀어야 하기 때문에 시간복잡도는 O(n)이 된다.
