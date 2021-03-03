# Dynamic Programming

중복을 피하여 효율적인 알고리즘 짜는 법

<br>

## Memorization

- 중복되는 계산은 한번만 계산 해두어 저장
- 비효율성을 해결하는 알고리즘

<br>

## 예시

```python
def fib_memo(n, cache):
    # Base Case
    if n < 3:
        return 1

    # cache에 n이 저장되어 있으면 저장되어있는 값을 바로 리턴
    if n in cache:
        return cache[n]

    # 아직 n번째 피보나치 수를 계산하지 않았으면 계산을 한 후 cache에 저장
    cache[n] = fib_memo(n-1, cache) + fib_memo(n-2, cache)
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))
'''
Out Put
55
12586269025
354224848179261915075
'''
```
