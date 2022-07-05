# k진수에서 소수 개수 구하기

## 문제

- [k진수에서 소수 개수 구하기](https://school.programmers.co.kr/learn/courses/30/lessons/92335)


<br>

## 풀이 

```python
import math


def convert(num, base):
    T = '0123456789'
    q, r = divmod(num, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
    
    
def is_primenumber(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    nums = convert(n, k).split('0')

    for num in nums:
        if num != '' and is_primenumber(int(num)):
            answer += 1
    
    return answer
```

이 문제을 접하면서 소수판별하는 법, `N` 진법으로 변환하는 로직을 공부할 수 있엇고, 마지막 `solution` 풀이에서 각 패턴에 따라 숫자를 필터링 하는 것은 간단하게 `0` 을 기준으로 `split()`하면 간단하게 패턴에 맞는 숫자들을 걸러줄 수 있엇다.